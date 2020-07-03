def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return "Enter number greater than 1"


number = int(input("ENter a number: "))
print(is_prime(number))
