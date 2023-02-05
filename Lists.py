# food = ["Pizza", "Burger", "Spaghitee"]
# # food.sort()
# food.clear()
# for x in food:
#     print(x)

# 2d Lists
drinks = ["coffee", "Soda", "Tea"]
dinner = ["pizza", "Burgers", "Hotdogs"]
dessert = ["Cake", "Ice cream", "choc"]
food = [drinks, dinner, dessert]
for i in range(0, 3, +1):
    for j in range(3):
        print(food[i][j])
