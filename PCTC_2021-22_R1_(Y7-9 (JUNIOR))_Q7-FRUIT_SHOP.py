n1 = input()
n2 = input()
if len(n1) == 1:
    p1 = '0' + n1
else:
    p1 = n1
if len(n2) == 1:
    p2 = '0' + n2
else:
    p2 = n2

s1 = n1+'.'+p2
s2 = n2+'.'+p1
if float(s1) < float(s2):
    if float(s1) <= 20:
        print('£'+str(s1))
    if float(s2) <= 20 and s1 != s2:
        print('£'+str(s2))
else:
    if float(s2) <= 20:
        print('£'+str(s2))
    if float(s1) <= 20 and s2 != s1:
        print('£'+str(s1))