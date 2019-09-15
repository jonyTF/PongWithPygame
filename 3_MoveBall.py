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
player_speed = 10
player1_y = 0
player2_y = 0

ball_x = WIDTH/2
ball_y = HEIGHT/2
ball_speed_x = -3
ball_speed_y = 1

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: # If the W key is pressed
        player1_y -= player_speed
    elif keys[pygame.K_s]: # If the S key is pressed
        player1_y += player_speed
    
    if keys[pygame.K_UP]: # If the UP ARROW key is pressed
        player2_y -= player_speed
    elif keys[pygame.K_DOWN]: # If the DOWN ARROW key is pressed
        player2_y += player_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Draw Player 1
    player1_rect = [0, player1_y, 10, 80]
    pygame.draw.rect(screen, (255, 255, 255), player1_rect)

    # Draw Player 2
    player2_rect = [WIDTH-10, player2_y, 10, 80]
    pygame.draw.rect(screen, (255, 255, 255), player2_rect)

    # Draw the ball
    ball_rect = [ball_x-5, ball_y-5, 10, 10]
    pygame.draw.ellipse(screen, (255, 255, 255), ball_rect)

    # This displays whatever you have drawn to the screen
    # This should ALWAYS be the VERY LAST THING in this while loop
    pygame.display.flip()
    

pygame.quit()
