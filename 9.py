def div(a,b):
    try :
        return a/b
    except ZeroDivisionError:
        print("除零错误")
print(div(10,2))
div(10,0)