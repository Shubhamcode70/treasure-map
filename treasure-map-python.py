from turtle import pos


row1 = ["🙄", "🙄", "🙄"]
row2 = ["🙄", "🙄", "🙄"]
row3 = ["🙄", "🙄", "🙄"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

'''map = [" ", " ", " "],[" ", " ", " "],[" ", " ", " "]'''

'''user input 31
3 and 1 should go in list index of map[3,1]
and the value should be there is X'''
position = input("Where do you want to put the trasure? : ")
#23

horizontal = int(position[0]) #2
vertical = int(position[1]) #3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
#print(f"{row1}{row2}{row3}")

