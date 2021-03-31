# functions go here
def string_check(choice, options):
 
  for var_list in options:
 
 # if the snack is one of the lists, return the filter
      if choice in var_list:
 
 # get full name of snack and put it
 # in title case so it looks nice when outputted
        chosen = var_list[0].title()
        print(chosen)
        is_valid = "yes"
        break
 
 # if the chosen option is not valid, set is_valid to no
  else:
      is_valid = "no"
 
# if the snack is not OK - ask question again.
  if is_valid == "yes":
     return chosen
  else:
     return "invalid choice"
 
# Valid snacks hold list of all snacks
# Each item in valid snacks is a list with
# Valid options for each snack <full name, full letter (a - e)
# , and possible abbreviations etc>
valid_snacks = [
 ["popcorn", "p", "corn", "a"],
["M&M's", "m&m's", "mms", "m", "b"], # first item is M&M
 ["pita chips", "chips", "pc", "pita", "c"],
 ["water", "w", "d"]
 ["xxx"]
]
 
yes_no = [
 ["yes", "y"],
 ["no", "n"] 
]
 
# holds snack order for a single UserWarning
snack_order = []
check_snack = "invalid choice"
while check_snack == "invalid choice":
 want_snack = input("Do you want to order snack? ").lower()
 check_snack = string_check(want_snack, yes_no)
 
# loop three times to make testing quicker


desired_snack = ""
while desired_snack != "xxx" :
  # ask user for desired snack and put it in in lowercase
  desired_snack = input("snack: ").lower()

  if desired_snack == "xxx":
    break

  # check if snack is valid
  snack_choice = string_check(desired_snack, valid_snacks)   
  print("snack choice: ", snack_choice)

  # add snack to list...

  # check that snack is not the exit code before adding
  if snack_choice != "xxx" and snack_choice != "in valid choice":
    snack_order.append(snack_choice)

# show snack orders
print()
if len(snack_order) == 0:
  print("snacks ordered: None")

else:
    print("snacks ordered:")

    for item in snack_order:
      print (item)