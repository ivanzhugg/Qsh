from .Request import Request

class Agent:
    def __init__(self) -> None:
        self.req = Request()
        return

    def get_message(self, query: str) -> None:

        try:
            response = self.req.response(query)
            print(response)
        except:
            print("Error with API")
