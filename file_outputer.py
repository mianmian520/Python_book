# -*- coding:utf-8 -*-
import os

class Outputer(object):
    def __init__(self):
        self.datas = []

    # 把章节内容添加到datas中
    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    # 把datas中内容一起写入文件
    def outputer_file(self, title):
        path = "book/%s" % title
        if os.path.exists(path) is False:
            os.makedirs(path)
        book_path = "book/%s.txt" % title
        f = open(book_path, 'w')
        for data in self.datas:
            # chapter_path = "%s/%s.txt" % (path, data['title'])
            # # print chapter_path
            # file = open(chapter_path, "w")
            # file.write("\t%s\n" % data['title'].encode('utf-8'))
            # file.write(data['content'].encode('utf-8'))
            # file.close()
            f.write("\n\t%s\n" % data['title'].encode('utf-8'))
            f.write(data['content'].encode('utf-8'))
        f.close()

    # 把章节题目和内容写入小说文本
    def outputer(self, title, data):
        path = "book"
        if os.path.exists(path) is False:
            os.makedirs(path)
        book_path = "book/%s.txt" % title
        f = open(book_path, 'a')
        f.write("\n\t%s\n" % data['title'].encode('utf-8'))
        f.write(data['content'].encode('utf-8'))
        f.close()