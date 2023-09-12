price = input(
    'Enter the price of the item to determine the discounted price: ')
# convert string to an integer
price = int(price)

if price >= 300:
    price = price - (price * 0.3)
elif price >= 200 & price < 300:
    price = price - (price * 0.2)
elif price >= 100 & price < 200:
    price = price - (price * 0.1)
else:
    price = price - (price * 0.05)

print(f'The discounted price is {price}')


# alternate way of handling it:

# if price >= 300:
#     price *= 0.7  # (1 - 0.3)
# elif price >= 200:
#     price *= 0.8  # (1 - 0.2)
# elif price >= 100:
#     price *= 0.9  # (1 - 0.1)
# elif price < 100 and price >= 0:
#     price *= 0.95  # (1 - 0.05)