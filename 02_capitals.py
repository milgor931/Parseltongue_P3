d = {}
f = open("capitols.txt", 'r')
for line in f:
    key, val = line.strip().split(',')
    d[key] = val
print(d)
user = input("Ready: ")
while user != "Done":
    for key in d.keys():
        if user == key:
            print(d[key])
        if user == d[key]:
            print(key)
    user = input("Ready: ")

