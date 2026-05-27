import pygame

from game.environment import Environment

from game.settings import *

from agents.bfs_agent import BFSAgent

from game.renderer import render

from game.input_handler import process_events

from agents.agent_factory import create_agent

from menu import (

    select_agent,

    select_map

)


pygame.init()


screen = pygame.display.set_mode(
    (WIDTH,HEIGHT)
)

clock = pygame.time.Clock()

font = pygame.font.SysFont(
    None,
    30
)


map_name = select_map()

env = Environment(
    map_name
)

agent_name = select_agent()

agent = create_agent(
    agent_name
)
running = True

current_fps = FPS


while running:


    # -------------------
    # EVENTS
    # -------------------

    running,current_fps = process_events(
        current_fps
    )


    # -------------------
    # AGENT
    # -------------------

    action = agent.get_action(
        env
    )


    # -------------------
    # UPDATE WORLD
    # -------------------

    env.step(
        action
    )


    if env.game_over:

        running=False


    # -------------------
    # RENDER
    # -------------------

    render(

        screen,

        env,

        font,

        current_fps,

        agent_name,

        agent

    )


    pygame.display.update()


    clock.tick(
        current_fps
    )


pygame.quit()