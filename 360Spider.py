"""爬取360"""
company=3
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib import request
# from app import db
import random

ua=UserAgent()
#ip池
ips=["112.93.208.47:8080","27.40.144.34:61234"]
proxy=request.ProxyHandler({'http':random.choice(ips)})
url="http://campus.360.cn/2015/grad.html"
opener=request.build_opener(proxy,request.ProxyHandler)
opener.addheaders = [('User-Agent', ua.random)]
data=opener.open(url).read().decode()
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
