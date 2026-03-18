from google import genai
from qsh.Config import Config
import json
from pathlib import Path


class Request:
    def __init__(self):
        api_key = Config().api_key
        self.path = Path(__file__).resolve().parent / "data" / "config.json"
        self.client = genai.Client(api_key=api_key)

    def prompt(self: str) -> str:
        with self.path.open("r", encoding="utf-8") as f:
            config = json.load(f)
            return config["base_prompt"]

    
    def response(self, context: str) -> str:
        sys_prompt = self.prompt().format(context)
        response = self.client.models.generate_content(
        model="gemini-3-flash-preview", contents=sys_prompt
        )

        return response.text

