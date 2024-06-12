import pygame
import pygame_gui
from main import *
from graphs import *

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

manager = pygame_gui.UIManager((screenWidth, screenHeight))
calculateButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (150, 50)),text='Calculate Vectors',manager=manager,anchors={'centre': 'centre'})
clock = pygame.time.Clock()
is_running = True

numberOfTextEntrys = 3
xVectorTextEntrys = []
yVectorTextEntrys = []

#Create numerous text boxes for vector coordinate input
for i in range(numberOfTextEntrys):
    xVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((350, 0 + i * 60), (100, 50)),
        manager=manager
    )
    xVectorTextEntrys.append(xVectorTextEntry)
for i in range(numberOfTextEntrys):
    yVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((500, 0 + i * 60), (100, 50)),
        manager=manager
    )
    yVectorTextEntrys.append(yVectorTextEntry)


while is_running:
    #Limit FPS to 60
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == calculateButton:
                graph.fill(pygame.Color('#FFFFFF'))
                drawAxes(graph,(0,0))
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
                    drawAdditionOfVectors(graph,(0,0),-1,*vectors)

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(graph,(150,300))
    manager.draw_ui(window_surface)

    pygame.display.update()