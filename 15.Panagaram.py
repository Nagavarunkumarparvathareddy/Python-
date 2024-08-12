n = input('Enter your word: ').lower()
l = len(n)
count = 0
if l < 26:
    print('Not a panagaram')
else:
    lst = list(n)
    for ele in lst:
        if ele >= 'a' and ele <= 'z':
            count += 1
    if count < 26:
        print('Not a panagaram')
    else:
        print('panagaram')

