
# Blitcrank-Bot

Discord bot interfacing riot games api to have information about ingame content.




## Tech Stack

**Python:** [Requests](https://docs.python-requests.org/en/latest/), [Discord.py](https://discordpy.readthedocs.io/en/stable/)

**API:** [Discord](https://discord.com/developers/docs/intro), [Riot Games](https://developer.riotgames.com/apis)


## Run Bliztcrank

Clone the project

```bash
  git clone https://github.com/AiresB/Blitzcrank
```

Go to the project directory

```bash
  cd Blitzcrank
```

Install dependencies

```bash
  pip install requirements.txt
```

Add Environements variables

```bash
  BOT_TOKEN={discord bot token}
  RIOT_TOKEN={Riot API token}
```

Start the bot

```bash
  python3 main.py
```


## Commands

- !add [pseudo] > register a player to the bot
- !remove [pseudo] > remove a registered pseudo
- !ranking  > show the ranking of the registered players
- !token [token] > change the riot token

## Authors

- [@AiresB](https://github.com/AiresB)
- [@Nicolas6272](https://github.com/Nicolas6272)

