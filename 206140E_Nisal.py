
import random

def generate_random_number():
  """Generates a random number between 1 and 100."""
  random_number = random.randint(1, 100)
  return random_number

# Generate a random number and print it to the console.
random_number = generate_random_number()
print(random_number)


def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True


num = int(input("Enter a number: "))
if is_prime(num):
  print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")



