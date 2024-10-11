yearsNumber=int(input("请输入年份："))
if yearsNumber%4==0 and yearsNumber%100!=0:
    print("你输入的年份{}是闰年".format(yearsNumber))