
print("*******Welcome to my Calculator App*******")

print("\nPlease select option from calculator:")
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Exponential")
print("5.Division")
print("6.Modulus")
print("7.Floor division\n")
select=int(input("select option:"))

number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))

if select==1:
  print(number_1,"+",number_2,"=",int(number_1)+int(number_2))


elif select==2:
  print(number_1,"-",number_2,"=",int(number_1)-int(number_2))
  
elif select==3:
    print(number_1,"*",number_2,"=",int(number_1)*int(number_2))

elif select==4:
    print(number_1,"**",number_2,"=",int(number_1)**int(number_2))

elif select==5:
    print(number_1,"/",number_2,"=",int(number_1)/int(number_2))

elif select==6:
    print(number_1,"%",number_2,"=",int(number_1)%int(number_2))

elif select==7:
    print(number_1,"//",number_2,"=",int(number_1)//int(number_2))

else:
  print("Invalid option")





  
  
