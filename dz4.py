#№3
# num1 = int(input("enter your fitst num -->"))
# num2 = int(input("enter your second num -->"))
# for i in range(num1, num2, 1):
#     if i % 7 == 0:
#         print(i)

num1 = int(input("enter your fitst num -->"))
num2 = int(input("enter your second num -->"))
print ("1:")
for i in range(num1, num2, 1):
     print (i)
print ("2:")
for i in range(num2, num1, -1):
     print (i)
print ("3:")
for i in range(num1, num2, 1):
     if i % 7 == 0:
         print(i)

