
# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()

row = int(input("Enter the row ?"))
col = int(input("Enter the column ?"))
for i in range(1, row, +1):
    for j in range(5, i, -1):
        print(" ", end="")

    print()
