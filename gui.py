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
graph = pygame.Surface((400, 400))
graph.fill(pygame.Color('#FFFFFF'))
drawAxes(graph,(0,0),2)
drawGridLines(graph,9)

manager = pygame_gui.UIManager((screenWidth, screenHeight))
clock = pygame.time.Clock()
is_running = True
debug = False

numberOfTextEntrys = 6
xVectorTextEntrys = []
yVectorTextEntrys = []

#Create numerous text boxes for vector coordinate input
for i in range(numberOfTextEntrys):
    xVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250, 50 + i * 30), (100, 30)),
        manager=manager
    )
    drawText(background,"Vector "+str(i+1),(xVectorTextEntry.rect.left-50,xVectorTextEntry.rect.centery),colours[i % len(colours)])
    xVectorTextEntrys.append(xVectorTextEntry)
for i in range(numberOfTextEntrys):
    yVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250+150, 50 + i * 30), (100, 30)),
        manager=manager
    )
    yVectorTextEntrys.append(yVectorTextEntry)
#Write above the entry boxes
drawText(background,"x",(xVectorTextEntrys[0].rect.centerx,xVectorTextEntrys[0].rect.top-20),"black")
drawText(background,"y",(yVectorTextEntrys[0].rect.centerx,yVectorTextEntrys[0].rect.top-20),"black") 



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
                scale = scaleVectorAddition(graph.get_width(),(0,0),*vectors)
                drawGridLines(graph,9,scale)
                drawAdditionOfVectors(graph,(0,0), 10,*vectors)
            else:
                drawGridLines(graph,9)
                
        manager.process_events(event)
    #Draw border around graph surface
    pygame.draw.rect(graph,"black",(0,0,graph.get_width(),graph.get_height()),1)  
    if debug:
        print(pygame.mouse.get_pos())
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(graph,(175,250))
    manager.draw_ui(window_surface)

    pygame.display.update()