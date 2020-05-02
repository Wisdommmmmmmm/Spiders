import requests
import re
#爬小说
#统一资源定位符
url = "http://www.xbiquge.la/15/15714/"
#回应
response = requests.get(url)
#编码方式
response.encoding = "utf-8"
#网页源码
html = response.text
#正则表达式匹配
title = re.findall(r'booktitle = "(.*?)"', html)[0]
div = re.findall(r'<div id="list">.*?</div>', html, re.S)[0]
chapter_list = re.findall(r"href='(.*?)' >(.*?)</a>", div)
#写入文件
fb = open('%s.txt'%title, 'w', encoding = "utf-8")
for chapter in chapter_list:
    chapter_url, chapter_title = chapter
    chapter_url = 'http://www.xbiquge.la%s'%chapter_url
    chapter_title = chapter_title+'\n'
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = "utf-8"
    chapter_html = chapter_response.text
    #提取章节内容
    chapter_content = re.findall(r'content(.*?)href', chapter_html, re.S)
    if chapter_content:
        #数据清洗
        content = chapter_content[0]
        content = content.replace(' ', '')
        content = content.replace('&nbsp;', ' ')
        content = content.replace('<br \>', '')
        content = content.replace('<p>', '')
        content = content.replace('<br/>', '\n')
        content = content.replace('\n\r\n', '\n')
        fb.write(chapter_title)
        fb.write(content)
        print(chapter_title)
    else:
        break
