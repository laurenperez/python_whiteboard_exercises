# create an algorithm that detects whether or not a credit card number is valid

card_num = input("what is your credit card number?")

numbers = []
for c in card_num:
  numbers.append(int(c))
#print(numbers)

def check_for_legit_card(lst, num):
  even_digits = lst[1::2]
  odd_digits = lst[::2]
  times_two = [x*2 for x in even_digits]
  sum = 0
  for x in times_two:
    if x > 10:
      x = int(x / 10) + (x % 10)
    sum +=x
  for x in odd_digits:
    sum += x
  if sum % 10 == 0:
    print("its a card!")
    first_two = int(num[0]+num[1])
    amex_starts = [34, 37]
    mc_starts = [51, 52, 53, 54, 55]

    if first_two in amex_starts and len(num) == 15:
      card_type = "AMEX"
    elif first_two in mc_starts and len(num) == 16:
      card_type = "MasterCard"
    elif len(num) == 13 or len(num) == 16:
      if num[0] == "4":
        card_type = "Visa"
      else:
        card_type = "invalid card number"
    else:
      card_type = "invalid card number"
    print(card_type)
  else:
    print("Not a valid card")


check_for_legit_card(numbers,card_num)
