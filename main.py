import os
import sys
import json
import time
import logging
import requests
import asyncio
import websockets
from threading import Thread
from keep_alive import keep_alive

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Fetch environment variables
status = os.getenv("status", "online")
custom_status = os.getenv("custom_status", "")
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

async def onliner(token, status):
    try:
        async with websockets.connect("wss://gateway.discord.gg/?v=9&encoding=json") as ws:
            logging.info("WebSocket connected")
            
            async for message in ws:
                payload = json.loads(message)
                if payload["op"] == 10:  # Hello
                    interval = payload["d"]["heartbeat_interval"] / 1000
                    
                    async def heartbeat():
                        while True:
                            await ws.send(json.dumps({"op": 1, "d": None}))
                            logging.debug("Heartbeat sent")
                            await asyncio.sleep(interval)
                    asyncio.create_task(heartbeat())

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
                    await ws.send(json.dumps(auth))
                    logging.info("Authentication sent")

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
                    await ws.send(json.dumps(cstatus))
                    logging.info("Custom status sent")

    except Exception as e:
        logging.error(f"Exception occurred: {e}")

async def run_onliner():
    os.system("clear")
    logging.info(f"Logged in as {username}#{discriminator} ({userid}).")
    while True:
        await onliner(usertoken, status)
        logging.info("Attempting to reconnect in 30 seconds")
        await asyncio.sleep(30)

keep_alive()

# Run the event loop
asyncio.run(run_onliner())
