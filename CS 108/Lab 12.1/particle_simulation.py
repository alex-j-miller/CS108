"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Particle Simulation'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT


        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,2,1])
        self.drawing.bg = "black"
        PushButton(box, text= 'Add particle', command= self.add_particle, grid= [0, 1])
        
        self.drawing.when_clicked = self.check_remove_particle
        
        self.p_list = []
        app.repeat(10, self.draw_frame)
    
    def check_remove_particle(self, event):
        copy = self.p_list[:]
        for p in self.p_list:
            if p.is_clicked(event.x, event.y):
                self.p_list.remove(p)
        
    def add_particle(self):
        radius = randint(5, 25)
        particle = Particle(randint(25, self.drawing.width - 25),
                            randint(25, self.drawing.height - 25),
                            randint(-radius // 10, radius // 10),
                            randint(-radius // 10, radius // 10),
                            radius,
                            get_random_color()
                            )
        self.p_list.append(particle)
        
    def draw_frame(self):
        self.drawing.clear()
        for particle in self.p_list:
            particle.move(self.drawing)
        for i in range(len(self.p_list)):
            for j in range(i):
                self.p_list[i].bounce(self.p_list[j])
        for particle in self.p_list:
            particle.draw(self.drawing)
app = App()
ParticleSimulation(app)
app.display()

