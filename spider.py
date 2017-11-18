"""爬取360"""
company=3

from app import db
from lxml import etree
from urllib import request
import random
import json
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import mysql.connector
from pprint import pprint


# ua=UserAgent()
# #ip池
# ips=["112.93.208.47:8080","27.40.144.34:61234"]
# proxy=request.ProxyHandler({'http':random.choice(ips)})
# url="http://campus.360.cn/2015/grad.html"
# opener=request.build_opener(proxy,request.ProxyHandler)
# opener.addheaders = [('User-Agent', ua.random)]
# data=opener.open(url).read().decode()
with open('a.html','r') as f:
    data=f.read()
    soup = BeautifulSoup(data, 'html.parser')

    #########################技术模块####################################
    techJobs = soup.find_all("li", attrs={"class": "sub"}, recursive=True)
    #技术
    category=1

    #jobTitle

    for index,job in enumerate(techJobs):
        tech_jobname=job.find('div',attrs={"class":"job-name"},recursive=True).span.get_text()
        pingType=index%2
        # time
        location=job.find("div",attrs={"class":"job-msg"},
                recursive=True).find("div",attrs={"class":"place"}).find("span",attrs={"class":"value"}).get_text()

        link=job.find("div",attrs={"class":"apply-btn"},recursive=True).a["href"]
        requirements=job.find("div",attrs={"class":"job-req"},
                              recursive=True).ul.find_all("li")
        for requirement in requirements:
            real_req=requirement.get_text().strip()


    ##########################产品模块###########################3
    ##recursive=True/False指定的是是否爬取他字节点的下面的节点
    productJobs = soup.find("li", attrs={"class": "job-pm"},
                                recursive=True).find('ul',attrs={"class":"job-list"},
                                recursive=True).find_all("li",attrs={},recursive=False)
    for index,job in enumerate(productJobs):
        category=2
        pingType = index % 2
        product_jobname=job.find('div',attrs={"class":"job-name"},recursive=True).span.get_text()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        for requirement in requirements:
            real_req = requirement.get_text().strip()





    ##########################设计模块###########################3
    designJobs = soup.find("li", attrs={"class": "job-ue"},
                            recursive=True).find('ul', attrs={"class": "job-list"},
                                                 recursive=True).find_all("li", attrs={}, recursive=False)
    for index, job in enumerate(designJobs):
        category=3
        pingType = index % 2
        product_jobname = job.find('div', attrs={"class": "job-name"}, recursive=True).span.get_text()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        for requirement in requirements:
            real_req = requirement.get_text().strip()
            # print(real_req)

    ##########################市场模块###########################3
    marketJobs = soup.find("li", attrs={"class": "job-ue"},
                           recursive=True).find('ul', attrs={"class": "job-list"},
                                                recursive=True).find_all("li", attrs={}, recursive=False)
    for index, job in enumerate(marketJobs):
        category = 3
        pingType = index % 2
        product_jobname = job.find('div', attrs={"class": "job-name"}, recursive=True).span.get_text()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        for requirement in requirements:
            real_req = requirement.get_text().strip()
            print(real_req)
# cursor = conn.cursor()
# print("游标建立")
# count=0
# for movieid in movieIds:
#     for i in range(0,101,20):
#         proxy=request.ProxyHandler({'http':random.choice(ips)})
#         url="https://movie.douban.com/subject/"+str(movieid)+"/comments?start="+str(i)+"&limit=20&sort=new_score&status=P"
#         opener=request.build_opener(proxy,request.ProxyHandler)
#         opener.addheaders=[('User-Agent',ua.random)]
#         print(">>>>>>>>>>>>>>>>>.")
#         data=opener.open(url).read().decode()
#         print("<<<<<<<<<<<<<<<<<<<<<")
#         print(data[8:90])
#         #匹配并且存入数据库
#         soup = BeautifulSoup(data, 'html.parser')
#         results = soup.find_all("p", attrs={"class": ""}, recursive=True)
#         for index, vaule in enumerate(results[0:-6]):
#             content=vaule.get_text().strip()
#             print(content)
#             try:
#                 cursor.execute("insert into allcomment (content,movieid) values('%s',%d)" % ( content,int(movieid)))
#             except mysql.connector.errors.DatabaseError:
#                 time.sleep(3)
#             time.sleep(0.2)
#             print(count)
#             count+=1
# # cursor.commit()
# # conn.close()
# conn.commit()
# cursor.close()
# import mysql.connector
# conn = mysql.connector.connect(user='root', password='pqc19960320',
#                                        database='Hackerthon', host="120.77.220.239", port=32777)
#     #游标
# cursor = conn.cursor()
# cursor.execute("insert into allcomment (content,movieid) values('%s',%d)" % ("哈哈", int(1)))
# conn.commit()
# cursor.close()

#
# from urllib import request
# import random
# import json
# import time
# from urllib import error
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import mysql.connector
# #User_Agent池
# ua=UserAgent()