def select_agent():

    agents = {

        "1":"human",

        "2":"simple",

        "3":"bfs"

    }


    print()

    print("Choose Agent\n")

    print("1 Human")

    print("2 Simple")

    print("3 BFS")

    print()


    while True:

        choice = input(
            "Select option: "
        )


        if choice in agents:

            return agents[
                choice
            ]


        print(
            "Invalid option"
        )

def select_map():

    maps={

        "1":"empty",

        "2":"obstacles",

        "3":"random"

    }


    print()

    print("Choose Map\n")

    print("1 Empty")

    print("2 Obstacles")

    print("3 Random")


    while True:


        choice=input(
            "Select map: "
        )


        if choice in maps:

            return maps[
                choice
            ]


        print(
            "Invalid option"
        )