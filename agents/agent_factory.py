from agents.bfs_agent import BFSAgent
from agents.human_agent import HumanAgent
from agents.simple_agent import SimpleAgent


def create_agent(
    agent_name
):

    agents = {

        "human": HumanAgent(),

        "simple": SimpleAgent(),

        "bfs": BFSAgent()

    }


    return agents[
        agent_name
    ]