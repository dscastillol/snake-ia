from game.settings import *
import random



def create_empty_map():

    grid=[]


    for y in range(
        GRID_HEIGHT
    ):

        row=[]


        for x in range(
            GRID_WIDTH
        ):


            if (

                x==0
                or y==0

                or x==GRID_WIDTH-1

                or y==GRID_HEIGHT-1

            ):

                row.append(
                    1
                )

            else:

                row.append(
                    0
                )


        grid.append(
            row
        )


    return grid

from game.settings import *


def create_obstacle_map():

    grid = create_empty_map()


    obstacles = [

        (8,5),
        (8,6),
        (8,7),

        (15,10),
        (16,10),
        (17,10),

        (20,4),
        (20,5),
        (20,6)

    ]


    for x,y in obstacles:

        grid[y][x] = 1


    return grid

def create_random_map(

    obstacle_rate=0.1

):

    grid=create_empty_map()


    for y in range(
        1,
        GRID_HEIGHT-1
    ):

        for x in range(
            1,
            GRID_WIDTH-1
        ):


            if random.random() < obstacle_rate:

                grid[y][x]=1


    return grid

MAPS={

    "empty":create_empty_map,

    "obstacles":create_obstacle_map,

    "random":create_random_map

}

def get_map(

    map_name

):

    return MAPS[
        map_name
    ]()