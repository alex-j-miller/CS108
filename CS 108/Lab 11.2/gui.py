"""CS 108 Lab 11.2

This module implements a basic calculator GUI.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2020 - ported to ZyLabs
@date: Spring, 2021 - ported to GuiZero

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from guizero import App, Box, Text, TextBox, ButtonGroup, PushButton
from calculator import Calculator


class CalculatorApp:

    def __init__(self, app):
        """Build the Calculator interface."""

        # Configure the application GUI.
        app.title = 'Calculator'
        app.width = 300
        app.height = 200
        app.font = 'Helvetica'
        app.text_size = 12

        # Instantiate a single calculator object for repeated use.
        self.calculator = Calculator()

        # Add the operand-input widgets.
        box = Box(app, layout='grid')
        Text(box, text="Input 1:", grid=[0, 0], align='right')
        self.input1_entry = TextBox(box, width=6, grid=[1, 0], align='left')
        Text(box, text="Input 2:", grid=[0, 1], align='right')
        self.input2_entry = TextBox(box, width=6, grid=[1, 1], align='left')
        
        self.operator_choice = ButtonGroup(box, options= ['+', '-', '*', '/'], horizontal= True, grid= [0, 2])
        calculate = PushButton(box, text= 'Calculate', grid= [0, 3], command= self.do_calculation)
        self.answer = Text(box, grid= [1, 3])
        
        PushButton(box, text= 'Memory', grid= [0, 4], command= self.memory)
        self.memory_text = Text(box, grid= [1, 4])
    
    def do_calculation(self):
        self.result = self.calculator.calculate(self.input1_entry.value, self.operator_choice.value, self.input2_entry.value)
        self.answer.value = str(self.result)
    
    def memory(self):
        self.calculator.set_memory(self.result)
        self.memory_text.value = str(self.calculator.memory)
        
app = App()
CalculatorApp(app)
app.display()
