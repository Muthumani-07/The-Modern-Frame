from datetime import datetime, timedelta

start_date = datetime(2025, 4, 1)
end_date = datetime(2025, 9, 30)

sales_by_month = {}
retail_sales = 0
corporate_sales = 0
mid_period_sales = 0

current_date = start_date

while current_date <= end_date:
    month_key = current_date.strftime("%B")
    month_end = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    day_count = 0
    month_sales = 0

    while current_date <= month_end and current_date <= end_date:
        n = day_count + 1
        vehicles_sold = n * n + 1
        month_sales += vehicles_sold

        if n % 5 == 0:
            corporate_sales += vehicles_sold
        else:
            retail_sales += vehicles_sold

        if datetime(2025, 8, 15) <= current_date <= datetime(2025, 9, 15):
            mid_period_sales += vehicles_sold

        current_date += timedelta(days=1)
        day_count += 1

    sales_by_month[month_key] = month_sales

for month, count in sales_by_month.items():
    print(f"{month}: {count}")

print(f"Retail Sales: {retail_sales}")
print(f"Corporate Sales: {corporate_sales}")
print(f"Sales from Aug 15 to Sep 15: {mid_period_sales}")
