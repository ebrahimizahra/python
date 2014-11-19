__author__ = 'vafa'
import sys
def robat(list):
  x=0
  y=0
  list3=[]
  for i in range(len(list)):
      if list[i] =="R":
          x=x+1
      elif list[i]=="L" :
          x=x-1
      elif list[i]=="U":
          y=y+1
      elif list[i]=="B":
          y=y-1
      list2=(x,y)
      list3.append(list2)
  return list3










def main():

  list= ['R','U','U','L','L','L','D','D','D','R','R']
  print robat(list)


if __name__ == '__main__':
    main()


