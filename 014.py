item=float(input("Enter the price of the item: "))
gst_rate=float(input("Enter the GST rate (in percentage): "))

gst_amount=item * (gst_rate / 100)
total_price=item + gst_amount

print(f"The total price is: {total_price:.2f}")