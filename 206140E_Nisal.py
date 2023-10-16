import random

def generate_random_number():
  """Generates a random number between 1 and 100."""
  random_number = random.randint(1, 100)
  return random_number

# Generate a random number and print it to the console.
random_number = generate_random_number()
print(random_number)

