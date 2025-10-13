def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return number // 2
  elif number % 2 == 1:
    print(3 * number + 1)
    return 3 * number + 1

while True:
  try:
    print("Enter a number:" )
    user_value = int(input())
    while True:
      return_value = collatz(user_value)
      if return_value == 1:
        break
      else:
        user_value = return_value      
    break
  except KeyboardInterrupt:
    print('Progam ended')
    break
  except ValueError:
    print('Error: Must be integer')


  

































# while True:
#   return_value = collatz(user_value)
#   if return_value != 1:
#     user_value = return_value
#   else:
#     break    