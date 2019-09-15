import pygame

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 400
FPS = 60

# Create the screen we will draw to
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG!')

# Set up the clock which will calculate FPS
clock = pygame.time.Clock()

########################
# Define variables here:
########################


########################
# Define functions here:
########################



# Main game loop
done = False
while not done:
    # FPS calculations
    clock.tick(FPS)

    # Quit when the X button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # fills the screen with black
    screen.fill((0, 0, 0))

    #################################
    # Write the rest of the code here:
    #################################





    # This displays whatever you have drawn to the screen
    # This should ALWAYS be the VERY LAST THING in this while loop
    pygame.display.flip()
    

pygame.quit()
