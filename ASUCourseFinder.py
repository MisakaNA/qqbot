import re, requests
#import time, logging
import ASUrmp

class ASUCourses:

    def __init__(self, code=' ', num = ' '):
        #self.startTime = time.time()
        self.code = code
        self.num = num

    def find_class(self):
        url = 'https://webapp4.asu.edu/catalog/myclasslistresults?t=2197&s=%s&n=%s&hon=F&promod=F&e=open&page=1' % (self.code, self.num)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        req = requests.get(url=url, headers=headers).content.decode('utf-8')

        try:
            howmany = re.findall(r'Showing \d to \d+ of (\d+)', req)[0]
            classcode = re.findall(r'>[\s]+<span>[\s]+(.*?)[\s]+</span>', req)[0]
            classnumber = re.findall(r'[1-9]\d{4}(?!\d)', req)
            profname = re.findall(r'<span id=\"For_?\d*">[\s]+<span>[\s]+[\s\S]*?<span>[\s]?(.*?)[\s]*</span>', req)
            proffullname = re.findall(r'title=\"Instructor\|(.*?)\"', req)
            seatsinfo = re.findall(r'<div class=\"col\-xs\-3\">[\s]+(\d+)[\s]+</div>', req)

        except IndexError:
            return '暂无开放的该课程信息'

        t = 0
        for each in profname:
            if each != 'Staff':
                each = each[22:]
                profname[t] = each
            t += 1

        classnumberList = []
        profnameList = []
        proffullnameList = []
        seatsremainList = []
        seatstotalList = []

        for each in classnumber:
            if each not in classnumberList:
                classnumberList.append(each)


        for each in profname:
            if each != 'Staff':
                if each not in profnameList:
                    profnameList.append(each)

        for each in proffullname:
            if each not in proffullnameList:
                proffullnameList.append(each)

        count = 1
        for each in seatsinfo:
            if count % 2 == 0:
                seatstotalList.append(each)
            else:
                seatsremainList.append(each)
            count += 1

        rmpoverall = []
        rmptag = []
        for each in proffullnameList:
            rmpinfo = ASUrmp.asuratings(each).ASUrating()

            if rmpinfo[0] == '信息暂不可用':
                rmpoverall.append(rmpinfo[0])
                rmptag.append(rmpinfo[0])
            else:
                rmpoverall.append(rmpinfo[0])
                rmptag.append(rmpinfo[1])



        profrmpDict = {each : {} for each in profnameList}
        count = 0
        for each in profnameList:
            profrmpDict[each]['RMP综合评分：'] = rmpoverall[count]
            profrmpDict[each]['反选率：'] = rmptag[count]
            count += 1


        result = '课程 %s\n' % classcode
        for each in range(int(howmany)):
           if  profname[each] != 'Staff':
                result +=  '课号：%s  \t任课教授：%s  \t座位信息：%s/%s  \tRMP综合评分：%s  \t反选率：%s  \n' \
                      % (classnumberList[each], profname[each], seatsremainList[each], seatstotalList[each],
                       profrmpDict[profname[each]]['RMP综合评分：'], profrmpDict[profname[each]]['反选率：'])
           else:
                result += '课号：%s  \t任课教授：%s  \t座位信息：%s/%s  \tRMP综合评分：信息暂不可用  \t反选率：信息暂不可用  \n' \
                         % (classnumberList[each], profname[each], seatsremainList[each], seatstotalList[each])
        
        #logging.warning('消耗时间：%.2fs' % (time.time() - startTime))
        return result
















