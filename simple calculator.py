import calculatormodule
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Remainder \n 6.Integer division")
choice=int(input("\n Enter your choice :"))
if choice==1:
    print("The sum is :",calculatormodule.add(a,b))
elif choice==2:
    print("The Difference is :",calculatormodule.difference(a,b))
elif choice==3:
    print("The Product is :",calculatormodule.product(a,b))
elif choice==4:
    print("The Division is :",calculatormodule.division(a,b))
elif choice==5:
    print("The Remainder is :",calculatormodule.remainder(a,b))
elif choice==6:
    print("The Integer Difference is :",calculatormodule.integerdivision(a,b))
