import math
n = int(input('Enter a Number: '))
s = str(n)
l = len(s)
fact_sum = 0
for i in range(l):
    fact_sum += math.factorial(int(s[i]))
if fact_sum == n:
    print('Strong Number')
else:
    print('Not a strong Number')
