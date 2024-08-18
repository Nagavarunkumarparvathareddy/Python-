print('='*50)
print(''' program to swap 2 numbers 
1.Multiline Assignment - any type of data (Integer,float,string)
    ---> a,b = b,a 
2.Arithmetic Operator        
    2.1 Plus(+) and minus(-) -- only for Integer  and data Float
          a = a+b
          a = a-b
          b = a-b
    2.2 Multiplication(*) and integral division operators(//) -- only for Integer data not applicable for float for float use (/)
          a = a*b
          b = a//b
          a = a//b
3.Swapping using third variable -- any type of data (Integer,float,string)
    k = a
    a = b
    b = k
4.Using Bitwise Operators - only for Integer data
   a = a^b
   b = a^b
   a = a^b
''')
print('='*50)
print('\t\t Logic - 1')
a,b = int(input('Enter input1 :')),int(input('Enter input2: '))
print(f'\t\t\t before swapping a = {a},b = {b}')
a,b =b,a
print(f'\t\t\t After swapping a = {a},b = {b}')
print('='*50)

print('\t\t Logic - 2')
a,b = int(input('Enter input1 :')),int(input('Enter input2: '))
print(f'\t\t\t before swapping a = {a},b = {b}')
k = a
a = b
b = k
print(f'\t\t\t After swapping a = {a},b = {b}')
print('='*50)

print('\t\t Logic - 3')
a,b = int(input('Enter input1 :')),int(input('Enter input2: '))
print(f'\t\t\t before swapping a = {a},b = {b}')
a = a+b
b = a-b
a = a-b
print(f'\t\t\t After swapping a = {a},b = {b}')
print('='*50)

print('\t\t Logic - 4')
a,b = int(input('Enter input1 :')),int(input('Enter input2: '))
print(f'\t\t\t before swapping a = {a},b = {b}')
a = a * b
b = a // b
a = a // b
print(f'\t\t\t After swapping a = {a},b = {b}')
print('='*50)

print('\t\t Logic - 5')
a,b = int(input('Enter input1 :')),int(input('Enter input2: '))
print(f'\t\t\t before swapping a = {a},b = {b}')
a = a ^ b
b = a ^ b
a = a ^ b
print(f'\t\t\t After swapping a = {a},b = {b}')
print('='*50)









