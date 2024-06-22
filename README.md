![GitHub all releases](https://img.shields.io/github/downloads/P5-0/V/total)
![GitHub language count](https://img.shields.io/github/languages/count/P5-0/V)
![GitHub top language](https://img.shields.io/github/languages/top/P5-0/V?color=yellow).
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/P5-0/V)
![GitHub forks](https://img.shields.io/github/forks/P5-0/V?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/P5-0/V?style=social)
****

# Updated version with the ability to use animated and static emojis
##This bot sets a custom status on your Discord account with an optional emoji. It supports both regular and custom emojis.

**** 
Forked from https://github.com/SealedSaucer/Online-Forever/blob/main/main.py
**** 
Discord Custom Status bot 24/7 Can be deployed on Render.
**** 
> Getting token:

- 1 Open Discord on Browser, F12 or ctrl+shift+i. Go to Network tab. 
- 2 Click on some server or chat. Find 'Science' on the Network.
- 3 Find Authorzation. This is your `token`
> Or just paste this code into the console after opening developer mode and copy the token between  '  Your Token  '
```sh
(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
```
---
| Ａｎ Ｉｍｐｏｒｔａｎｔ Ｎｏｔｅ |
| :---- |
---
- [x] *__It is preferable to use a session token other than your actual session token on the browser or application to ensure stable performance and that Discord does not block the account, you can do this by opening Discord in a private browsing window, for example on “brave due to its safest” and taking the token from it and then closing it after the moment the bot is created on render__*


- [ ] 𝐖𝐡𝐞𝐧 𝐲𝐨𝐮 𝐫𝐞𝐚𝐝 𝐢𝐭, 𝐦𝐚𝐫𝐤 𝐢𝐭 ``done`` 𝐬𝐢𝐠𝐧.  
---
**** 


```diff
- # ＲＥＮＤＥＲ ＳＩＤＥ :
```
**** 

- Link to the site: `https://render.com/`
****

- Installation command: `pip install -r requirements.txt`
- Run command: `python main.py`
****
                               
                                     𝓲𝓶𝓹𝓸𝓻𝓽𝓪𝓷𝓽 𝓻𝓮𝓶𝓪𝓻𝓴𝓼
****
## Prerequisites

- A Discord account
- Discord user token
- Render account for deployment
****

## Environment Variables

Set the following environment variables in Render:

- `status`: Desired status (`online`, `dnd`, `idle`)
- `custom_status`: Custom status text
- `emoji_name`: Name of the emoji (e.g., `🪓` or `YYYY` for custom emoji `<a:YYYY:1247965345034010728>`)
- `emoji_id`: ID of the emoji if it's a custom emoji (e.g., `1247965345034010728`)
- `emoji_animated`: `True` if the custom emoji is animated; otherwise `False`
- `token`: Your Discord user token

```diff
+ # 𝑹𝒆𝒈𝒖𝒍𝒂𝒓 𝑬𝒎𝒐𝒋𝒊 𝑬𝒙𝒂𝒎𝒑𝒍𝒆 :
```

For a regular emoji like 🪓:

- `status`: `online`
- `custom_status`: `Feeling like a king`
- `emoji_name`: `🪓`
- `emoji_id`: (leave blank)
- `emoji_animated`: (leave blank or set to `False`)
- `token`: (your Discord user token)

```diff
+ # 𝑪𝒖𝒔𝒕𝒐𝒎 𝑬𝒎𝒐𝒋𝒊 𝑬𝒙𝒂𝒎𝒑𝒍𝒆 :
```

For a custom emoji like <a:YYYY:1247965345034010728>:

- `status`: `online`
- `custom_status`: `Feeling like a king`
- `emoji_name`: `:YYYY:`
- `emoji_id`: `1247965345034010728`
- `emoji_animated`: `True`
- `token`: (your Discord user token)
****

## Deployment on Render

1. Create a new Web Service on Render.
2. Connect your GitHub repository or upload your code.
3. Set the environment variables as described above.
4. Deploy your service.
****

The bot will automatically set your Discord status with the specified custom status and emoji.

## Keep Alive

The script includes a keep_alive function to ensure the bot remains active. This is especially useful for hosting environments that might otherwise time out.
## Use sites like `https://cron-job.org/` or `https://uptimerobot.com/` to make it work 24-7
****

## Running Locally

To run the bot locally, ensure you have Python and the required dependencies installed. Set the environment variables in your local environment and run the script:

``python3 main.py``
****
```sh
### The hard way, but it gives you all the information you need about anything including emojis and lets you know even the id of regular or animated emojis

- 1 Open Discord on Browser, F12 or ctrl+shift+i . Click on  Pick an elemen <it has an icon that looks like a Cursor on a screen>. 

> Select the emoji by clicking on it after you have already sent the emoji in a chat message. And double-click on it. 
> It will give you all the information you need about the emoji in a very detailed way.
```

****
****


```diff
@@ If you have any issues, contact me. @@
```



