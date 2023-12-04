import discord
import random
import time
from time import gmtime, strftime
from discord.ext import commands, tasks
import asyncio

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
bot = commands.Bot(command_prefix="!", intents=intents)
ctxBackground = None


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


def getJoke():
    return random.choice(jokes)


@tasks.loop(seconds=1500)
async def work_timer():
    # This function will be called every TIMER_INTERVAL seconds
    if work_timer.current_loop >= 4:
        print("work stopping")
        work_timer.stop()
    if work_timer.current_loop > 0:
        global ctxBackground
        if ctxBackground:
            print("one loop of work " + strftime("%H:%M:%S", gmtime()))
            await ctxBackground.send(
                "Background timer: 25 minutes have passed. Break time!"
            )
        if not break_timer.is_running():
            print("break starting " + strftime("%H:%M:%S", gmtime()))
            break_timer.start()


@tasks.loop(seconds=300)
async def break_timer():
    # This function will be called every TIMER_INTERVAL seconds
    # stops after one loop
    global ctxBackground
    if ctxBackground and break_timer.current_loop == 1:
        await ctxBackground.send(
            "Background timer: 5 minutes have passed. Back to work."
        )
        print("break stopping " + strftime("%H:%M:%S", gmtime()))
        break_timer.stop()


# Add your commands here
@bot.command()
async def joke(ctx):
    await ctx.send(f"{getJoke()}")


@bot.command()
async def debug(ctx):
    await ctx.send(
        f"Hi {ctx.author}. Please walk me through the code you are working on, step by step using the !step command."
    )


@bot.command()
async def timer(ctx):
    await ctx.send("Okay, starting the ProductivityTimer!")
    global ctxBackground
    ctxBackground = ctx

    work_timer.start()


bot.run(TOKEN)
