# coding:utf-8

# url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = []
    # 添加url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)

    # 添加urls
    def add_new_urls(self, urls):
        if urls is None and len(urls) != 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 是否有url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 取url
    def get_new_url(self):
        url = self.new_urls.pop(0)
        self.old_urls.append(url)
        return url