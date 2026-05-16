import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !advice — random life advice
    @commands.command()
    async def advice(self, ctx):
        tips = [
            "Read one research paper per week. In a year, you'll know more than 99% of your peers.",
            "Build in public. Your journey inspires others more than your finished product.",
            "The fastest way to learn is to teach someone else.",
            "Your first project will be bad. Ship it anyway.",
            "Contribute to open source before you think you're ready.",
            "Talk to users before writing a single line of code.",
            "The best tech stack is the one you can ship with.",
            "Document your learnings. Future you will thank present you.",
            "Consistency beats intensity. 1 hour every day > 8 hours on weekends.",
        ]
        embed = discord.Embed(
            title="💡 Builder's Advice",
            description=random.choice(tips),
            color=0xFFC947
        )
        await ctx.send(embed=embed)

    # !challenge — random mini coding challenge
    @commands.command()
    async def challenge(self, ctx):
        challenges = [
            "Build a CLI tool that converts temperatures (C/F/K) in any language.",
            "Create a script that fetches and displays the top 5 trending GitHub repos today.",
            "Build a simple URL shortener that works in your terminal.",
            "Write a function that checks if a string is a valid palindrome.",
            "Create a markdown to HTML converter using only standard library.",
            "Build a pomodoro timer that runs in your terminal.",
            "Write a script that generates a random strong password.",
            "Create a simple REST API with one endpoint using any framework.",
            "Build a word frequency counter for any text file.",
        ]
        embed = discord.Embed(
            title="⚡ Mini Challenge",
            description=f"**Your challenge:**\n\n{random.choice(challenges)}\n\n*Share your solution in <#show-your-work>!*",
            color=0x39FF14
        )
        embed.set_footer(text="Complete it and share — earn XP + community recognition 🏆")
        await ctx.send(embed=embed)

    # !roast — friendly self-roast for devs
    @commands.command()
    async def roast(self, ctx, member: discord.Member = None):
        target = member or ctx.author
        roasts = [
            f"{target.mention} still uses `print()` for debugging. 🖨️",
            f"{target.mention}'s commit messages are just 'fixed stuff' and 'idk'. 💀",
            f"{target.mention} googles how to exit Vim every single time. 📖",
            f"{target.mention} writes TODO comments they never come back to. 📝",
            f"{target.mention} pushes directly to main. We don't talk about that. 😶",
            f"{target.mention} names variables like `x`, `x2`, and `x_final_v3`. 🤦",
        ]
        await ctx.send(random.choice(roasts))

async def setup(bot):
    await bot.add_cog(Fun(bot))