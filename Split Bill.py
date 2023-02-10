# Create a program to split the restaurant bill among friends.

# Get an integer value for the total number of friends and assign it to the total_friends variable.
# Get an integer value for the total bill and assign it to the total_bill variable.
# Add 20% tax to the subtotal bill and divide the total bill among friends.

no_of_friend = int(input("Enter the no of friend:"))
total_bill = int(input("Enter the bill:"))
cal_tax1 = int(total_bill*(80/100))
cal_tax2 = total_bill-cal_tax1
total_bill = total_bill+cal_tax2
print("Your Total bill with 20%tax is :", total_bill)
print("Each friend give :", round(total_bill/no_of_friend, 1))
