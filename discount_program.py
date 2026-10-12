# Day 6: Smart Checkout System

print("=== WELCOME TO SMART CART ===")

# Step 1: User details and cart inputs
customer_name = input("Enter your name: ").strip()
cart_total = float(input("Enter your total cart value (in Rs): "))
membership = input("Do you have VIP Membership? (yes/no): ").strip().lower()

# Boolean flag to check membership
is_vip = (membership == "yes")

# Variables to calculate final bill
discount_percentage = 0
shipping_fee = 0

# Step 2: Discount Logic using 'and' / 'or'
if cart_total >= 1000 and is_vip:
    discount_percentage = 20
elif cart_total >= 1000 and not is_vip:
    discount_percentage = 10
elif cart_total >= 500:
    discount_percentage = 5
else:
    discount_percentage = 0

# Step 3: Shipping Fee Logic
# If cart is less than 500 AND user is not a VIP, add shipping fee
if cart_total < 500 and not is_vip:
    shipping_fee = 50
else:
    shipping_fee = 0

# Step 4: Calculations
discount_amount = (cart_total * discount_percentage) / 100
amount_after_discount = cart_total - discount_amount
final_total = amount_after_discount + shipping_fee

# Step 5: Detailed Bill Output
print("\n" + "=" * 30)
print(f"Customer Name: {customer_name}")
print(f"Original Cart Total: Rs. {cart_total}")
print(f"VIP Status: {'Active' if is_vip else 'Not Active'}")
print(f"Discount Applied: {discount_percentage}% (-Rs. {discount_amount})")
print(f"Shipping Fee: Rs. {shipping_fee}")
print("-" * 30)
print(f"Final Payable Amount: Rs. {final_total}")
print("=" * 30)