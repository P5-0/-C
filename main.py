import os
import sys
import json
import time
import requests
import websocket
import logging
from keep_alive import keep_alive

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Fetch environment variables
status = os.getenv("status", "online")  # default to 'online' if not set
custom_status = os.getenv("custom_status", "")  # default to empty string if not set
emoji_name = os.getenv("emoji_name", "")
emoji_id = os.getenv("emoji_id", "")
emoji_animated = os.getenv("emoji_animated", "false").lower() == "true"

usertoken = os.getenv("token")
if not usertoken:
    logging.error("Please add a token inside Secrets.")
    sys.exit()

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

# Validate token
validate = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers)
if validate.status_code != 200:
    logging.error("Your token might be invalid. Please check it again.")
    sys.exit()

userinfo = validate.json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def on_message(ws, message):
    logging.debug(f"Received message: {message}")

def on_error(ws, error):
    logging.error(f"Encountered error: {error}")

def on_close(ws, close_status_code, close_msg):
    logging.info(f"Closed connection: {close_status_code} - {close_msg}")

def on_open(ws):
    logging.info("Opened connection")

def onliner(token, status):
    try:
        ws = websocket.WebSocketApp(
            "wss://gateway.discord.gg/?v=9&encoding=json",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close
        )
        ws.on_open = on_open
        
        def run(*args):
            start = json.loads(ws.recv())
            heartbeat = start["d"]["heartbeat_interval"]
            auth = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": "Windows 10",
                        "$browser": "Google Chrome",
                        "$device": "Windows",
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
            
            while True:
                time.sleep(heartbeat / 1000)
                ws.send(json.dumps(online))

        ws.run_forever()
    
    except websocket.WebSocketBadStatusException as e:
        logging.error(f"WebSocket failed with status: {e.status_code} - {e}")

def run_onliner():
    os.system("clear")
    logging.info(f"Logged in as {username}#{discriminator} ({userid}).")
    while True:
        onliner(usertoken, status)
        time.sleep(30)

keep_alive()
run_onliner()
