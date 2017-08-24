# coding:utf-8
import requests

# html下载器
class HtmlDowmloader(object):

    # 根据url获取数据
    def download(self, url, type):
        if url is None:
            return None
        response = requests.get(url)
        if response.status_code != 200:
            return None
        # 根据不同的网站设置不同的编码
        if type == 'qidian' or type == 'biquge' or type == '17K' or type == 'bxwx':
            response.encoding = 'utf-8'
        elif type == 'xbxwx':
            response.encoding = 'gbk'
        return response.text