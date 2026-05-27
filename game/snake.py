class Snake:

    def __init__(self):

        self.body = [

            (10,10),

            (9,10),

            (8,10)

        ]

        self.direction = (1,0)

        self.grow = False


    def move(self):

        head_x,head_y = self.body[0]

        dx,dy = self.direction


        new_head=(

            head_x+dx,

            head_y+dy

        )


        self.body.insert(

            0,

            new_head

        )


        if not self.grow:

            self.body.pop()

        else:

            self.grow=False


    def eat(self):

        self.grow=True


    def change_direction(

        self,

        direction

    ):

        opposites={

            (1,0):(-1,0),

            (-1,0):(1,0),

            (0,1):(0,-1),

            (0,-1):(0,1)

        }


        if direction != opposites[
            self.direction
        ]:

            self.direction=direction


    def check_collision(

        self,

        game_map

    ):

        head_x,head_y = self.body[0]


        # fuera del mapa

        if (

            head_x < 0
            or head_x >= len(game_map[0])

            or head_y < 0
            or head_y >= len(game_map)

        ):

            return True


        # pared

        if game_map[
            head_y
        ][
            head_x
        ] == 1:

            return True


        # cuerpo

        if self.body[0] in self.body[1:]:

            return True


        return False


    # -------------------
    # Helpers
    # -------------------


    def get_head(self):

        return self.body[0]


    def danger_at(

        self,

        position,

        game_map

    ):

        x,y = position


        # fuera del mapa

        if (

            x < 0
            or x >= len(game_map[0])

            or y < 0
            or y >= len(game_map)

        ):

            return True


        # pared

        if game_map[
            y
        ][
            x
        ] == 1:

            return True


        # cuerpo

        if position in self.body:

            return True


        return False


    def get_state(

        self,

        food,

        game_map

    ):

        head_x,head_y = self.get_head()


        left=(

            head_x-1,

            head_y

        )


        right=(

            head_x+1,

            head_y

        )


        up=(

            head_x,

            head_y-1

        )


        down=(

            head_x,

            head_y+1

        )


        dx,dy=self.direction


        state=[


            # food

            food.position[0] < head_x,

            food.position[0] > head_x,

            food.position[1] < head_y,

            food.position[1] > head_y,


            # dangers

            self.danger_at(
                left,
                game_map
            ),

            self.danger_at(
                right,
                game_map
            ),

            self.danger_at(
                up,
                game_map
            ),

            self.danger_at(
                down,
                game_map
            ),


            # direction

            dx == -1,

            dx == 1,

            dy == -1,

            dy == 1

        ]


        return state