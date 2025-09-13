# Fixed stock prices
prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140}

total = 0
print("📊 Simple Stock Tracker")
print("Available stocks:", ', '.join(prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done'): ").upper()
    if stock == "DONE":
        break
    if stock in prices:
        qty = int(input("Enter quantity: "))
        total += prices[stock] * qty
    else:
        print("❌ Invalid stock symbol.")

print(f"\n💼 Total Investment: ₹{total}")

