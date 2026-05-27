from agents.agent_factory import create_agent

from game.environment import Environment


# ------------------
# CONFIG
# ------------------

AGENT_NAME = "bfs"

MAP_NAME = "random"

N_GAMES = 10

MAX_STEPS = 5000


# ------------------
# RUN BENCHMARK
# ------------------

scores=[]


for game in range(
    N_GAMES
):

    env = Environment(
        MAP_NAME
    )

    agent = create_agent(
        AGENT_NAME
    )

    steps = 0


    while (

        not env.game_over

        and

        steps < MAX_STEPS

    ):


        action = agent.get_action(
            env
        )


        env.step(
            action
        )


        steps += 1


    scores.append(
        env.score
    )


    print(

        f"Game {game+1}"

        f" | Score: {env.score}"

        f" | Steps: {steps}"

    )


# ------------------
# RESULTS
# ------------------

average = sum(
    scores
) / len(
    scores
)


print()

print(
    "===== RESULTS ====="
)

print(
    "Agent:",
    AGENT_NAME
)

print(
    "Map:",
    MAP_NAME
)

print(
    "Games:",
    N_GAMES
)

print(
    "Average Score:",
    round(
        average,
        2
    )
)

print(
    "Max Score:",
    max(
        scores
    )
)

print(
    "Min Score:",
    min(
        scores
    )
)