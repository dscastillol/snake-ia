import pygame

from game.settings import *


def draw_border(screen):

    for x in range(GRID_WIDTH):

        # borde superior
        pygame.draw.rect(
            screen,
            (100,100,100),
            (
                x*CELL_SIZE,
                0,
                CELL_SIZE,
                CELL_SIZE
            )
        )

        # borde inferior
        pygame.draw.rect(
            screen,
            (100,100,100),
            (
                x*CELL_SIZE,
                (GRID_HEIGHT-1)*CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
        )


    for y in range(GRID_HEIGHT):

        # izquierda
        pygame.draw.rect(
            screen,
            (100,100,100),
            (
                0,
                y*CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
        )

        # derecha
        pygame.draw.rect(
            screen,
            (100,100,100),
            (
                (GRID_WIDTH-1)*CELL_SIZE,
                y*CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
        )

import pygame

from game.settings import *


def render(

    screen,

    env,

    font,

    current_fps,

    agent_name, 

    agent

):

    screen.fill(
        (0,0,0)
    )


    for y,row in enumerate(
        env.map
    ):

        for x,cell in enumerate(
            row
        ):

            if cell == 1:

                pygame.draw.rect(

                    screen,

                    (100,100,100),

                    (

                        x*CELL_SIZE,

                        y*CELL_SIZE,

                        CELL_SIZE,

                        CELL_SIZE

                    )

                )


    # score

    score_text = font.render(

        f"Score: {env.score}",

        True,

        (255,255,255)

    )

    screen.blit(
        score_text,
        (20,20)
    )


    # fps

    fps_text = font.render(

        f"FPS: {current_fps}",

        True,

        (255,255,255)

    )

    screen.blit(
        fps_text,
        (20,50)
    )

    #current agent

    agent_text = font.render(

        f"Agent: {agent_name}",

        True,

        (255,255,255)

    )

    screen.blit(
        agent_text,
        (20,80)
    )

    # food

    pygame.draw.rect(

        screen,

        (255,0,0),

        (

            env.food.position[0]*CELL_SIZE,

            env.food.position[1]*CELL_SIZE,

            CELL_SIZE,

            CELL_SIZE

        )
    )

    for x,y in getattr(
        agent,
        "current_path",
        []
    ):

        pygame.draw.rect(

            screen,

            (180,0,255),

            (

                x*CELL_SIZE,

                y*CELL_SIZE,

                CELL_SIZE,

                CELL_SIZE

            ),

            1
        )

    # snake

    for index,(x,y) in enumerate(
        env.snake.body
    ):


        color = (0,255,0)


        # cabeza

        if index == 0:

            color = (
                0,
                150,
                255
            )


        # cola

        elif index == len(
            env.snake.body
        ) - 1:

            color = (
                255,
                255,
                0
            )


        pygame.draw.rect(

            screen,

            color,

            (

                x*CELL_SIZE,

                y*CELL_SIZE,

                CELL_SIZE,

                CELL_SIZE

            )
        )