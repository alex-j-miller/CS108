"""CS 108 Lab 11.0

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from guizero import App, Text, PushButton, TextBox


class MyApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'My Application'
        app.width = 300
        app.height = 150
        app.font = 'Helvetica'
        app.text_size = 12

        # Add the widgets.
        hello_text = Text(app, text='Please enter your name.')
        name_input = TextBox(app)
        quit_button = PushButton(app, command= app.destroy, text= 'Goodbye!')
        
# Create the GuiZero application.
app = App()
my_app = MyApp(app)
app.display()
