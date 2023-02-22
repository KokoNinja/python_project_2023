custName = 'Mary Smith'
itemDesc = ['Shirt', 'Top', 'Bag', 'Cloth']

outOfStock=False

price=100
quantity=1
tax=price*quantity*10/100


if quantity>1:
    message=custName + "wants to buy " + str(itemDesc) +'s'
else:
    message = (custName + "wants to buy " + str(quantity) + str(itemDesc[3]))

print (message)

total=price * quantity * tax
print(total)

if outOfStock:
    print('item is unavailable')
else:
    print('Item is available')




