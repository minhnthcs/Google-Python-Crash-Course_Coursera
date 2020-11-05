def factorial(number):
    print("Factorial called with " + str(number))
    if number < 2:
        return 1
    result = number * factorial(number-1)
    print("Returning " + str(result) + " for factorial of " + str(number))
    return result

def main():
    factorial(6)

if __name__ == "__main__":
    main()
