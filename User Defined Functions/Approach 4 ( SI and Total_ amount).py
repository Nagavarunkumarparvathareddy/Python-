print('''
Approach 4: Inputs Values in Function head : NO
            Returns Values in              : YES
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def rect():
    p = float(input('Enter Principle amount: '))
    t = float(input('Enter time in years: '))
    r = float(input('Enter rate of Interest: '))
    simple_int = p * t * r / 100
    amount = simple_int + p
    return simple_int,amount
result = rect()
print(f'simple_int : {result[0]}')
print(f'amount : {result[1]}')
