class SimpleAgent:


    def get_action(
        self,
        env
    ):

        state = env.snake.get_state(
            env.food,
            env.map
        )


        (

            food_left,
            food_right,

            food_up,
            food_down,


            danger_left,
            danger_right,

            danger_up,
            danger_down,


            moving_left,
            moving_right,

            moving_up,
            moving_down

        ) = state


        # intentar ir hacia comida

        if food_right and not danger_right:

            return (1,0)


        if food_left and not danger_left:

            return (-1,0)


        if food_up and not danger_up:

            return (0,-1)


        if food_down and not danger_down:

            return (0,1)


        # fallback


        possible=[]


        if not danger_right:

            possible.append(
                (1,0)
            )


        if not danger_left:

            possible.append(
                (-1,0)
            )


        if not danger_up:

            possible.append(
                (0,-1)
            )


        if not danger_down:

            possible.append(
                (0,1)
            )


        if possible:

            return possible[0]


        return env.snake.direction