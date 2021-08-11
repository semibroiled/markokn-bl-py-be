def check_prime(num):

    num = int(num)

    if num<=1:
        return False
    for divisors in range(2, num-1):
        if num%divisors == 0:
            return False
    return True

while True:
    print(check_prime(input()))