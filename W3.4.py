'''You are tasked with writing a program that can handle various tasks based on the input. The first line of the input represents the task to be performed. The possible tasks are:

factors - Find the factors of a number n (including 1 and itself) in ascending order.
find_min - Take n numbers from the input and print the minimum number.
prime_check - Check whether a given number is prime or not.
is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
any_true - Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
manhattan - Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
Write a program to solve these tasks. Use loops where necessary.'''

# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()

if task == 'factors':
  n = int(input())
  for i in range(1,n + 1):
    if n % i == 0:
      print(i)
      
elif task == 'find_min':
  n = int(input())
  smallest = 1000000

  for i in range(n):
    a = int(input())
    if (a < smallest):
      smallest = a
  print(smallest)
  
elif task == 'prime_check':
  num = int(input())
  if num > 1:
    for i in range(2,num):
      if num % i == 0:
        print(False)
        break
      else:
        print(True)
        break
  
  
elif task == 'is_sorted':
  w = str(input())
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  for i in range(len(w)):

    if alpha.index(w[i]) > alpha.index(w[i + 1]):
      print(False)
      break
    else:
      print(True)
      break  
  
elif task == 'any_true':
  n = int(input())
  is_div_3 = False
  for i in range(n):
    a = int(input())
    if (a % 3 == 0):
      is_div_3 = True
    else:
      continue
  print(is_div_3)
  
elif task == 'manhattan':
  x, y = 0, 0
  while True:
    direction = input()
    if direction == 'STOP':
      break
    elif direction == 'UP':
      y += 1
    elif direction == 'DOWN':
      y -= 1
    elif direction == 'LEFT':
      x -= 1
    elif direction == 'RIGHT':
      x += 1
  manhattan_distance = abs(x) + abs(y)
  print(manhattan_distance)
