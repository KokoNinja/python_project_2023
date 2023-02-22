
age1= int(input("Enter the age1:"))
age2= int(input("Enter the age2:"))
age3=int(input("Enter the age3:"))

if age1<age2 and age1<age3:
    print('age1 is younger')
elif age2<age1 and age2<age3:
    print('age2 is younger')
elif age3<age1 and age3<age2:
    print('age3 is younger')
else:
    print('All of same age')