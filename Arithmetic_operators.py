inp1 = float(input('Enter input1: '))
inp2 = float(input('Enter input2: '))
print('='*50)
print('{} + {} = {}'.format(inp1,inp2,inp1+inp2))
print('{} - {} = {}'.format(inp1,inp2,inp1-inp2))
print(f'{inp1} * {inp2} = {inp1*inp2}')
print(f'{inp1} / {inp2} = {inp1/inp2}')
print('%0.1f // %0.1f = %0.1f' %(inp1,inp2,inp1//inp2))
print(f'{inp1} % {inp2} = {inp1%inp2}')
print('{} power {} is {}'.format(inp1,inp2,inp1**inp2))
print('='*50)