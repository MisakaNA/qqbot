import requests, re

class exchange_rates:

    def __init__(self, duiqian, duihou):
        self.duiqian = str(duiqian).upper()
        self.duihou = str(duihou).upper()

    def exchange(self):



        url = 'https://webapi.huilv.cc/api/exchange?num=100&chiyouhuobi=%s&duihuanhuobi=%s&callback=jisuanjieguo&_=1567062403595' % (self.duiqian, self.duihou)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        req = requests.get(url=url, headers=headers).content.decode('utf-8')

        huilv = re.findall(r':\"(.*?)\"', req)[1]
        frommoney = re.findall(r':\"(.*?)\"', req)[0][3:]
        tomoney = re.findall(r':\"(.*?)\"', req)[2][8:]
        updatetime = re.findall(r':\"(.*?)\"', req)[5]

        if huilv == '':
            return '暂不支持所输入国家或地区的汇率查询'

        return '%s对%s的汇率为\t%s\n更新时间：%s\n注意：查询结果非银行牌价，具体数额请以银行挂牌价为准！' % (frommoney, tomoney, huilv, updatetime)

