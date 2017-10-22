'''
用于文件中全文替换字符
fileNae:文件路径与文件名
str1:需要替换的字符
str2:替换后的字符
'''
def str_replace(fileName, str1, str2):
    with open(fileName, 'r') as f:
        s = f.readlines()
    with open(fileName, 'w'):
        pass
    for x in s:
        b = x.replace(str1, str2)
        with open(fileName, 'a') as f:
            f.write(b)
