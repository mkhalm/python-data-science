#1-lists - a lists of things and you want to know the order.
#Order is important and can change lists (add or delete things within the list)
from functools import reduce

odds = [5,7,9]

#get sum - different ways
a=sum(odds)

total=0 #variable to set up the for loop
for num in odds:
    total += num #total=total+num1


total = 0
for i, num in enumerate(odds): #enumerate returns a tuple--read only
    total = total + (i * num)

roots= [n**0.5  for n in odds]
cuberoots =[n**(1/3)  for n in odds]
divisibleby5 = [n**(1/3)  for n in range(31) if n%5==0]


#how to use map. map is a generator and for it to do loop over anything, you have to add list()
#lambda is an inline function
list(map(lambda n: n**(1/3), odds))
list(filter(lambda n: n < 5, [3,4,5,6,7]))
reduce(lambda total, n: total+n, odds, 10)

#2 - tuple You still want order, but can't change it. You can do everything you can do as lists, but you can add/subtract items from the tuple
tup1=(3,4)

#3 - set -- no order, iterable (able to loop over them), unique, mutable, only takes immutable/hashable values
s1 = {3,4}

#4 dictionaries
#no order, iterable,keys are unique, values aren't necessarily unique, keys are hashable/immutable. Based on sets
d={}
for n in range(5):
    d[n] = n **2

d.get(5, 'default')
