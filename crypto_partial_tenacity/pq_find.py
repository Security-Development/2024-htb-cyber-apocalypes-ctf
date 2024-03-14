#p = 524287 
#q = 131071
#n = p*q # 68718821377
#p = 524287
#q = 131071

from sympy import symbols, Eq, solve

def solve(prob,answer, l):
    ret = 0
    a = 0
    print(f"l={l}")
    for i in range(100):
        a = eval(prob.replace("x", str(i))) + l

        if (a % 10) == int(answer, 10):
            ret = i
            break

    return ret, a
# 홀수
p = list("x2x2x7")[::-1]
# 짝수
q = list("1x1x7x")[::-1]
n = list("68718821377"[::-1])

cycle_count = len(q)
ip = 1
dp = []
for i in range(cycle_count):
    table = []
    prob = ""

    e = 0
    for j in range(i + 1):
        pp = p[i-j]
        qq = q[j]
        prob += f"{pp}*{qq}"
        
        if pp == "x":
            e = 1
        elif qq == "x":
            e = 2


        if j != i:
            prob += "+"

        if j == i:
            l = 0
            if len(dp) > 0:
                l = int(''.join(dp[j-1][:-1]), 10)
            k, g = solve(prob, n[j], l)
            if e == 1:
                p[i] = str(k)
            elif e == 2:
                q[j] = str(k)

            gg = (g % 10) + l

            dp.append(list(str(g).zfill(2)))
            print(f"p={''.join(p[::-1])}")
            print(f"q={''.join(q[::-1])}")
    prob = ""
     
    print("= "* 12)