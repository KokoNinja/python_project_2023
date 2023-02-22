###LIST  is muttable
colors = ['red', 'yellow', 'green']
# color--->l2-->
# 0-->red
# 1-->green
print(colors[2])
print(type(colors))

# add in the list
colors.append("pink")
print(colors)

# add black at index 1

colors.insert(2, 'black')
print(colors)

# remove green from colors
colors.remove('green')
print(colors)

# to print length
print(len(colors))

# to remove index
colors.remove(colors[1])
print(colors)

# pop colors
colors.pop()
print(colors)

# print index of the number
numbers = [98.2, 88, 77, 99, 0]
print(type(numbers[0]))

# TUPLE Set of fixed collection. Cannot append. Immutable

signal = ('red', 'yellow', 'green')
print(signal[1:])


# dictionary Key value - mobile automation

desired_cap = {
    "plarformName": 'android',
    "deviceName": 'oneplus',
    "platformVersion": 8

}
print(desired_cap)
print(desired_cap["deviceName"])

student_data = {
    "studentName": 'konika',
    "studentMailId": 'konika.negi@einfochips.com',
    "marks": [90, 45, 67, 67],
    "sports": {"indoor": "chess",
               "outdoor": "hockey"
               }
}
print(student_data)
print(student_data["marks"])
print(type(student_data["marks"]))
print(student_data["marks"][0])

all_marks = student_data["marks"]
print(all_marks[0])

print(student_data["sports"]["outdoor"])


#Boolean

check=True
print(check)
print(type(check))