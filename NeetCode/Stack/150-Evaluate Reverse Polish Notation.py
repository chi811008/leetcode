tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
num = list()
for e in tokens:
    if e.startswith("-") and e[1:].isdigit():
        num.append(int(e))
    elif e.isdigit():
        num.append(int(e))
    else:
        a = num.pop()
        b = num.pop()
        if e == "+":
            tmp_ans = b + a
        elif e == "-":
            tmp_ans = b - a
        elif e == "*":
            tmp_ans = b * a
        elif e == "/":
            tmp_ans = int(b / a)
        num.append(tmp_ans)
print(num[0])