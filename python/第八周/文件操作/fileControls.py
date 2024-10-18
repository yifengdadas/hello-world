import os.path


with open('练习.txt','w',encoding='utf-8')as file:
    file.write('锦瑟\n')
    file.write('锦瑟无端五十弦，一弦一柱思华年。\n')
    file.write('庄生晓梦迷蝴蝶，望帝春心托杜鹃。\n')
    file.write('沧海月明珠有泪,蓝田日暖玉生烟.\n')
    file.write('此情可待成追忆，只是当时已惘然.\n')
file.close()    
with open('练习.txt','r',encoding='utf-8')as file:
    print(file.read(3))
    print(file.read(20))
    print(file.read(37))
    file.seek(0)
    print(file.readline(5))
    print(file.readline(10))
    file.seek(0)
    print(file.readlines())
file.close()    

os.rename('练习.txt','锦瑟.txt')
os.remove('锦瑟.txt')