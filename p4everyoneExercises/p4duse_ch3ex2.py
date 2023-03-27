# payment and overtime calculating program\

hrs = input("Enter Hours");
rate = input("Enter Rate");
h = float(hrs)
r = float(rate)

if h > 40:
    print("Overtime")
    regular_pay = h * r 
    overtime_pay = (h - 40.0) * (r * 0.5)
    print(regular_pay, overtime_pay)
    total_pay = regular_pay + overtime_pay
else :
      print("Regular")
      total_pay = h * r; 
print("Pay", total_pay)
