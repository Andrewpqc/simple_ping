import urllib.request
import json
import re
from app import db
from app.models import Requirement,PingInfo


def crawl(url,category,pingType):
	page=urllib.request.urlopen(url).read()
	jsonpage = json.loads(page.decode('utf-8'))
	postlist = jsonpage["postList"][:10]
	for post in postlist:
		company = 2
		jobTitle=post["name"]
		time=post["publishDate"]
		location=post["workPlace"]
		if pingType == 0:
			link="http://talent.baidu.com/external/baidu/index.html#/jobDetail/12/"+str(post["postId"])
		elif pingType == 1:
			link="http://talent.baidu.com/external/baidu/campus.html#/jobDetail/1/"+str(post["postId"])
		requirements=post["serviceCondition"]
		ping = PingInfo(company=company,category=category,jobTitle=jobTitle,
						pingType=pingType,time=time,location=location,link=link)
		db.session.add(ping)
		db.session.commit()
		alist = requirements.split()
		blist = []
		for a in alist:
			dr = re.compile(r'<[^>]+>',re.S)
			dd = dr.sub('',a)
			dd = dd.strip().strip('-')
			if dd!='':
				blist.append(dd)
		for b in blist:
			r = Requirement(text=b,pinginfo_id=ping.id)
			db.session.add(r)
			db.session.commit()
