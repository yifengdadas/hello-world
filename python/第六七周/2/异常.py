try:
    a = 10/0
except ZeroDivisionError:
    print('除零错误')
else:
    print('没有错误结果为',a)
finally:
    print('有无错误都会执行')
    
        
    