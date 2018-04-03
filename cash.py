
def make_change(cents):
  # return the fewest coins possible


  quarters = 0
  dimes = 0
  nickles = 0

  # cents = ???? get just the .22 from 4.22
  #
  # if cents % 25 == 0:
  #   quarters = Int(cents / 25)
  #   return quarters
  # else:
  #   cents -= (quarters * 25)
  # if cents % 10 == 0:
  #   dimes = Int(cents / 10)
  #   return quarters + dimes
  # else:
  #   cents -= (dimes * 10)
  # if cents % 5 == 0:
  #   nickles = Int(cents / 5)
  #   return quarters + dimes + nickles
  # else:
  #   cents -= (nickles * 5)
  #   return quarters + dimes + nickles + cents



print(make_change(.80))


def make_change(cents):
  # return the fewest coins possible

  quarters = 0
  dimes = 0
  nickles = 0

  # cents = ???? get just the .22 from 4.22


  if cents >= 25:
    quarters = cents // 25
    cents -= (quarters * 25)
    print(cents)
    return cents
  if cents >= 10:
    dimes = cents // 10
    cents -= (dimes * 10)
    return cents
  if cents >= 5:
    nickles = cents // 5
    cents -= (nickles * 5)
    return cents
  if cents >= 0:
    return cents
  print(quarters + dimes + nickles + pennies)



print(make_change(80))






print(80 // 25)
