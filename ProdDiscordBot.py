import discord
import random

# api request for today's WC schedule
jokes = [
    "Why do Java programmers have to wear glasses? Because they don’t C#.",
    "Why did the programmer quit his job?\n\n Because he didn’t get arrays.",
    "An attractive String walks into a Java cafe, and sees an int, a boolean, and a double sitting at the bar.\nThe int walks up to her and says, “Hey baby, we can make interesting things happen with you around me.”  The String promptly slaps him, and the int walks away.\nThe boolean walks up to her and says, “Hey girl, you don’t know me yet, but you can trust that I’m your true love.”  The String rejects him as well, saying, “Not until I say so!” and the boolean walks away too.\nThe double tries next and says, “I may not be good with money, but I can definitely show you a good time.”  The String quickly declines and orders her drink.\nThe bartender asks casually asks, “Were those primitives bothering you?”\nThe String says, “Yeah, totally…. They’ve got no class!”",
    "3 Errors walk into a bar. The barman says, “Normally I’d Throw you all out, but tonight I’ll make an Exception.”",
]

# token for the discord bot
TOKEN = "MTE2MjQ0Mzc5NjcxODU3MTY1MA.GxGlQx.gKPnz_P05UlyZRYCV7eTdDdO6QGfPEJCP7GTFI"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# returns string of home and away teams
def getJoke():
    return random.choice(jokes)


# controlling bot messages based on user message.


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    # ignores the bot's messages
    if message.author == client.user:
        return

    if message.channel.name == "general":
        if user_message.lower() == "hey":
            await message.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == "!joke":
            await message.channel.send(f"{getJoke()}")
            return
        elif user_message.lower() == "!debug":
            await message.channel.send(
                f"Hi {username}. Please walk me through the code you are working on, step by step using the !step command."
            )
            return
        elif user_message.startswith("!step"):
            await message.channel.send(
                f"Interesting {username}, what is the next step?"
            )
            return


client.run(TOKEN)
