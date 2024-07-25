# Sample inputs
a = 5

price1, discount1 = 50, 4  # for offer1
price2, discount2 = 60, 8  # for offer2

# Conditions
output1 = a >= 5  # True if a is greater than or equal to 5
output2 = a % 5 == 0  # True if a is divisible by 5 (leaves no remainder)
output3 = a % 2 != 0 and a < 10  # True if a is odd and less than 10
output4 = -10 <= a <= 10 and a % 2 != 0  # True if a is odd within -10 and 10
num_digits = len(str(a))  # Find number of digits in a
output5 = num_digits % 2 == 0 and num_digits <= 10  # True if a has even number of digits and less than or equal to 10

# Calculate discounted prices
discounted_price1 = price1 * (1 - discount1 / 100)
discounted_price2 = price2 * (1 - discount2 / 100)

# Check which offer is cheaper (strictly cheaper)
is_offer1_cheaper = discounted_price1 < discounted_price2

# Print outputs
print(f"output1: {output1}")
print(f"output2: {output2}")
print(f"output3: {output3}")
print(f"output4: {output4}")
print(f"output5: {output5}")
print(f"Offer 1 is cheaper: {is_offer1_cheaper}")
