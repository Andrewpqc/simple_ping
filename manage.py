import os
from app import create_app,db
from flask_script import Manager,Shell
from app.models import Requirement,PingInfo
from flask_migrate import Migrate,MigrateCommand
app=create_app("default")
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    """自动加载环境"""
    return dict(app=app,db=db,Requirement=Requirement,PingInfo=PingInfo)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

@manager.command
def command_360():
    from urllib import request
    import random
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    # 用户代理池
    ua=UserAgent()
    # ip池
    ipPool=ips=["112.93.208.47:8080","27.40.144.34:61234"]
    company=3
    #获取包含数据的html页面
    proxy=request.ProxyHandler({'http':random.choice(ips)})
    url="http://campus.360.cn/2015/grad.html"#包含所需数据的url
    opener=request.build_opener(proxy,request.ProxyHandler)
    opener.addheaders = [('User-Agent', ua.random)]
    data=opener.open(url).read().decode()
    #解析数据
    soup=BeautifulSoup(data,"html.parser")

    ################################技术模块###################################
    techJobs = soup.find_all("li", attrs={"class": "sub"}, recursive=True)
    category = 1
    for index, job in enumerate(techJobs):
        tech_jobname = job.find('div', attrs={"class": "job-name"},
                                recursive=True).span.get_text().strip()
        pingType = index % 2
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        pingobj=PingInfo(company=company,
                         category=category,
                         jobTitle=tech_jobname,
                         pingType=pingType,
                         location=location,
                         link=link
                         )
        db.session.add(pingobj)
        db.session.commit()

        for requirement in requirements:
            real_req = requirement.get_text().strip()
            requiobj=Requirement(text=real_req,pinginfo=pingobj)
            db.session.add(requiobj)
            db.session.commit()


    ##########################产品模块###########################3
    ##recursive=True/False指定的是是否爬取他字节点的下面的节点
    productJobs = soup.find("li", attrs={"class": "job-pm"},
                                recursive=True).find('ul',attrs={"class":"job-list"},
                                recursive=True).find_all("li",attrs={},recursive=False)
    for index,job in enumerate(productJobs):
        category=2
        pingType = index % 2
        product_jobname=job.find('div',attrs={"class":"job-name"},
                                 recursive=True).span.get_text().strip()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        pingobj = PingInfo(company=company,
                           category=category,
                           jobTitle=product_jobname,
                           pingType=pingType,
                           location=location,
                           link=link
                           )
        db.session.add(pingobj)
        db.session.commit()

        for requirement in requirements:
            real_req = requirement.get_text().strip()
            requiobj = Requirement(text=real_req, pinginfo=pingobj)
            db.session.add(requiobj)
            db.session.commit()

    ##########################设计模块###########################3
    designJobs = soup.find("li", attrs={"class": "job-ue"},
                            recursive=True).find('ul', attrs={"class": "job-list"},
                                                 recursive=True).find_all("li", attrs={}, recursive=False)
    for index, job in enumerate(designJobs):
        category=3
        pingType = index % 2
        design_jobname = job.find('div', attrs={"class": "job-name"},
                                   recursive=True).span.get_text().strip()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        pingobj = PingInfo(company=company,
                           category=category,
                           jobTitle=design_jobname,
                           pingType=pingType,
                           location=location,
                           link=link
                           )
        db.session.add(pingobj)
        db.session.commit()

        for requirement in requirements:
            real_req = requirement.get_text().strip()
            requiobj = Requirement(text=real_req, pinginfo=pingobj)
            db.session.add(requiobj)
            db.session.commit()

    ##########################市场模块###########################3
    marketJobs = soup.find("li", attrs={"class": "job-ue"},
                           recursive=True).find('ul', attrs={"class": "job-list"},
                                                recursive=True).find_all("li", attrs={},
                                                                         recursive=False)
    for index, job in enumerate(marketJobs):
        category = 3
        pingType = index % 2
        market_jobname = job.find('div', attrs={"class": "job-name"}, recursive=True).span.get_text()
        location = job.find("div", attrs={"class": "job-msg"},
                            recursive=True).find("div", attrs={"class": "place"}).find("span", attrs={
            "class": "value"}).get_text()
        link = job.find("div", attrs={"class": "apply-btn"}, recursive=True).a["href"]
        requirements = job.find("div", attrs={"class": "job-req"},
                                recursive=True).ul.find_all("li")
        pingobj = PingInfo(company=company,
                           category=category,
                           jobTitle=market_jobname,
                           pingType=pingType,
                           location=location,
                           link=link
                           )
        db.session.add(pingobj)
        db.session.commit()
        for requirement in requirements:
            real_req = requirement.get_text().strip()
            requiobj = Requirement(text=real_req, pinginfo=pingobj)
            db.session.add(requiobj)
            db.session.commit()
    print("done")



@manager.command
def command_baidu():
    pass

@manager.command
def command_alibaba():
    pass

if __name__ == '__main__' :
    manager.run()




