n = int(input('Enter input : '))
s = str(n)
lst = list(s)
sum_of_digits = 0
for ele in lst:
    sum_of_digits += int(ele)
print(sum_of_digits)