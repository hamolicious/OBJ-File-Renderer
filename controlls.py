import pygame

class CheckBox:
    def __init__(self, x, y, wh, text, font):
        self.x = x
        self.y = y
        self.wh = wh
        self.text = text
        self.font = pygame.font.SysFont(font, 30)

        self.boolean = False

        self.counter = 0

    def update(self, screen, mouse_pos, mouse_press):
        label = self.font.render(self.text, 1, [255, 255, 255])
        screen.blit(label, (self.x, self.y))

        if self.boolean:
            pygame.draw.rect(screen, [255, 255, 255], (self.x + label.get_width() + 10, self.y, self.wh, self.wh), 0)
        else:
            pygame.draw.rect(screen, [255, 255, 255], (self.x + label.get_width() + 10, self.y, self.wh, self.wh), 1)

        if pygame.Rect(self.x + label.get_width() + 10, self.y, self.wh, self.wh).collidepoint(mouse_pos) and mouse_press[0] == 1 and self.counter <= 0:
            if self.boolean:
                self.boolean = False
            else:
                self.boolean = True

            self.counter = 15

        self.counter -= 1

class Button:
    def __init__(self, x, y, delay, text, font):
        self.x = x
        self.y = y
        self.delay = delay
        self.text = text
        self.font = pygame.font.SysFont(font, 30)

        self.label = self.font.render(self.text, 1, [0, 0, 0])

        self.counter = 0

        self.rect = pygame.Rect(self.x, self.y, self.label.get_width(), self.label.get_height())

    def update(self, screen, mouse_pos, mouse_press):
        pygame.draw.rect(screen, [255, 255, 255], self.rect, 0)

        screen.blit(self.label, (self.x, self.y))

        if self.rect.collidepoint(mouse_pos) and mouse_press[0] == 1 and self.counter <= 0:
            self.counter = self.delay
            return True
        else:
            self.counter -= 1
            return False
