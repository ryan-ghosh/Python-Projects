def isprime(num):
    if num == 4:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

def allPrimes(n):
    for i in range(n):
        if i<=3:
            print(i)
        if i%2!=0 and i>3:
            if isprime(i):
                print(i)

if __name__ == "__main__":
    inp = int(input("Enter a number and I will check if it is prime: "))
    allPrimes(inp)