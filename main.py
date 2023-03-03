import time
from tkinter import *
from colorama import init, Fore
import threading
from button1_action import button1_custom_action

init()  # Initialize colorama

print(Fore.GREEN + "This text is in green color!")


def print_message():
    while True:
        output_text.insert('1.0', "Please press the 'S' key to continue\n")
        output_text.delete('5.0', END)  # clear the existing text in TXT_text
        time.sleep(1)


def button1_action():
    action_text.insert('1.0', "Button 1 pressed\n")
    data = TD_entry.get()  # get the text entered in TD_entry
    result = button1_custom_action(data)  # pass the data to button1_custom_action() function
    TXT_text.delete('1.0', END)  # clear the existing text in TXT_text
    TXT_text.insert('1.0', result)  # insert the returned data into TXT_text


def button1_action_thread():
    threading.Thread(target=button1_action).start()


top = Tk()
top.geometry("1000x500")

with open('D:/info.txt', 'r', encoding='utf-8') as f:
    info_dict = {}
    for line in f:
        key, value = line.strip().split('=')
        info_dict[key] = value

W_label = Label(top, text="W:")
W_label.place(x=10, y=20)

WD_label = Label(top, text=info_dict.get('name', ''))
WD_label.place(x=80, y=20)

B_label = Label(top, text="B:")
B_label.place(x=10, y=40)

BD_label = Label(top, text=info_dict.get('pass', ''))
BD_label.place(x=80, y=40)

T_label = Label(top, text="T:")
T_label.place(x=10, y=60)

TD_entry = Entry(top, width=60)
TD_entry.place(x=80, y=60)
TD_entry.insert(0, '')

BT_label = Label(top, text="BT:")
BT_label.place(x=10, y=80)

# Add three buttons
button1 = Button(top, text="Button 1", command=button1_action_thread)
button1.place(x=10, y=120)

button2 = Button(top, text="Button 2", command=lambda: threading.Thread(target=button2_action).start())
button2.place(x=80, y=120)

button3 = Button(top, text="Button 3", command=lambda: threading.Thread(target=button3_action).start())
button3.place(x=150, y=120)

action_label = Label(top, text="Action:")
action_label.place(x=10, y=160)

action_text = Text(top, width=40, height=5)
action_text.place(x=60, y=180)

output_label = Label(top, text="Output:")
output_label.place(x=10, y=280)

output_text = Text(top, width=80, height=5)
output_text.place(x=60, y=300)

TXT_label = Label(top, text="TXT:")
TXT_label.place(x=10, y=400)

TXT_text = Text(top, width=40, height=2)
TXT_text.place(x=60, y=420)

# Start the print_message thread
threading.Thread(target=print_message, daemon=True).start()

# Bind the 'S' key to the print_message() function
top.bind('s', lambda event: None)

top.mainloop()
