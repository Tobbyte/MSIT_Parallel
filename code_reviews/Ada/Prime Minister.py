def is_divisible_by(number, by):
    if number % by == 0:
        return True
    else:
        return False


def is_prime(number):
    if number <=1:
        return False

    for divisor in range(2, number):
        if is_divisible_by(number, divisor):
            return False
    return True


def primes_in_range(start, end):
    for number in range(start, end):
        if is_prime(number) == True:
            print(f"The number {number} is prime")


def main():
    start = int(input("Type here the start of your desired range: "))
    end = int(input("Type here the end of your desired range: "))
    primes_in_range(start, end)


if __name__ == "__main__":
    main()

#print(f"Is 10 divided by 2? {is_divisible_by(10, 2)}")
#print(f"Is 10 divided by 3? {is_divisible_by(10, 3)}")
#print(f"Is 20 divided by 11? {is_divisible_by(20, 11)}")
#print(is_prime(10))
#print(is_prime(2))
#print(is_prime(13))
