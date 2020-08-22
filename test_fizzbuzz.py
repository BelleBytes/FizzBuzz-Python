from fizzbuzz_implementation import fizzbuzz

def test_multiple_of_three():
    result = fizzbuzz(15)
    assert result[2] == "Fizz", "3 Should be Fizz"
    assert result[5] == "Fizz", "6 Should be Fizz"

def test_multiple_of_five():
    result = fizzbuzz(15)
    assert result[4] == "Buzz", "3 Should be Buzz"
    assert result[9] == "Buzz", "10 Should be Buzz"

def test_multiple_of_three_and_five():
    result = fizzbuzz(50)
    assert result[14] == "Fizzbuzz", "15 Should be Fizzbuzz"
    assert result[29] == "Fizzbuzz", "30 Should be Fizzbuzz"

if __name__ == "__main__":
    test_multiple_of_three()
    test_multiple_of_five()
    test_multiple_of_three_and_five()
    print("Everything passed")