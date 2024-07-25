# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    while True:  # Repeat indefinitely until the terminal condition is met
        n = int(input())
        if n == 0:  # The terminal condition
            break
        total += n  # Add n to the total
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # Repeat indefinitely until the terminal condition is met
        line = input()
        if line == "":  # The terminal condition (an empty line)
            break
        quantity, price = line.split()  # split uses space by default
        quantity, price = int(quantity), float(price)  # convert to int and float respectively
        total_price += quantity * price  # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    words = input().split()
    result = [word for word in words if word.endswith('ed') or word.endswith('ing')]
    print(' '.join(result))


elif task == "reverse_sum_palindrome":
    def is_palindrome(s):
        return s == s[::-1]

    n = int(input())
    attempts = 0
    while not is_palindrome(str(n)) and attempts < 1000:  # Avoid infinite loop
        n += int(str(n)[::-1])
        attempts += 1
    if is_palindrome(str(n)):
        print(n)
    else:
        print("Palindrome not found within 1000 attempts")

elif task == "double_string":
     s = input()
     doubled = ''.join([char * 2 for char in s])
     print(doubled)

elif task == "odd_char":
    s = input()
    result = ''.join([char for i, char in enumerate(s) if i % 2 != 0])
    print(result)

elif task == "only_even_squares":
    n = int(input())
    result = [i ** 2 for i in range(n) if i ** 2 % 2 == 0]
    print(result)

elif task == "only_odd_lines":
    import sys
    lines = sys.stdin.read().splitlines()
    for i, line in enumerate(lines):
        if i % 2 != 0:  # Only print odd lines (1-based index)
            print(line)

x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1,x2=x2,x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 
temp = y1
y1 = y2
y2 = y3
y3 = temp

# create a new variable `a` with the value of `z`
a=z
# delete the variable `z`
del z
print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)
