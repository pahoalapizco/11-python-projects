# Program that calculates tip % of an user check.

# calculate:
def calculate(subtotal: float, tip: float):
  if tip == 0.0:
    return subtotal
  
  total_tip = subtotal * (tip/100)
  total = subtotal + total_tip
  return total, total_tip


def validate_float_input(value: str) -> bool:
  splited_value = value.split('.')
  for val in splited_value:
    if not val.isdigit(): 
      return False
  
  return True


def run():
  subtotal = input('How mush is on your check? $')
  tip = input('How many perfent of tip do you want to pay? ')

  if not validate_float_input(subtotal) or not validate_float_input(tip):
    print('Sorry, we can not process your calculate requests.')
    return

  subtotal = float(subtotal)
  tip = float(tip)
  total, total_tip = calculate(subtotal, tip)


  output = f""" 
  This is your total check:
    Sub total: $ {subtotal}
         tips: $ {total_tip}  {tip}%
    _________________________
        total: $ {total}
  """
  print(output)
  

if __name__ == "__main__":
  run()