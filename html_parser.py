# coding:utf-8
import re
import urlparse

from bs4 import BeautifulSoup

# HTML解析器
class HtmlParser(object):

    # 解析小说章节
    def parser_chapter(self, url, content, type):
        if url is None or content is None:
            return None
        soup = BeautifulSoup(content, 'html.parser')
        title = self.get_title(soup, type)
        urls = self.get_new_urls(url, soup, type)
        return title, urls

    # 得到章节标题
    def get_title(self, soup, type):
        # 根据不同的网站type 获取标题方式不同
        if type == 'qidian':
            return soup.find("div", class_ = "book-info").find("h1").find("em").get_text()
        elif type == 'xbxwx':
            return soup.find("div", id = "info").find("h1").get_text()
        elif type == 'bxwx':
            return soup.find("div", id = "title").get_text()
        elif type == 'biquge':
            return soup.find("div", class_ = "box_con").find("div", id = "info").find("h1").get_text()
        elif type == "17K":
            return soup.find("div", class_ = "Main List").find("h1").get_text()

    # 得到章节的urls
    def get_new_urls(self, url, soup, type):
        new_urls = []

        # 根据不同的网站type 获取章节url方式不同
        if type == 'qidian':
            lis = soup.find("div", class_ = "volume-wrap").find_all("li")
            links = []
            for li in lis:
                links.append(li.find("a"))
        elif type == 'xbxwx':
            links = soup.find("dl", class_ = "zjlist").find_all("a")
        elif type == 'bxwx':
            links = soup.find("table").find_all("a")
        elif type == 'biquge':
            links = soup.find("div", id = "list").find_all("a")
        elif type == '17K':
            links = soup.find("div", class_ = "Main List").find_all("a", href = re.compile(r"/chapter/"))

        for link in links:
            new_url = link['href']
            full_url = urlparse.urljoin(url, new_url)
            # print full_url
            new_urls.append(full_url)
        return new_urls

    # 解析小说章节内容
    def parser_content(self, url, content, type):
        if url is None or content is None:
            return None
        soup = BeautifulSoup(content, 'html.parser', from_encoding = 'utf-8')
        new_datas = self.get_new_datas(url, soup, type)
        return new_datas

    # 得到章节数据数据
    def get_new_datas(self, new_url, soup, type):
        new_datas = {}
        new_datas['url'] = new_url


        if type == 'qidian':
            title = soup.find('div', class_ = 'text-head').find("h3", class_ = "j_chapterName")
            content = soup.find('div', class_ = 'read-content j_readContent')
            new_datas['content'] = content.get_text(separator='\n')
        elif type == 'xbxwx':
            title = soup.find("div", class_ = "border").find("h1")
            content = soup.find('div', id = 'content')
            new_datas['content'] = content.get_text()
        elif type == 'biquge':
            title = soup.find("div", class_ = "content_read").find("div", class_ = "bookname").find("h1")
            content = soup.find("div", class_ = "content_read").find("div", id = "content")
            new_datas['content'] = content.get_text(separator='\n')
        elif type == '17K':
            title = soup.find("div", class_ = "read").find("h1")
            content = soup.find("div", class_ = "read").find("div", class_ = "p")
            new_datas['content'] = content.get_text(separator = '\n')

        new_datas['title'] = title.get_text()
        return new_datas

    # 解析起点推荐榜单
    def parser_rank(self, url, content):
        if url is None or content is None:
            return None
        soup = BeautifulSoup(content, 'html.parser')
        datas = []

        lis = soup.find("div", id = "rank-view-list").find_all("li")
        for li in lis:
            book = {}
            book['name'] = li.find("h4").find("a").get_text()
            book['url'] = urlparse.urljoin(url, li.find("h4").find("a")['href'])
            book['writer'] = li.find("p", class_ = "author").find("a", class_ = "name").get_text()
            book['tag'] = li.find("p", class_ = "author").find("em").find_next_sibling("a").get_text()
            book['update'] = li.find("p", class_ = "update").find("a").get_text()
            datas.append(book)
        return datas