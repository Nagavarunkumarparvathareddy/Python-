a = input('Enter any character in between A to Z: ').lower()
if len(a) != 1 or not(a >='a' and a <='z'):
    print('Please Enter valid Input')
else:
    result = 'Vowel' if a == 'a' or a == 'e' or a == 'i' or a =='o' or a =='u' else 'Consonant'
    print(result)