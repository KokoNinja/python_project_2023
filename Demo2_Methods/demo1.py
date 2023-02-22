radius=10
result=3.14*radius*radius
print(result)

radius=20
result=3.14*radius*radius
print(result)

# imported area_forumla from area package to call the method
from area import area_formula

#calling the function
res=area_formula.area_of_circle(10)
print(res)

res=area_formula.area_of_circle(20)
print(res)

resul=area_formula.area_of_triangle(10,10)
print (resul)

output=area_formula.area_of_square(10)
print (output)

outcome=area_formula.area_of_trapizium(2,3,4)
print(outcome)

import math
print(math.pi)

ret=math.sqrt(64)
print(ret)

math.pow()