# -*-coding:utf-8 -*-
import file_outputer
import html_downloader
import html_parser
import url_manager

class BookMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 网页下载器
        self.downloader = html_downloader.HtmlDowmloader()
        # 网页解析器
        self.parser = html_parser.HtmlParser()
        # 文件读写工具
        self.outputer = file_outputer.Outputer()

    # 爬取网站内容写入文件
    # url 小说网站地址
    # type 网站类别
    def craw(self, url, type):
        # 得到小说网站的内容
        content = self.downloader.download(url, type)
        # 得到小说的标题和章节url列表
        title, new_urls = self.parser.parser_chapter(url, content, type)
        print title
        # 往章节url列表添加到管理器
        self.urls.add_new_urls(new_urls)
        # 章节url列表数量
        chapter_count = len(new_urls)
        print "一共有%d章" % chapter_count
        count = 1
        # 循环取出url管理器中的url
        # 判断url管理器是否还有url
        while self.urls.has_new_url():
            try:
                # 得到一个新的url
                new_url = self.urls.get_new_url()
                # 得到章节网址的内容 type用来区分不同的网站
                cont = self.downloader.download(new_url, type)
                # 解析章节网址的内容，得到章节题目和内容
                datas = self.parser.parser_content(new_url, cont, type)
                # print datas['content'].encode("utf-8")
                # self.outputer.collect_data(datas)
                # 把章节题目和内容写入文件
                self.outputer.outputer(title, datas)
                # if count == 10:
                #     break
                count += 1
                print "下载进度%d%%" % (count*100/chapter_count)
            except Exception as e:
                print e
                break
        # self.outputer.outputer_file(title)

if __name__ == '__main__':
    # http://www.bxwx.io/list/1.html   新笔下文学
    # http://book.qidian.com/info/1005986941#Catalog 起点
    # http://www.qu.la/book/18049/ or http://www.xxbiquge.com/12_12416/
    # or http://www.biquge5200.com or http://www.biquge5.com/   笔趣阁
    # http://www.17k.com   17K
    # root_url = "http://www.bxwx.io/book/24168/"
    root_url = "http://www.17k.com/list/493239.html"

    # 得到type 用来区分不同的网站
    if root_url.find("http://book.qidian.com") != -1:
        type = 'qidian'
    elif root_url.find("http://www.bxwx.io") != -1:
        type = 'xbxwx'
    # elif root_url.find("http://www.bxwx9.org") != -1:
    #     type = 'bxwx'
    elif root_url.find("http://www.qu.la") != -1 \
            or root_url.find("biquge") != -1:
        type = 'biquge'
    elif root_url.find("http://www.17k.com") != -1:
        type = '17K'
    else:
        type = '0'
        print "没有找到来自%s的内容" % root_url
    if type != '0':
        book = BookMain()
        book.craw(root_url, type)