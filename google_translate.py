import requests, re

class translateapi:

    def __init__(self, lang, txt):
        self.lang = lang
        self.txt = txt


    def get_translate_language(self):
        lang_dict = {
            '中文': 'zh-CN',
            '汉语': 'zh-CN',
            '简体中文': 'zh-CN',
            '繁体中文': 'zh-TW',
            '德语': 'de',
            '俄语': 'ru',
            '法语': 'fr',
            '韩语': 'ko',
            '拉丁语': 'la',
            '日语': 'ja',
            '泰语': 'th',
            '西班牙语': 'es',
            '意大利语': 'it',
            '印地语': 'hi',
            '英语': 'en',
            '英文': 'en',
        }

        try:
            langf = lang_dict[str(self.lang)]
        except KeyError:
            return -1
        else:
            return langf


    def get_translate_result(self):

        if self.get_translate_language() == -1:
            return '暂不支持该语言呢。。。'

        url = 'https://translate.google.com/m?hl=en&sl=auto&tl=%s&ie=UTF-8&prev=_m&q=%s' % (self.get_translate_language(), str(self.txt))
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        req = requests.get(url=url, headers=headers, timeout=5).content.decode('utf-8')

        try:
            resstr = re.findall(r'\"t0\">(.*?)</div>', req)[0]
            resstr = str(resstr).replace('&#39;', '\'')

            if len(str(self.txt)) > 10:
                result = '翻译结果为：\n' + resstr
            else:
                result = '“' + str(self.txt) + '”的' + str(self.lang) + '翻译为：\n' + resstr

        except IndexError:
            result = '啊哦，翻译姬出错惹~试试别的输入吧'

        return result
