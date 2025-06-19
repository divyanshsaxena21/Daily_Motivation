import requests
import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def get_inspirational_article(query):
    """Search for an inspirational article using Tavily API."""
    if not TAVILY_API_KEY:
        return None

    try:
        headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
        payload = {
            "query": query,
            "search_depth": "basic",
            "max_results": 1
        }

        response = requests.post("https://api.tavily.com/search", json=payload, headers=headers)
        data = response.json()

        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]["url"]
        return None

    except Exception as e:
        print("Tavily error:", e)
        return None
