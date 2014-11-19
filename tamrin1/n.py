__author__ = 'esy'

def mabna (n):
   x=[]

   while(n>0):
     x.append(n%16)
     n=(n/16)
     return(n)
     x.reverse()
   return x





if __name__ == '__main__':
     print mabna(200)