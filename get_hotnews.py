import re, requests, sys
from urllib import parse
from bs4 import BeautifulSoup


class hotNews:
    def __init__(self):
        self.hot = []
        self.how = []

    def get_news_list(self):
        url = 'https://www.baidu.com/s?wd=搜索热点&rsv_spt=1&rsv_iqid=0xc0f5da900017c49e&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie' \
              '=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&inputT=13299&rsv_t=a8a5vGxVZhb%2FjDAY68TS2n7AVBS%2Fn' \
              'j5od82M6trNIqenw8iF24e%2FyCpTRHi5qh9Sq3kt&oq=1&rsv_pq=e371757000080e3e&rsv_sug2=0&rsv_sug4=13299'

        req = requests.get(url=url).text

        self.hot = re.findall(r'<span class="c-index.*?c-gap-icon-right-small">\d*</span><a target=\"_blank\" title=\"(.*?)\"', req)[:10]
        self.how = re.findall(r'<td class=\"opr-toplist1-right\">(.*?)<i', req)[:10]



    def list_toStrng(self):
        resultstr = '当前热点：\n'
        count = 1
        print(len(self.hot))
        for idx in range(len(self.hot)):

            resultstr += '%d. %s \t点击量：%s\n' % (count, self.hot[idx], self.how[idx])
            count += 1
        return resultstr

    def get_news_url(self, num):

        print(self.hot)

        newstitle = self.hot[int(num)-1]

        newstitleencode = newstitle.encode('gbk')
        newstitleencode = str(newstitleencode)[2:len(str(newstitleencode)) - 1]
        newstitleencode = newstitleencode.replace('\\x', '%')

        url = 'https://search.sina.com.cn/?q=%s&range=all&c=news&sort=time' % newstitleencode

        req = requests.get(url).text
        try:
            newsurl = re.findall(r'<h2><a href=\"(.*?)\" target=\"_blank\">', req)[0]
        except IndexError:
            return -1

        else:
            return newsurl


    def get_news_detail(self, num):

        if self.get_news_url(num) == -1:
            return '啊哦，还没有关于该热点的详细报道呢。。。要不再等等？'

        articlestr = ''
        articleurl = self.get_news_url(num)



        try:

            result = {}
            article = []
            res = requests.get(articleurl)
            res.encoding = 'utf-8'
            temp = res.text
            texts = re.findall(r'<p>*([^\x00-\xff]*)</p>', temp)
            soup = BeautifulSoup(res.text, 'html.parser')
            result['title'] = soup.select('.main-title')[0].text
            timesource = soup.select('.date')[0].contents[0]
            result['time'] = timesource
            article2 = soup.select('.article p')[0:-1]

            for p in article2:
                article.append(p.text.strip())
            result['article'] = article

            for each in range(len(result['article'])):
                articlestr += result['article'][each]

            articlestr += '\n发布时间：%s' % result['time']

        except IndexError:
            articlestr += '暂不支持该新闻的格式，点击链接试试吧~\n' + articleurl

        return articlestr











