import get_hotnews as a
import re, requests
import time, logging
def main():

    startTime = time.time()
    r = a.hotNews()

    t = r.get_news_list()
    print(t)
    b = r.get_news_detail(2)

    logging.warning('消耗时间：%.2fs' % (time.time() - startTime))

    print(b)




if __name__ == '__main__':
    main()


