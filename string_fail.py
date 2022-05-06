fs = []
ls = []
rs = 0
rs2 = 0

def exx(x):
    count = 0
    while x != 0:
        if  count == 0:
            temp = x%10
            ls.append(temp)
            x = x//10
            count = 1
        elif count == 1:
            while x != 0:
                if x//10 == 0:
                    fs.append(x)
                x=x//10

user = int(input("please enter an integer: "))
if user <= 1:
    print("invalid")
else:
    for i in range(user):
        x = int(input("enter how many ex you had: "))
        exx(x)

for k in range(len(fs)):
    rs = rs + fs[k]
for l in range(len(ls)):
    rs2 = rs2 + ls[l]
print(rs)
print(rs2)

print(fs, ls)
