n = float(input('Enter number 1: '))
m = float(input('Enter number 2: '))
product = n*m
print('*'*50)
print('The product of 2 numbers are {}'.format(product))
print('*'*25+'  OR  '+'*'*25)
print('The product of {} and {} is {}'.format(n,m,product))
print('*'*25+'  OR  '+'*'*25)
print(f'The product of {n} and {m} is {product}')
print('*'*25+'  OR  '+'*'*25)
print('The product of %0.2f and %0.2f is %0.2f' %(n,m,product))
print('*'*50)

