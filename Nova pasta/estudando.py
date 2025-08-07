hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = sum(prices)

average_price = total_price / len(prices) 

print("Average Haircut Price:", average_price)

new_prices = [price -5 for price in prices]

print(new_prices)

# Calculate total revenue

def calculate_revenue(prices, last_week):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * last_week[i]
    return total, total / 7

total_revenue, average_daily_revenue = calculate_revenue(prices, last_week)
print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("Cuts Under $30:", cuts_under_30)