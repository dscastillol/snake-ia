import random

from game.settings import *


class Food:

    def __init__(self):

        self.position = None


    def random_position(

        self,

        snake_body,

        game_map

    ):

        max_x = len(
            game_map[0]
        ) - 1

        max_y = len(
            game_map
        ) - 1


        while True:


            position=(

                random.randint(
                    1,
                    max_x-1
                ),

                random.randint(
                    1,
                    max_y-1
                )

            )


            x,y = position


            if position in snake_body:

                continue


            if game_map[
                y
            ][
                x
            ] == 1:

                continue


            return position