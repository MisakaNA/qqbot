
class exchangehelp:

    def __init__(self, country):
        self.country = country

    def get_code(self):

        code = {
            '澳大利亚': 'AUD',
            '加拿大': 'CAD',
            '中国': 'CNY',
            '中国大陆': 'CNY',
            '古巴': 'CUP',
            '英国': 'GBP',
            '德国': 'DEM',
            '丹麦': 'DKK',
            '缅甸': 'MMK',
            '西班牙': 'ESP',
            '柬埔寨': 'KHR',
            '欧元': 'EUR',
            '欧洲': 'EUR',
            '芬兰': 'FIM',
            '法国': 'FRF',
            '希腊': 'GRD',
            '香港': 'HKD',
            '中国香港': 'HKD',
            '新西兰': 'NZD',
            '爱尔兰': 'IEP',
            '冰岛': 'ISK',
            '荷兰': 'NLG',
            '意大利': 'ITL',
            '日元': 'JPY',
            '朝鲜': 'KPW',
            '韩国': 'KRW',
            '蒙古': 'MNT',
            '澳门': 'MOP',
            '中国澳门': 'MOP',
            '马尔代夫': 'MVR',
            '希腊': 'GRD',
            '墨西哥': 'MXP',
            '马来西亚': 'MYR',
            '挪威': 'NOK',
            '俄罗斯': 'RUB',
            '瑞典': 'SEK',
            '新加坡': 'SGD',
            '泰国': 'THB',
            '台湾': 'TWD',
            '中国台湾': 'TWD',
            '美国': 'USD',
        }

        try:
            value = code[self.country]
        except KeyError:
            return '很抱歉，数据库中没有该国家或地区对应的货币代码，请检查输入或自行搜索'

        return '%s的货币代码为： %s' % (self.country, value)



