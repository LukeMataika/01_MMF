import re


# function goes here
def string_check(choice, options) : ...





























#regular expression to find if the item starts with a number
number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# , and possible abbreviations etc>
valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "fiji water", "fiji", "w", "d"],
  ["xxx"]
]

# valid options for free / no questions
yes_no = [
  ["yes", "y"],
  ["no", "n"]
]

# holds snack order for a single user
snack_order = []

# aks user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
 want_snack = input("Do you want to order snack? ").lower()
 check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks they want (and add to our snacks)
if check_snack == "yes":

  desired_snack = ""
  while desired_snack != "xxx"

    snack_row = []

    # ask user for desired snack and put it in lowercase
    desired_snack = input("snack: ").lower()

    if desired_snack == "xxx":
      break

    # if itemhas a number, seperate it into two (number / )
    if re.match(number_regex, desired_snack):
      amount = int(desired_snack)