# In this part, we will have a value where an odd or even are weird or not weird, and a specific range is weird or not weird.
# n = odd = weird
# n even 2 to 5, not weird
# n even 6 to 20, weird
# n > 20 not weird
n=23
if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n<=5:
        print("Not weird")
    elif n >=6 and n<=20:
        print("Weird")
    if n > 20:
        print("Not Weird")