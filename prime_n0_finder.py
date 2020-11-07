num =int(input("enter any number :"))
for i in range (2,num):
    if num % i==0:
        print('not a prime number')
        break
else:
    print('prime')