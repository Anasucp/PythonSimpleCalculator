#function for calculations
def add(x, y):
	return x + y


def subtract(x,y):
	return x - y


def div(x, y):
	return x / y 


def mul(x, y):
	return x * y

 

#menu

print ("1.Add Numbers")
print ("2.Subtract Numbers")
print ("3.Divide Numbers")
print ("4.Multiply Numbers")
print ("5.exit")





while True:
	

	print("|----------------------------|")

	choice = input ("Enter 1/2/3/4/5:")

	if choice in ('1','2','3','4'):
		try:
			num1 = float(input("Enter first number:"))
			num2 = float(input("Enter second number:"))
		except ValueErorr:
			print ("Invalid Choice")
			continue


		if choice == "1":
			print (num1, '+', num2, '=', add(num1, num2))
		elif choice == "2":
			print (num1, '-', num2, '=', subtract(num1, num2))
		elif choice == "3":
			print (num1, '/', num2, '=' , div(num1, num2))
		elif choice == "4":
			print (num1, '*', num2, '=' , mul(num1, num2))
			

		next__calculation = input("Want to do next calculation? (Yes/No):")

		if next__calculation == "no":
			break
	elif choice == "5":
		break
	else:
		print("invalid Choice")
		