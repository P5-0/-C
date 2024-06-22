import os
import sys
import json
import time
import requests
import websocket
from keep_alive import keep_alive

status = os.getenv("status")  # online/dnd/idle
custom_status = os.getenv("custom_status")  # If you don't need a custom status on your profile, just put "" instead of "youtube.com/@SealedSaucer"
emoji_name = os.getenv("emoji_name")  # Name of the emoji to display
emoji_id = os.getenv("emoji_id")  # ID of the emoji, if it's a custom emoji
emoji_animated = os.getenv("emoji_animated", "false").lower() == "true"  # Whether the emoji is animated

usertoken = os.getenv("token")
if not usertoken:
    print("[ERROR] Please add a token inside Secrets.")
    sys.exit()

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers)
if validate.status_code != 200:
    print("[ERROR] Your token might be invalid. Please check it again.")
    sys.exit()

userinfo = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def onliner(token, status):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    start = json.loads(ws.recv())
    heartbeat = start["d"]["heartbeat_interval"]
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "Windows",
                "$browser": "Discord Client",
                "$device": "Desktop",
            },
            "presence": {"status": status, "afk": False},
        },
        "s": None,
        "t": None,
    }
    ws.send(json.dumps(auth))

    activities = {
        "type": 4,
        "state": custom_status,
        "name": "Custom Status",
        "id": "custom",
    }
    if emoji_name:
        activities["emoji"] = {"name": emoji_name, "animated": emoji_animated}
        if emoji_id:
            activities["emoji"]["id"] = emoji_id
    
    cstatus = {
        "op": 3,
        "d": {
            "since": 0,
            "activities": [activities],
            "status": status,
            "afk": False,
        },
    }
    
    ws.send(json.dumps(cstatus))
    online = {"op": 1, "d": "None"}
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))

def run_onliner():
    os.system("clear")
    print(f"Logged in as {username}#{discriminator} ({userid}).")
    while True:
        onliner(usertoken, status)
        time.sleep(30)

keep_alive()
run_onliner()
