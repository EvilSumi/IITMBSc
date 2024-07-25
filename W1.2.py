# Sample inputs
a = 5
b = 6
price, discount_percent = 80, 5.75
total_mins = 470

# Provided calculations
output1 = a + b  # int: sum of a and b
output2 = 2 * (a + b)  # int: twice the sum of a and b
output3 = abs(a - b)  # int: absolute difference between a and b
output4 = abs(a * b - (a + b))  # int: absolute difference between sum and product of a and b

# Discounted price calculation
discounted_price = price * (1 - discount_percent / 100)  # float

# Rounding the discounted price
rounded_discounted_price = round(discounted_price)  # int

# Finding hours and minutes from total minutes
hrs = total_mins // 60  # int: floor division for hours
mins = total_mins % 60  # int: modulo for minutes remaining

# Print outputs (optional)
print(f"output1: {output1}")
print(f"output2: {output2}")
print(f"output3: {output3}")
print(f"output4: {output4}")
print(f"Discounted price: ₹{rounded_discounted_price}")  # Assuming price is in Indian Rupees
print(f"Time duration: {hrs} hrs {mins} mins")
