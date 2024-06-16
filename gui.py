import pygame
import pygame_gui
from main import *
from graphs import *


def drawText(surface: pygame.Surface, text: str, centre, color):
    arialFont = pygame.font.SysFont('Arial',25)
    text = arialFont.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = centre
    surface.blit(text,textRect)
screenWidth = 750
screenHeight = 650
pygame.init()

pygame.display.set_caption('Vector Calculator')
window_surface = pygame.display.set_mode((screenWidth, screenHeight))



#Main GUI surface
background = pygame.Surface((screenWidth, screenHeight))
background.fill(pygame.Color('#FFFFFF'))
#Graph surface
graph = pygame.Surface((300, 300))
graph.fill(pygame.Color('#FFFFFF'))
drawAxes(graph,(0,0),2)

manager = pygame_gui.UIManager((screenWidth, screenHeight))
clock = pygame.time.Clock()
is_running = True
debug = False

numberOfTextEntrys = 3
xVectorTextEntrys = []
yVectorTextEntrys = []

#Create numerous text boxes for vector coordinate input
for i in range(numberOfTextEntrys):
    xVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((150, 100 + i * 60), (100, 50)),
        manager=manager
    )
    xVectorTextEntrys.append(xVectorTextEntry)
for i in range(numberOfTextEntrys):
    yVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((150+150, 100 + i * 60), (100, 50)),
        manager=manager
    )
    yVectorTextEntrys.append(yVectorTextEntry)




while is_running:
    #Limit FPS to 60
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            graph.fill(pygame.Color('#FFFFFF'))
            drawAxes(graph,(0,0),2)
            vectors = []
            #Get user's input values
            for i in range(numberOfTextEntrys):
                #Handle empty boxes
                try:
                    vector = (float(xVectorTextEntrys[i].get_text()),float(yVectorTextEntrys[i].get_text()))
                    if vector != (0,0):
                        vectors.append((float(xVectorTextEntrys[i].get_text()),float(yVectorTextEntrys[i].get_text())))
                except ValueError:
                    pass
            if vectors != []:
                drawAdditionOfVectors(graph,(0,0), 10,*vectors)
        manager.process_events(event)  
    drawText(background,"x",(200,80),"black")
    drawText(background,"y",(350,80),"black") 
    if debug:
        print(pygame.mouse.get_pos())
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(graph,(150,300))
    manager.draw_ui(window_surface)

    pygame.display.update()