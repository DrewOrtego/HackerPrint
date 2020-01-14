import string
from random import choice
from time import sleep

digit_list = ''.join((string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation))

def get_names():
  """Get a name from the list of students"""
  with open('names.txt') as names:
    names = [line.lower().strip('\n') for line in names.readlines()]
    names = list(map(lambda name: name.title(), names))
  return names

def hacker_print(name):
  """Print out a sting hacker-style!"""
  CBLINK = '\033[5m'
  for i, char in enumerate(name):
    for digit in digit_list:
      if digit != char:
        print(
          '\r',
          ''.join(choice(digit_list) for _ in range(len(name))),
          name[:i+1], 
          end="", sep=(CBLINK + '\rAnd the winner is! '), flush=True
        )
        sleep(0.001)

names = get_names()
while(True):
  random_name = choice(names)
  # print(random_name)
  hacker_print(random_name)
  input()
