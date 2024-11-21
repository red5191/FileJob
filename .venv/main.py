file = open('data.txt', 'r')
content = file.read()
print(content)

file = open('data.txt', 'a')
file.write('\n\n123456')

file = open('data.txt', 'r')
content2 = file.readlines()
print(content2)

file = open('data.txt', 'rb')
copying = file.read()

file = open('data2.txt', "wb")
file.write(copying)
