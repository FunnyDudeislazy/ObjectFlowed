# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import random
import webbrowser
from urllib.request import urlopen
import re

def get_latest_episode():
    url = "https://objectifiedcomic.com/archive"

    html = urlopen(url).read().decode("utf-8")

    episodes = re.findall(r"Ep\s+(\d+)\.", html)

    return max(map(int, episodes)) - 1

class ObjectFlowed(FlowLauncher):

    def query(self, query):
        parts = query.strip().split()

        if len(parts) == 1 and parts[0].isdigit() == True:
            episode = int(parts[0])

            return [{
                    "Title": f"Open Objectified Episode {episode}",
                    "SubTitle": f"https://objectifiedcomic.com/episode/{episode}",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_episode",
                        "parameters": [episode]
                    }
                }]

        elif len(parts) == 1 and parts[0] in ["random", "rand"]:
            latest_ep = get_latest_episode()
            random_episode = random.randint(1, latest_ep)

            return [{
                    "Title": f"Open Objectified Episode {random_episode}",
                    "SubTitle": f"https://objectifiedcomic.com/episode/{random_episode}",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_episode",
                        "parameters": [random_episode]
                    }
                }]

        elif len(parts) == 1 and parts[0] in ["latest"]:
            latest_ep = get_latest_episode()

            return [{
                    "Title": f"Latest Objectified Episode: {latest_ep}",
                    "SubTitle": f"https://objectifiedcomic.com/episode/{latest_ep}",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_episode",
                        "parameters": [latest_ep]
                    }
                }]

        elif len(parts) == 1 and parts[0] in ["first", "start"]:
            first_ep = 1

            return [{
                    "Title": f"Start Reading: {first_ep}",
                    "SubTitle": f"https://objectifiedcomic.com/episode/{first_ep}",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_episode",
                        "parameters": [first_ep]
                    }
                }]


        return []

    def open_episode(self, episode):
        url = f"https://objectifiedcomic.com/episode/{episode}"
        webbrowser.open(url)

if __name__ == "__main__":
    ObjectFlowed()
