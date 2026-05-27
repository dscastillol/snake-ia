from game.snake import Snake
from game.food import Food
from game.maps import get_map

class Environment:

    def __init__(
            self,
            map_name
        ):

        self.map = get_map(
            map_name
        )

        self.snake = Snake()

        self.food = Food()

        self.food.position = (
            self.food.random_position(
                self.snake.body,
                self.map
            )
        )

        self.score = 0

        self.game_over = False

        self.steps_without_food = 0


    def step(
        self,
        action
    ):

        self.snake.change_direction(
            action
        )

        self.snake.move()

        self.steps_without_food += 1

        if self.snake.check_collision(
            self.map
        ):

            self.game_over = True

            return


        if self.snake.body[0] == self.food.position:

            self.snake.eat()

            self.steps_without_food = 0

            self.food.position = (

                self.food.random_position(
                    self.snake.body,
                    self.map
                )
            )

            self.score += 1

        if self.steps_without_food > 200:

            self.game_over = True

            return