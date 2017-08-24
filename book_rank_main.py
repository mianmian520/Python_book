# -*-coding:utf-8 -*-
import urlparse

import db_manager
import html_downloader
import html_parser
import url_manager

class RankMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 网页下载器
        self.downloader = html_downloader.HtmlDowmloader()
        # 网页解析器
        self.parser = html_parser.HtmlParser()

    # 爬取网站内容
    def craw(self, url):
        for i in range(1, 20):
            self.urls.add_new_url(urlparse.urljoin(url, '?page=%d' % i))
            # print self.urls.get_new_url()
        db = db_manager.Db_Manager()
        while self.urls.has_new_url():
            try:
                content = self.downloader.download(self.urls.get_new_url(), 'qidian')
                datas = self.parser.parser_rank(url, content)
                print datas
                for data in datas:
                    db.add(data)
            except Exception as e:
                print e
        db.close()



if __name__ == "__main__":
    root_url = "http://r.qidian.com/recom"
    rank = RankMain()
    rank.craw(root_url)