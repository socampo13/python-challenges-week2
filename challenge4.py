### 🌟 **Challenge 4: Generators**
##* Create a generator function that yields prime numbers indefinitely.
##* Expected function: `prime_generator() -> Generator[int, None, None]`.

from typing import Generator

def prime_generator() -> Generator[int, None, None]:
    def es_primo(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2 
    while True:
        if es_primo(num):
            yield num
        num += 1

## Test
if __name__ == "__main__":
    primes = prime_generator()
    for _ in range(10):
        print(next(primes))