p1 = float(input("Enter price of product 1: "))
q1 = int(input("Enter quantity: "))

p2 = float(input("Enter price of product 2: "))
q2 = int(input("Enter quantity: "))

p3 = float(input("Enter price of product 3: "))
q3 = int(input("Enter quantity: "))

subtotal = p1 * q1 + p2 * q2 + p3 * q3
discount = subtotal * 10 / 100
amount = subtotal - discount
gst = amount * 18 / 100
final_amount = amount + gst

print("Subtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Amount =", final_amount)
