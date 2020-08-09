#Sara Margaret Rizzo
#2020-08-08
#This program goes through the numbers 1-50
#It tells you if the number is divisible by 3, 5, or both.

for i in range(1, 51):
    if((i%3==0) & (i%5==0)):
      print("Divisible by three and five")
    elif(i%3==0):
        print("Divisible by three")
    elif(i%5==0):
        print("Divisible by five")
    else:
        print(i)