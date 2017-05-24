import pygame
pygame.init()
#pygame.joystick.get_count()
print(pygame.joystick.get_init())
print(pygame.joystick.get_count())
j1 = pygame.joystick.Joystick(1)
#print(type(j1))
j1.init()

print(j1.get_numbuttons())
while True:
    for x in range(j1.get_numbuttons()):
        if j1.get_button(x) == 0:
            print("FALSO FALSO FALSO")
        if j1.get_button(x) == 1:
            print("kadjlasjdlasjdlasjdklasjdajdlaskjdklasjdlask")
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
'''
pygame.joystick.init()
#pygame.joystick.Joystick.init()
joystick = pygame.joystick.Joystick(0)
button = joystick.get_button(0)
print(button)
#textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
'''
