data ="Hello World"

print(data[0])

# includes only 0,1 & 2 index. 3rd index wont be included.
print(data[0:3])
print(data[0:5])
print(data[1:])

# space is also allocated with index
print(data[5])

# -1, -2 will pick from last character

print(data[-1:])  # last one character
print(data[-2:]) # last two character
print(data[-5]) # accessing the index position from last. Single character will be printed if : is not given

# start and end point
print(data[6:])

print(data.index("World"))
print(data[data.index("World")])

# replaces the text
print(data.replace("World", "Loki"))

mail_id="john.dev@gmail.com"
print(mail_id[0:8])

print(mail_id[0:mail_id.index("@")])

list=mail_id.split("@")
print(list)

list1=mail_id.split("@")[0]
print(list1)



