import ASUCourseFinder as a
import re, requests
import time, logging
def main():

    startTime = time.time()
    r = a.ASUCourses(code='CSE', num='355')

    t = r.find_class()
    print(t)
    #b = r.get_news_detail(2)

    logging.warning('消耗时间：%.2fs' % (time.time() - startTime))

    #print(t)




if __name__ == '__main__':
    main()


