n = int(input('Enter a Number : '))
s = str(n)
l = len(s)
arm_sum = 0
for i in range(l):
    arm_sum += int(s[i])**l
if arm_sum == n:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')