file = open('Gitpulltest')

# print(file.read(36))

# print(file.readline())
# print(file.readline())


# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()
