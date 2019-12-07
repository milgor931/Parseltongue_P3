text = "(whats going on()?)"

newStr = ""
index = 1
for i in text:
    if index%2 == 0 and i !=" " and i != "(" and i != ")":
        i = chr(ord(i) - 32)
    newStr = newStr + i
    index += 1
print(newStr)

for i in newStr:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        newStr = newStr.replace(i, '*')

def check_parentheses(text):
    leftP = 0
    rightP = 0
    for i in text:
        if i == "(" :
            leftP += 1
        if i == ")" :
            rightP += 1
    if leftP == rightP:
        return True
    else:
        return False

print("()()()()(((a)b)b)b")
print("Balanced? " + str(check_parentheses("()()()()(((a)b)b)b")))
print("((Th*s Do*sN't MaTcH)")
print("Balanced? " + str(check_parentheses("((Th*s Do*sN't MaTcH)")))
print(newStr)