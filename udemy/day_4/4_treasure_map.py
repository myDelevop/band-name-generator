# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

if len(position) == 2:
    right_pos = int(position[0]) - 1
    left_pos = int(position[1]) - 1

    if not (0 > right_pos > 3 or 0 > left_pos > 3):
        map[left_pos][right_pos] = "X"
    else:
        print("Not a valid position")
else:
    print("Not a valid number")


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

