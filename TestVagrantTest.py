basket = [
    {"Product": "Leather Wallet", "Unit Price": 1100, "GST (%)": 18, "Quantity": 1},
    {"Product": "Umbrella", "Unit Price": 900, "GST (%)": 12, "Quantity": 4},
    {"Product": "Cigarette", "Unit Price": 200, "GST (%)": 28, "Quantity": 3},
    {"Product": "Honey", "Unit Price": 100, "GST (%)": 0, "Quantity": 2},
]

total_amount = sum(item["Unit Price"] * item["Quantity"] * (1 + item["GST (%)"] / 100) * 0.95 if item["Unit Price"] >= 500 else item["Unit Price"] * item["Quantity"] * (1 + item["GST (%)"] / 100) for item in basket)

max_gst_product = max(basket, key=lambda x: x["Unit Price"] * x["Quantity"] * (x["GST (%)"] / 100))

print("Total Amount to be Paid:", total_amount)
print("Product with Maximum GST Amount:", max_gst_product["Product"])