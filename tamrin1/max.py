__author__ = 'esy'
def maxmin(x):
    char={}

    for i in x:
        if i in char.keys():
            char[i]+=1
        else:
            char[i]=1
    test= sorted(char.items())
    b=test[0]
    n=len(test)
    m=test[n-1]
    return(b,m)
if __name__ == '__main__':
    x="sddfbbb"
    print maxmin(x)


