# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import random
import webbrowser


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

        if len(parts) == 1 and parts[0] in ["random", "Random"]:
            episode = random.randint(1, 108)

            return [{
                    "Title": f"Open Objectified Episode {episode}",
                    "SubTitle": f"https://objectifiedcomic.com/episode/{episode}",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "open_episode",
                        "parameters": [episode]
                    }
                }]

        return []

    def open_episode(self, episode):
        url = f"https://objectifiedcomic.com/episode/{episode}"
        webbrowser.open(url)

if __name__ == "__main__":
    ObjectFlowed()
