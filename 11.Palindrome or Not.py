print('='*150)
print("\t\t 10. Write a Python Program to check given number is palindrome or Not ?")
print('='*150)
n = int(input("Enter the Number: "))
s = str(n)
print('='*150)
output = int(s[::-1])
if n == s:
    print(f"\t\t\t\t Entered Number : {n} ")
    print(f"\t\t\t\t Output Number : {output}")
    print("\t\t\t\t Both are same.Hence Given number is a Palindrome Number")
else:
    print(f"\t\t\t\t Entered Number :  {n} ")
    print(f"\t\t\t\t Output Number : {output}")
    print("\t\t\t\t Both are not same.Hence Given number is not a Palindrome Number")
print('='*150)


