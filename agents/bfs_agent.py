from collections import deque

from game.settings import *


class BFSAgent:
    
    def __init__(self):

        self.current_path = []


    def get_neighbors(
        self,
        position
    ):

        x,y = position

        return [

            (x+1,y),
            (x-1,y),

            (x,y+1),
            (x,y-1)

        ]


    def find_path(

        self,

        start,

        goal,

        obstacles,

        game_map

    ):

        queue = deque()

        queue.append(
            (
                start,
                []
            )
        )

        visited=set()


        while queue:

            current,path = queue.popleft()


            if current==goal:

                return path


            if current in visited:

                continue


            visited.add(
                current
            )


            for neighbor in self.get_neighbors(
                current
            ):

                x,y = neighbor


                if (

                    x < 0

                    or x >= len(game_map[0])

                    or y < 0

                    or y >= len(game_map)

                ):

                    continue

                if game_map[
                    y
                ][
                    x
                ] == 1:

                    continue

                if neighbor in obstacles:

                    continue


                queue.append(

                    (

                        neighbor,

                        path+[neighbor]

                    )
                )


        return []



    def get_action(
        self,
        env
    ):

        snake = env.snake

        food = env.food


        obstacles = set(
            snake.body[:-1]
        )


        food_path = self.find_path(

            snake.body[0],

            food.position,

            obstacles,

            env.map

        )

        safe_path = []


        if food_path:

            simulated_body = self.simulate_body(

                snake.body,

                food_path

            )


            if self.can_reach_tail(

                simulated_body,

                env.map

            ):

                safe_path = food_path
        
        if not safe_path:

            tail_target = snake.body[-1]

            safe_path = self.find_path(

                snake.body[0],

                tail_target,

                obstacles,

                env.map

            )

        self.current_path = safe_path
        path = safe_path

        if not path:

            return snake.direction


        next_cell = path[0]


        head_x,head_y = snake.body[0]

        nx,ny = next_cell


        return (

            nx-head_x,

            ny-head_y

        )
    
    def simulate_body(

        self,

        body,

        path

    ):

        simulated = list(
            body
        )


        for step in path:

            simulated.insert(
                0,
                step
            )

            simulated.pop()


        return simulated
    
    def can_reach_tail(

        self,

        body,

        game_map

    ):

        head = body[0]

        tail = body[-1]


        obstacles = set(
            body[:-1]
        )


        path = self.find_path(

            head,

            tail,

            obstacles,

            game_map

        )


        return len(
            path
        ) > 0