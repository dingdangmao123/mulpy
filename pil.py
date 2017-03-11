from mul import *
from PIL import Image as im
import time
import re


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
      
      p=im.open(s)

      p.thumbnail((p.size[0]/2,p.size[1]/2))
      p.save(s)
      index=index+1
    except Exception,e:
      print e
      lq.put(e)


  print str(i)+" "+str(index)+" time: "+str(time.time()-start)+" s"


@mul.addFunc('main')
def getImg(mq,lq):
	p=re.compile(r'.*\.(jpg|jpeg|png)',re.I)
	for v in os.listdir(os.getcwd()):
		
		if p.match(v)!=None:
			mq.put(v)
			print v



mul.run(4)


