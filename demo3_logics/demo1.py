num=10

if num<0:
    print("The number is negative ", num)
elif num==0:
    print("its zero!!")
else:
    print("the number is positive ",num)


page_number=200

#check between 100 & 200

if page_number>=100:
    if page_number<=200:
        print('Yes between 100 & 200')

# OR it can be written as

if page_number>=100 and page_number<=200:
    print('Yes between 100 & 200')

# OR it can be written as . Hoevr mouse

if 100 <= page_number <= 200:
    print('Yes between 100 & 200')