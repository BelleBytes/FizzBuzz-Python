def fizzbuzz(n: int):
    x = 1
    result = []
    while x <= n:
        if x%3 == 0 and x%5 == 0:
            result.append("Fizzbuzz")
        elif x%3 == 0:
            result.append("Fizz")
        elif x%5 == 0:
            result.append("Buzz")
        else:
            result.append(x)
        x+= 1
    return result
