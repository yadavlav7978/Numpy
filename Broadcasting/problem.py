prices=[10,20,30]

dicount=10

final_prices=[]

for price in prices:
    new_price=price-(price*dicount/100)
    final_prices.append(new_price)

print(final_prices)


# 👉 Here:

# Loop runs one by one
# Slower ❌
# Manual work ❌