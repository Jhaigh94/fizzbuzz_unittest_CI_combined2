def fizzbuzz(n):
    if n % 15 ==0:
        return "FizzBuzz"
    if n % 3 ==0:
        return "Fizz"
    if n % 5 ==0:
        return "Buzz"
    return str(n)

def fizzbuzz_list(n):
    output = []
    for i in range (1, n+1):
        output.append(fizzbuzz(i))
    return output
