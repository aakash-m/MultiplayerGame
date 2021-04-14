import pygame as py

width = 500
height = 600
win = py.display.set_mode((width, height))
py.display.set_caption("Client")

clientNumber = 0


class Player:
    def __init__(self, x, y, Width, Height, Color):
        self.x = x
        self.y = y
        self.width = Width
        self.height = Height
        self.color = Color
        self.rect = (x, y, Width, Height)


def redrawWindow():
    win.fill(255, 255, 255)
    py.display.update()


def main():
    run = True

    while run:
        for event in py.event.get():
            if event.type == py.quit():
                run = False
                py.quit()
