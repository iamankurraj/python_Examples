from tkinter import VERTICAL
from turtle import position
from webbrowser import MacOSX


row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where you want to place the treasure:\n")

horizontal=int(position[0])
vertical=int(position[1])

selected_row=map[horizontal-1]
selected_column=map[vertical-1]


print(map[vertical-1])



print(f"{row1}\n{row2}\n{row3}")
