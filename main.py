import random
# import mymodule
def rands():
  # generate random whole number
  random_integer = random.randint(1, 10)
  print(random_integer)
  # print(mymodule.pi)
  
  # generate random float number
  random_float = random.random()
  print(random_float)
  # generate random floats between 0 and 5
  random_float = random.random() * 5
  print(random_float)

def cointoss():
  #Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
# import random
  toss = random.randint(0,1)
  print(toss)
  if toss == 0:
    print("Tails")
  else:
    print("Heads")
def listfun():
  states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

  print(states_of_america)
  print(len(states_of_america))
  return(states_of_america)

  dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

def banker():
  # Import the random module here
  
  # Split string method
  names_string = input("Give me everybody's names, separated by a comma. ")
  names = names_string.split(", ")
  print(names)
  x = ['amy', 'ang', 'gru', 'ata', 'stax']
  # 🚨 Don't change the code above 👆
  ch = random.randint(0, len(x) - 1)
  return(x[ch])
  #Write your code below this line 👇
  
  
  # cointoss()
  # l = listfun()
choice = banker()
print(f"{choice} is going to buy the meal today!")
