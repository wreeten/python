# this is using the sort function, and not the data structure
list = [ 1, 3, 5 ,7, 2, 3, 1]
print("list in order: ")
for i in sorted(list):
    print(i,end= " ")

print ("\r")

print("listed prints without duplicate")
for i in sorted(set(list)):
    print(i,end=" ")

print("\r")
for i in sorted(list):
    print(i, end=" ")
print("\r")
basket=['apple', 'cherry', 'banana', 'zebra']
for i in sorted(basket):
    print(i, end= " ")
print("\r")    
for i in reversed(basket):
    print(i, end=" ")
print("\r")
price=['001','003','242','291','321']
for i in sorted(price):
    print(i, end=" ")