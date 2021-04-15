import re

# works out wether string has numbers# and seperates string into amount and item

test_strings = [
  "popcorn",
  "2pc",
  "1.5oj",
  "4oj",
]

for item in test_strings:

  # regular expression to find if the item starts with a number
  number_regex = "^[1-9]"

  # if an item has a number, seperate it into two (number / item)
  if re.match(number_regex, item):
      amount = int(item[0])
      desired_snack = item[1:]

  else:
      amount = 1
      desired_snack = item

  #remove white space around snack
  desired_snack = desired_snack.strip()

  # if item does not have a number in front, set number to 1

  # print order
  print("amount:", amount)
  print("snack: ", desired_snack)
  print("length of snack:", len(desired_snack))
