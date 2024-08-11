print('*'*50)
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = (a+b)**2
print('*'*150)
print(f'\t\t logic - 1: (a+b)x2 --->({a}+{b})x2 = {c}')
print(f'\t\t logic - 2: (a+b)x(a+b) --->({a}+{b})x({a}+{b}) = {c}')
print(f'\t\t logic - 3: (a*a)+(2*a*b)+(b*b) --->({a}*{a})+(2*{a}*{b})+({b}*{b}) = {c}')
print(f'\t\t logic - 4: (a**2)+(2*a*b)+(b**2) --->({a}**2)+(2*{a}*{b})+({b}**2) = {c}')
print('*'*150)

