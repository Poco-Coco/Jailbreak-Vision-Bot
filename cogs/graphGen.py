import nextcord
from nextcord.ext import commands
import random
import json
import os
import matplotlib.pyplot as plt
import json

emcolor = 0x2596BE
footertext = "Raph Manager | Graph Generator"


class graphGen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog: graph.py is loaded!")

    @commands.command()
    async def structure(self, ctx, GraphTransparent=False):
        if str(ctx.message.attachments) == "[]":
            await ctx.send("There is no attachments.")
        else:
            for attachment in ctx.message.attachments:
                try:
                    plt.rcParams["figure.figsize"] = (16, 9)
                    plt.ylim([0, 500])

                    await attachment.save("./json/" + attachment.filename)
                    f = open("./json/" + attachment.filename)
                    data = json.load(f)

                    graphName = (
                        data["Settings"]["Test Mode"]
                        + " "
                        + data["Settings"]["Vehicle Name"]
                    )

                    timeLine = []
                    speedLine = []

                    index = 0
                    for v in data["SpeedTest"]:
                        timeLine.append(int(data["SpeedTest"][int(index)]["Time"]))
                        speedLine.append(int(data["SpeedTest"][int(index)]["Speed"]))
                        index += 1

                    x = timeLine
                    y = speedLine

                    colorlist = ["r", "b", "y", "c", "g"]
                    plt.plot(x, y, color=random.choice(colorlist))

                    plt.xlabel("Time - Seconds")
                    plt.ylabel("Speed - Mph")

                    plt.grid(False)

                    plt.savefig("./graph.png", transparent=GraphTransparent, dpi=500)
                    plt.clf()

                    await ctx.send(file=nextcord.File("./graph.png"))

                    os.remove("./graph.png")
                    os.remove("./json/" + attachment.filename)
                except Exception as e:
                    await ctx.send(f"Exception occured! ```{e}```")


async def setup(bot):
    bot.add_cog(graphGen(bot))
