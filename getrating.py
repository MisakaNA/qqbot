import re, requests
#import time, logging


class rmp:

    def __init__(self, schoolname=' ', profname=' '):
        #self.startTime = time.time()
        if schoolname != ' ' and profname != ' ':
            self.schoolname = schoolname
            self.professorname = profname
        else:
            return


    '''
        def ASUrating(asuprof=''):
            prof = str(asuprof).replace(' ', '+')
    
            asuurl = 'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=Arizona+State+University&schoolID=45&query=%s' % prof
    
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    
            tempreq = requests.get(url=asuurl, headers=headers).content.decode('utf-8')
    
            getid = re.findall(r'<a href="/ShowRatings\.jsp\?tid=(\d*)">',tempreq)[0]
    
            asuratingurl = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s' % getid
    
            req = requests.get(url=asuratingurl, headers=headers).content.decode('utf-8')
    
            getasuoverall = re.findall(r'<div class="grade" title="">(.*?)</div>', req)[0]
            getasutakeagain = re.findall(r'<div class=\"grade\" title=\"\">[\s]+(.*?)[\s]+</div>', req)[0]
            #getasuhottag = re.findall(r'<span class=\"tag\-box\-choosetags\">[\s]+(.*?)[\s]+<b>(.*?)</b></span>', req)[0][0]
    
            asulist = [getasuoverall, getasutakeagain]
    
            return asulist
    '''


    def set_school(self):
        try:
            school = str(self.schoolname).replace(' ', '+')
        except AttributeError:
            return 'q'
        else:
            return school

    def set_professor(self):
        professor = str(self.professorname).replace(' ', '+')

        return professor

    def get_teacher(self):
        url = 'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=%s&query=%s' % (self.set_school(), self.set_professor())

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        req = requests.get(url=url, headers=headers).content.decode('utf-8')

        regex = r'<a href="/ShowRatings\.jsp\?tid=(\d*)">'

        try:
            teacherid = re.findall(regex,req)[0]

            return teacherid

        except Exception:
            return -1

    def get_rating(self):
        ratingurl = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s' % self.get_teacher()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        req = requests.get(url=ratingurl, headers=headers).content.decode('utf-8')

        try:
            getdepartment = re.findall(r'Professor in the (.*?) department', req)[0]
            getoverall = re.findall(r'<div class="grade" title="">(.*?)</div>', req)[0]
            gettakeagain = re.findall(r'<div class=\"grade\" title=\"\">[\s]+(.*?)[\s]+</div>', req)[0]
            getdifficulty = re.findall(r'<div class=\"grade\" title=\"\">[\s]+(.*?)[\s]+</div>', req)[1]
            gethottag1 = re.findall(r'<span class=\"tag\-box\-choosetags\">[\s]+(.*?)[\s]+<b>(.*?)</b></span>', req)[0][0]
            gethottag2 = re.findall(r'<span class=\"tag\-box\-choosetags\">[\s]+(.*?)[\s]+<b>(.*?)</b></span>', req)[1][0]

        except IndexError:
            #logging.warning('消耗时间：%.2fs' % (time.time() - startTime))
            return '该教授信息暂不可用！'

        else:
            #logging.warning('消耗时间：%.2fs' % (time.time() - startTime))
            return (
                self.professorname +
                '\n学院：' + getdepartment +
                '\n综合评分：' + getoverall +
                '\n反选率：' + gettakeagain +
                '\n课程难度：' + getdifficulty +
                '\n热门标签：' + gethottag1 + ', ' + gethottag2
            )

if __name__ == '__main__':
    print(rmp('Arizona State University', 'Yinong Chen').get_rating())