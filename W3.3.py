'''Create a multi-functional program that performs different tasks based on the user input. The program should support the following tasks:

Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.
Sorted Permutation (sorted_permutation): Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order. The order in which the permutations are printed is same as the previous one (Type: Filtering).
Repeat the Repeat (repeat_the_repeat): Given a number n, print the numbers from 1 to n in the same line and repeat this n times.
Repeat Incrementally (repeat_incrementally): Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total. For example, if n is 4, the output should be:
1
12
123
1234
Increment and Decrement (increment_and_decrement): Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1. For example, if n is 4, the output should be:
1
121
12321
1234321'''

task=input()
if task == 'permutation':
  s = input()
  for i in range(len(s)):
    for j in range(len(s)):
      if i != j:
        print(s[i]+s[j])

elif task == 'sorted_permutation':
  s = input()
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  for i in range(len(s)):
    for j in range(len(s)):
      if alpha.index(s[i]) < alpha.index(s[j]):
        print(s[i]+s[j])
        
elif task == 'repeat_the_repeat':
  s = int(input())
  count = s
  for j in range(1, count + 1):
    for i in range(1,s+1):
      print(i, end='')
    print()
    
elif task == 'repeat_incrementally':
  num = int(input())
  for i in range(1,num + 1):
    for j in range(1,i + 1):
      print(j,end='')
    print()
    
elif task == 'increment_and_decrement':
    x = int(input())
    for i in range(1,x + 1):
        for k in range(1,i + 1):
            b = k
            print(b,end='')
            continue
        for j in range(i - 1,0,-1):
            a = j
            print(a,end='')
        print()
    
