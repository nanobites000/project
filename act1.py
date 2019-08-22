opt, num1, num2 = input().split()
#or use num1, num2 = int(num1), int(num2)
if(opt == 'A'):
	print(int(num1) + int(num2))
elif(opt == 'B'):
	print(int(num1) - int(num2))
elif(opt == '%'):
	print(int(num1) % int(num2))
elif(opt == '>'):
	if(int(num1) > int(num2)):
		print("1")
	else:
		print("0")
elif(opt == '<'):
	if(int(num1) < int(num2)):
		print("1")
	else:
		print("0")
else:
	print("Invalid Input")
