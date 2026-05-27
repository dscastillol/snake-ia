import pygame

human_action = None

def get_human_action():

    return human_action

def process_events(

    current_fps

):

    running = True


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        elif event.type == pygame.KEYDOWN:

            global human_action

            if event.key == pygame.K_UP:

                human_action = (0,-1)

            elif event.key == pygame.K_DOWN:

                human_action = (0,1)

            elif event.key == pygame.K_LEFT:

                human_action = (-1,0)

            elif event.key == pygame.K_RIGHT:

                human_action = (1,0)

            if event.key == pygame.K_SPACE:

                current_fps *= 2


            elif event.key == pygame.K_LSHIFT:

                current_fps = max(

                    1,

                    current_fps // 2

                )


    return (

        running,

        current_fps

    )