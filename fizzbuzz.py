def fizzbuzz(n: int):
    x = 1
    while x <= n:
        if x%3 == 0 and x%5 == 0:
            print("Fizzbuzz")
        elif x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print(x)
        x+= 1


n = 50
fizzbuzz(n)