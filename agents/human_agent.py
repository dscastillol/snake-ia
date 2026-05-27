from game.input_handler import get_human_action


class HumanAgent:


    def get_action(
        self,
        env
    ):

        action = get_human_action()


        if action is None:

            return env.snake.direction


        return action