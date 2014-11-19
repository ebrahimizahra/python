__author__ = 'esy'
def mabna (n):


       s = n/16
       n=n%16

       k=s/16
       while(s>16):

         s=s%16


       return k ,s ,n







print mabna(200)
