user = int(input("please enter an integer: "))

last = []
first = [] 
temp = 999999

if user <= 1:
    print("invalid")

else:
    for i in range(user):
        x = int(input("please enter your ex: "))
        if temp != 9999999:
            temp = x % 10
            first.append(temp)
        user = x // 10
        if x % 10 == 0:
            last.append(user)

