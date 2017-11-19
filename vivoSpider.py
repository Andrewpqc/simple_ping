#coding:utf-8
import urllib.request
import json
import re
from lxml import etree
from app import db
from app.models import Requirement,PingInfo


def vivocrawl(url,category,pingType):
	page = urllib.request.urlopen(url).read()
	Selector = etree.HTML(page)
	alist = Selector.xpath("//div[@class='data-jobs']//tr/td[@class='name first']/a/@href")[:10]
	linklist = ["http://hr.vivo.com.cn"+str(a) for a in alist]
	for l in linklist:
		lpage = urllib.request.urlopen(l).read()
		lSelector = etree.HTML(lpage)
		company = 4
		jobTitle = lSelector.xpath("//div[@class='des-title']/h2/span/text()")[0]
		time = lSelector.xpath("//div[@class='des-info']/span[@class='hr-----ico time']/text()")[0].split("：")[1]
		location = lSelector.xpath("//div[@class='des-info']/span[@class='hr-----ico add']/text()")[0].split("：")[1]
		ping = PingInfo(company=company,category=category,jobTitle=jobTitle,
						pingType=pingType,time=time,location=location,link=l)
		db.session.add(ping)
		db.session.commit()
		requirements = lSelector.xpath("//div[@class='hr-details-posdes']/dl[@class='cl'][2]/dd/text()")
		relist=[]
		for r in requirements:
			r = r.strip()
			if r!='':
				relist.append(r)
		for re in relist:
			requirement = Requirement(text=re,pinginfo_id=ping.id)
			db.session.add(requirement)
			db.session.commit()

