x = 1

while x <= 50:
    if x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    elif (x%3 == 0) and (x%5 == 0):
        print("Fizzbuzz")
    else:
        print(x)
    x+= 1