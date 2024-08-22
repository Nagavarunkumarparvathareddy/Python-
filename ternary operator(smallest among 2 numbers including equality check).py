a1 = float(input('Enter input1: '))
a2 = float(input('Enter input2 :'))
result = a1 if a1<a2 else a2 if a2>a1 else "Both numbers are equal"
print(f'Small({a1},{a2}) = {result}')