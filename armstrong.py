
'''
an armstrong number is a number where the sum of each digit raised to the power
of the number of digits of the original number is equal to the original number

145

1^3
4^3
5^3
=145

5643
5^4
6^4
4^4
3^4
=5643

-find the sum of the total digits powered
-power numbers
-compare final sum to original number
-given a number, find its digits
----------------------------------------------------------------------------------------------------------------
'''
def is_armstrong(number):
	strumber = str(number)
	numberofdigits = len(strumber)
	sum = 0


	for strdigit in strumber:
		digit = int(strdigit)
		sum = sum + (digit**numberofdigits)

	if(sum == int(strumber)):
		return True
	else:
		return False
for x in range(100000000000000000000):
	armstrong = is_armstrong(x)
	if (armstrong == True):
		print(str(x) + "is an armstrong number")
