import sys
from qsh.Agent import Agent

def main():
    agent = Agent()
    query = " ".join(sys.argv[1:])
    agent.get_message(query)

if __name__ == "__main__":
    main()


    