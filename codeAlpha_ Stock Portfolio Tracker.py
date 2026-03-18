# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")

# Step 2: Take user input
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity

# Step 3: Calculate total investment
print("\n📈 Your Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} → {qty} shares × ${price} = ${value}")

print("\n💰 Total Investment Value: $", total_investment)
