import multiprocessing as mp
import time
import os
import sys


class prohibit(Exception):
  def __init__(self,msg):
    self.msg=msg
  def __str__(self):
    print self.msg


def log(lq):
  if os.path.exists("mul.log"):
    os.remove("mul.log")
  fp=open("mul.log","w+")

  while True:
    msg=lq.get()
    print msg
    try:
      fp.write(str(msg)+"\r\n")
      fp.flush()
    except IOError,e:
      print '************'
      print e
      print '************'

class tip:
  __word={"-h":'',"-d":''}
  @staticmethod
  def parse():
    if len(sys.argv)>1:
      if sys.argv[1] not in tip.__word.keys():
        print "argv is invalid"
        sys.exit(0)
        
      tip.__word['-h']=tip.help
      tip.__word['-d']=tip.cd


      tip.__word[sys.argv[1]]()

  @staticmethod
  def help():

    print '-h: help'
    print '-d: change work dir'

    sys.exit(0)

  @staticmethod
  def cd():
    if len(sys.argv)<3 or not os.path.exists(sys.argv[2]):
      print 'dir argv error'
      sys.exit(0)

    os.chdir(sys.argv[2])


class mul:

  __num=0
  __dict={'log':log}
  __flag=0
  __word=['sub','main','log']


  def __init__(self):
    raise prohibit("prohibit building mul object!")


  @staticmethod
  def __setNum(num):
    if type(num)!=type(1) or num<=0:
      raise TypeError()
    mul.__num=num

  @staticmethod
  def addFunc(arg):
    
    if arg not in mul.__word:
      raise prohibit("method name it invalid")

    def func(f):
      
      mul.__dict[arg]=f
      return f
    return func

  @staticmethod
  def setMain(f):
    mul.__dict['main']=f

  @staticmethod
  def setSub(f):
    #print type(f)
    mul.__dict['sub']=f
    #print type(mul.__dict['sub'])

  @staticmethod
  def __before(num):
    tip.parse()
    mul.__setNum(num)

  @staticmethod
  def run(num):
    
    mul.__before(num)


    if mul.__flag==1:
      raise prohibit("process has started!")

    mul.__flag=1

    result = []

    mq=mp.Queue()
    lq=mp.Queue()
    
    for i in range(mul.__num):
      msg = "process %d start" %(i)
      result.append(mp.Process(target=mul.__dict['sub'],args=(mq,lq,i)))


    logp=mp.Process(target=mul.__dict['log'],args=(lq,))
    

    for v in result:
      v.start()

    logp.start()
    
   
    mul.__dict['main'](mq,lq)

    for v in range(mul.__num):
      mq.put('quit')

    for v in result:
        v.join()

    print "work process done."

    logp.terminate()

    print "log process done."

 
    