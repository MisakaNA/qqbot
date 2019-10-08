import re, requests

class GetWeather:

    def __init__(self, city):
        self.city = city


    def get_weather(self):

        cityname = self.city + '天气'
        url = 'https://www.baidu.com/s?wd=%s&rsv_spt=1&rsv_iqid=0xe89f04d50010e61a&issp=1&f=8&rsv' \
              '_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug2=0&inputT=23626&rsv_sug4=24998' % cityname

        req = requests.get(url=url, timeout=10).text
        try:
            date = re.findall(r'<p class=\"op_weather4_twoicon_date\">\n[\s]*\n[\s]*\n[\s]*(.*?) 周',req)[0]
            tomodate = re.findall(r'<p class=\"op_weather4_twoicon_date_day\">(.*?)</p>\n',req)[0]
            temperature = re.findall(r'<p class=\"op_weather4_twoicon_temp\">(.*?)</p>', req)[0]
            tomotemperature = re.findall(r'<p class=\"op_weather4_twoicon_temp\">(.*?)</p>', req)[1]
        except IndexError:
            return '天气信息暂不可用！'

        try:
            weather = re.findall(r'weath\"\n*[\s]*>\n[\s]*(.*?)\n[\s]*</p>', req)[0]
        except IndexError:
            weather = re.findall(r'weath\"\n[\s]*title=\"\">\n[\s]*(.*?)\n', req)[0]
        try:
            tomoweather = re.findall(r'weath\">\n[\s]*(.*?)\n[\s]*</p>', req)[1]
        except IndexError:
            tomoweather = re.findall(r'weath\"\n[\s]*title=\"\">\n[\s]*(.*?)\n', req)[1]

        windinfo = re.findall(r'<p class="op_weather4_twoicon_wind">(.*?)</p>', req)[0]
        tomowindinfo = re.findall(r'<p class="op_weather4_twoicon_wind">(.*?)</p>', req)[1]

        return '%s的天气情况如下：\n今天(%s)：%s \t气温：%s \t风向：%s \n明天(%s)：%s \t气温：%s \t风向：%s' \
               % (self.city, date, weather, temperature, windinfo, tomodate, tomoweather, tomotemperature, tomowindinfo)