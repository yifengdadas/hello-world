text="姓名 性别 住址 身份证号 手机号 职业 职位 学历 学位"
resesese=text.split()
print(resesese)

dick1={}
dick1["google"]="www.google.com"
print(dick1)
dick1["google"]="www.google.cn"
print(dick1["google"])
del dick1["google"]
print(dick1)
del dick1

yuanzu1=("google","youdun","baidu","bing","360","sohu")
yuanzu2=("youtube",)
yuanzu3=yuanzu1+yuanzu2
del yuanzu1
del yuanzu2

jihe1=set()
jihe1.update(["姓名","性别","住址","身份证号","手机号","职业"])
jihe1.remove("住址")
jihe1.pop()