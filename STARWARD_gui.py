import PySimpleGUI as sg


PLAYERS = [
	 {'player':1, 'ships' : 2, 'power' : 2, 'risk': '1'},
	 {'player':2, 'ships' : 2, 'power' : 2, 'risk': '2'},
	 {'player':3, 'ships' : 2, 'power' : 2, 'risk': '3'},
	 {'player':4, 'ships' : 2, 'power' : 2, 'risk': '4'} ]

sg.change_look_and_feel('DarkBlue13')    # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Submit(), sg.Cancel('Finished')] ,
            [sg.Text(PLAYERS[0])],
            [sg.Text(PLAYERS[1])], 
            [sg.Text(PLAYERS[2])],
            [sg.Text(PLAYERS[3])],
        ]

# Create the Window
window = sg.Window('Stardward', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Finished'):   # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()