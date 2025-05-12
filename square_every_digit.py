import codewars_test as test

def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(int(digit)**2)
    return int(result)

@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
        test.assert_equals(square_digits(0), 0)
