from httpx import Client
import re

id = r'"id": (\d+),'
name = r'"name": "(.+)",'
skin_template = "https://raw.githubusercontent.com/AzurLaneTools/AzurLaneData/main/EN/ShareCfg/ship_skin_template.json"

client = Client()

id_list = re.findall(id, client.get(skin_template).text)
name_list = re.findall(name, client.get(skin_template).text)


def write(content):
    with open("skins.txt", "w+", encoding="utf-8") as f:
        for line in content:
            f.write(line + "\n")


content = [f"{i} - {v}" for i, v in zip(id_list, name_list)]

write(content)
