import re, requests

class asuratings:
    def __init__(self, prof=''):
        self.prof = prof

    def set_professor(self):
        professor = str(self.prof).replace(' ', '+')

        return professor

    def ASUrating(self):

        asuurl = 'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName' \
                 '&schoolName=Arizona+State+University&schoolID=45&query=%s' % self.set_professor()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        tempreq = requests.get(url=asuurl, headers=headers).content.decode('utf-8')

        try:
            getid = re.findall(r'<a href="/ShowRatings\.jsp\?tid=(\d*)">', tempreq)[0]
        except IndexError:
            return ['信息暂不可用']

        asuratingurl = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s' % getid

        req = requests.get(url=asuratingurl, headers=headers).content.decode('utf-8')

        try:
            getoverall = re.findall(r'<div class="grade" title="">(.*?)</div>', req)[0]
            gettakeagain = re.findall(r'<div class=\"grade\" title=\"\">[\s]+(.*?)[\s]+</div>', req)[0]

        except IndexError:
            return ['信息暂不可用']

        rmplist = [getoverall, gettakeagain]

        return rmplist