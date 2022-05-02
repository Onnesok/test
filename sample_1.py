def cal(user):
    rs = 0
    for i in range(1, user+1):
        if i%2 == 0:
            temp = int(i) * "3"
            rs += int(temp)
        else:
            temp = int(i) * "1"
            rs += int(temp)
    return rs

def reverse(user):
    ls = []
    for i in range(len(user)-1, -1, -1):
        ls.append(int(user[i]))
    print(ls)

if __name__ == '__main__':
    user = int(input("please enter an input: "))
    string = str(cal(user))
    print(f"sum of series = {int(string)}")
    reverse(string)

