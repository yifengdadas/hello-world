input_string = input("请输入字符串：")
print(type(input_string))
if input_string.isdigit():
    print("输入的是数字")
elif input_string.isalpha():
    print("输入的是字母")
else:
    print("输入的是其他字符")