gross_sales = float(input("enter a gross sales"))
discount = 1 / 10 * gross_sales
net_sales = gross_sales - discount
print("your net sales is = ",net_sales , "with discount = ",discount )

p = float(input("enter your physics marks"))
m = float(input("enter your maths marks"))
c = float(input("enter your computer marks"))

avg = ( p + m + c )/3

print("your phy mark" "=" ,p)
print("your math mark" "=", m)
print("your computer mark" "=", c)

print(avg)

a = int(input("enter first number "))
b = int(input("enter second number "))

c = a + b
a = c - a
b = c - b

print(" after swap the number ")
 
print(a)
print(b)

a = 5
b = 2
temp = b
b= a
a = temp
print(a, b)
