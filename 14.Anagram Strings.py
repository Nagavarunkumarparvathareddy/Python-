str1 = input('Enter String 1 :').lower()
l1 = len(str1)
str2 = input('Enter String 2 :').lower()
l2 = len(str2)
result = 0
if l1 != l2:
    print('Both Strings are not anagrams')
else:
    lst1 = list(str1)
    lst2 = list(str2)
    for ele in lst1:
        if ele  not in lst2:
            result = 0
        else:
            result = 1
    if result == 0:
        print('Both Strings are not anagrams')
    else:
        print('Both Strings are  anagrams')
