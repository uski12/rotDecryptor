#shift your sentences by a factor

word = input("Enter: ")
word = word.upper()

def rotate(char, rotFactor=1):
    rotatedInt = (ord(char)-64 + rotFactor)
    #if rotatedInt%26==0:
    #    return chr(90)
    #return chr((rotatedInt%26)+64)

    #smart ass version of the above code
    return chr(rotatedInt%26 + ((int((rotatedInt%27)/26))*26) +64)

list = []
for i in range(1,26):
    rotated = ""
    for j in range(len(word)):
        rotated += rotate(word[j], i)
    rotated = str(i) + ": " + rotated
    list.append(rotated)

for i in list:
    print(i)
