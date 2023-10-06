import time
import random
from sympy import isprime

def main():
    while True:
        num = random.randint(1,100)
        prime_status = "prime" if isprime(num) else "not prime"
        print(f"(num) is (prime_status).")
        time.sleep(10)

if __name__ == "__main__":
    main()
