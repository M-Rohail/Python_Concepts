# Create a program to find the profit/loss amount of a shop.

# Get two input integers cost_price and selling_price.
# Calculate the profit or loss amount (i.e. selling_price - cost_price).
cost_price = int(input("Enter the cost price"))
selling_price = int(input("Enter the selling price :"))

if selling_price == cost_price:
    print("No Profit/No loss")
elif selling_price > cost_price:
    profit = selling_price-cost_price
    print("Your Profit is:", profit)
elif selling_price < cost_price:
    loss = cost_price-selling_price
    print("Your Loss is :", loss)
else:
    print("Invalid Syntax")
