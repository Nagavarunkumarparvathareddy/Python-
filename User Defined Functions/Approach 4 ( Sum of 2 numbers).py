print('''
Approach 4: Inputs Values in Function head : NO
            Returns Values in              : YES
**************************************************************************     
Input   : Function def 
Process : Function def = fun heading + fun body
Output  : Function call
''')
def sumofnum():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    res = num1+num2
    return res
result = sumofnum()
print(result)
