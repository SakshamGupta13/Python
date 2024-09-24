# Conversion rate

inr_to_usd_rate = 0.012  # 1 INR = 0.012 USD

# Amount in INR
inr_amount = 1000

# Conversion
usd_amount = inr_amount * inr_to_usd_rate

print(f"{inr_amount} INR is equal to {usd_amount:.2f} USD")