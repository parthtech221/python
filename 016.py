item=[]
n=int(input("Enter the number of items: "))


for i in range(n):
    price=float(input(f"Enter the price of item {i+1}: "))
    item.append(price)

    
gst_rate=float(input("Enter the GST rate (in percentage): "))
total_price=0


for price in item:
    total_price+=price
    
print(f"The total price for all items is : {total_price:.2f}")
print(f"The GST amount for all items is  : +{total_price*(gst_rate/100):.2f}")
print(f"The total price for all items is : {total_price+(total_price*(gst_rate/100)):.2f}")

    