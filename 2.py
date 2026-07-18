num = int(input("Enter a number: "))

temp = num
total = 0
totaldigits = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + digit ** totaldigits
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")