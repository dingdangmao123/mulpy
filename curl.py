from mul import *
from PIL import Image as im
import time
import re
import requests


@mul.addFunc('sub')
def pil(img,lq,i):
  print str(i)+" start"
  start=time.time()
  index=0
  while True:
    s=img.get()
    if s=='quit':
      break
    try:
      
      r=requests.get(s,headers={"User-Agent":"linux/firefox"})
      f=open(str(i)+'-'+str(time.time()).replace('.','-')+"."+s.split('.')[-1],"wb+")
      f.write(r.content)
      f.close()


      index=index+1
    except Exception,e:
      print e
      lq.put(e)


  print "i "+str(index)+" time: "+str(time.time()-start)+" s"


@mul.addFunc('main')
def getImg(mq,lq):
  r=requests.get("https://www.zhihu.com/question/21100397",headers={"User-Agent":"linux/firefox"})
  p=re.compile(r'(https://[^\s]*\.(jpg|jpeg|png))',re.I)
  img=p.findall(r.text)
  for v in img:
    mq.put(v[0])
  '''
  p=re.compile(r'.*\.(jpg|jpeg|png)',re.I)
	for v in os.listdir(os.getcwd()):
		
		if p.match(v)!=None:
			mq.put(v)
			print v
  '''


mul.run(4)


