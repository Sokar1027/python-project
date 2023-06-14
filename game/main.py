import random



def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input("piedra, papel o tijera => ")
  computer_option = random.choice(options)
  user_option = user_option.lower()

  
  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None, None
  
  print('user option es =>', user_option)
  print('computer option es =>', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if (user_option == computer_option):
    print("empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("user ha ganado!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("computer gano")
      computer_wins += 1
  
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("piedra gana a tijera")
      print("computer gana")
      computer_wins += 1
    else:
      print("tijera gana a papel")
      print("user gano")
      user_wins += 1
    
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("user gano")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("computer gana")
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
  
    print('~' * 10)
    print('USER WINS =>',user_wins)
    print('~' * 10)
  
    print('~' * 10)
    print('COMPUTER WINS =>', computer_wins)
    print('~' * 10 )
  
    rounds += 1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
   
    
  
    if computer_wins == 3:
      print('-' * 10)
      print('¡el ganador es COMPUTER!')
      print('-' * 10)
      break 
  
    if user_wins == 3:
      print('-' * 10)
      print('¡el ganador es USER!')
      print('-' * 10)
      break 


run_game()