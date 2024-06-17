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
showNegativeAngles = False

numberOfTextEntrys = 6
xVectorTextEntrys = []
yVectorTextEntrys = []
magnitudeTextEntrys = []
angleTextEntrys = []
resultantVector = ""
#Create numerous text boxes for vector coordinate input
for i in range(numberOfTextEntrys):
    xVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250, 50 + i * 30), (100, 30)),
        manager=manager
    )
    xVectorTextEntrys.append(xVectorTextEntry)
for i in range(numberOfTextEntrys):
    yVectorTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250+110, 50 + i * 30), (100, 30)),
        manager=manager
    )
    yVectorTextEntrys.append(yVectorTextEntry)
for i in range(numberOfTextEntrys):
    magnitudeTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250+110+125, 50 + i * 30), (100, 30)),
        manager=manager
    )
    magnitudeTextEntrys.append(magnitudeTextEntry)
for i in range(numberOfTextEntrys):
    angleTextEntry = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
        relative_rect=pygame.Rect((250+125+110*2, 50 + i * 30), (100, 30)),
        manager=manager
    )
    angleTextEntrys.append(angleTextEntry)





while is_running:
    #Limit FPS to 60
    time_delta = clock.tick(60)/1000
    background.fill(pygame.Color('#FFFFFF'))
    drawText(background,"Resultant Vector:",(80,250),"black",20)
    for index, xVectorTextEntry in enumerate(xVectorTextEntrys):
        drawText(background,"Vector "+str(index+1),(xVectorTextEntry.rect.left-50,xVectorTextEntry.rect.centery),colours[index % len(colours)])
    #Write above the entry boxes
    drawText(background,"x",(xVectorTextEntrys[0].rect.centerx,xVectorTextEntrys[0].rect.top-10),"black",15)
    drawText(background,"y",(yVectorTextEntrys[0].rect.centerx,yVectorTextEntrys[0].rect.top-10),"black",15) 
    drawText(background,"Magnitude",(magnitudeTextEntrys[0].rect.centerx,magnitudeTextEntrys[0].rect.top-10),"black",15)
    drawText(background,"Angle (Degrees)",(angleTextEntrys[0].rect.centerx,angleTextEntrys[0].rect.top-10),"black",15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            graph.fill(pygame.Color('#FFFFFF'))
            drawAxes(graph,(0,0),2)
            vectors = []
            #Get user's input values
            if (event.ui_element in xVectorTextEntrys) or (event.ui_element in yVectorTextEntrys):
                for i in range(numberOfTextEntrys):
                    #Handle empty boxes
                    try:
                        vector = (float(xVectorTextEntrys[i].get_text()),float(yVectorTextEntrys[i].get_text()))
                        if vector != (0,0):
                            magnitudeTextEntrys[i].set_text(str(round(getMagnitude(vector),4)))
                            vectorAngle = getVectorAngle(vector)
                            if (vectorAngle < 0) and (not showNegativeAngles):
                                angleTextEntrys[i].set_text(str(round(degrees(vectorAngle)+360,4)))
                            else:
                                angleTextEntrys[i].set_text(str(round(degrees(vectorAngle),4)))
                            vectors.append(vector)
                    except ValueError:
                        pass
            elif (event.ui_element in magnitudeTextEntrys) or (event.ui_element in angleTextEntrys):
                for i in range(numberOfTextEntrys):
                    #Handle empty boxes
                    try:
                        vector = toXAndY(float(magnitudeTextEntrys[i].get_text()),radians(float(angleTextEntrys[i].get_text())))
                        if vector != (0,0):
                            xVectorTextEntrys[i].set_text(str((round(vector[0],4))))
                            yVectorTextEntrys[i].set_text(str((round(vector[1],4))))
                            vectors.append(vector)
                    except ValueError:
                        pass
            if vectors != []:
                scale = scaleVectorAddition(graph.get_width(),(0,0),*vectors)
                drawGridLines(graph,9,scale)
                drawAdditionOfVectors(graph,(0,0), 10,*vectors)
                resultantVector = toAlgebraicForm(addVectors(*vectors),2)
            else:
                drawGridLines(graph,9)
                
        manager.process_events(event)
    if debug:
        print(pygame.mouse.get_pos())
    #Draw border around graph surface
    pygame.draw.rect(graph,"black",(0,0,graph.get_width(),graph.get_height()),1)  
    drawText(background,resultantVector,(80,300),"black",20)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    window_surface.blit(graph,(175,250))
    manager.draw_ui(window_surface)

    pygame.display.update()