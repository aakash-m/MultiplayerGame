import pygame as py
import pygame.draw

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
        self.vel = 3

    def draw(self, Win):
        py.draw.rect(Win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[py.K_LEFT]:
            self.x -= self.vel

        if keys[py.K_RIGHT]:
            self.x += self.vel

        if keys[py.K_UP]:
            self.y -= self.vel

        if keys[py.K_DOWN]:
            self.y += self.vel


def redrawWindow(Win, player):
    Win.fill(255, 255, 255)
    player.draw(Win)
    py.display.update()


def main():
    run = True
    p1 = Player(50, 50, 100, 100, (0, 255, 0))

    while run:
        for event in py.event.get():
            if event.type == py.quit():
                run = False
                py.quit()

        p1.move()
        redrawWindow(win, p1)


main()
