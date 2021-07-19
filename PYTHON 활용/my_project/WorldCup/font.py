# import pygame
# print(pygame.font.get_fonts())
import pygame
import pygame.freetype
pygame.init()
screen = pygame.display.set_mode((400, 600))
running = True
def word_wrap(surf, text, font, color=(0, 0, 0)):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height() + 2
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y
font = pygame.freetype.SysFont('Arial', 20)
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    word_wrap(screen, 'Hey, this is a very long text! Maybe it is too long... We need more than one line!', font)
    pygame.display.update()