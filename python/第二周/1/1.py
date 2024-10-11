text="姓名 性别 住址 身份证号 手机号 职业 职位 学历 学位"
result=text.split()
print(result)

dick1={}
dick1["google"]="www.google.com"
print(dick1)
del dick1["google"]
print(dick1)
del dick1

tuple1=('google','youtube','baidu','bing','bilibili')
tuple2=('facebook',)
tuple3=tuple1+tuple2
del tuple1
del tuple2

set1=set()
set1.update(['google','youtube','baidu','bing','bilibili',"yahoo"])
print(set1)
set1.remove("yahoo")
set1.pop()
