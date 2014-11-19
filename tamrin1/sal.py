def sal(x):
    list=["f","o","kh","t","m","sh","me","ab","aZ","D","B","E"]
    a=x/31
    b=x%31
    if b>30:
        c=b/30
        b=b%30
        a=a+c
    else:
        c=a

    return (str(b)+list[c-1])





if __name__ == '__main__':
    x=100
    print sal(x)