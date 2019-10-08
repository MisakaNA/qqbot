import requests,random

class nmsl:

    def __init__(self, mode):
        self.mode = mode

    def get_string(self):
        if self.mode == '火力全开':
           return self.get_nmsl()

        elif self.mode == '口吐莲花':
            return self.get_shadiao()

        else:
            choice = random.randint(0, 3)

            if choice == 0:
                return self.get_nmsl()
            else:
                return self.get_shadiao()


    def get_nmsl(self):

            url = 'https://nmsl.shadiao.app/api.php?lang=zh_cn'

            req = requests.get(url).text

            return str(req)

    def get_shadiao(self):

            url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
            req = requests.get(url).text

            return str(req)


