import discord
from discord.ext import commands
import random

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !help — custom help menu
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="📋 [Community Name] Bot — Commands",
            color=0x6C63FF
        )
        embed.add_field(
            name="📚 Resources",
            value="`!resources` — Learning resources\n`!roadmap [topic]` — Get a roadmap\n`!events` — Upcoming events",
            inline=False
        )
        embed.add_field(
            name="🚀 Community",
            value="`!ship` — How to share your work\n`!roles` — Role guide\n`!leaderboard` — Top contributors",
            inline=False
        )
        embed.add_field(
            name="🎯 Fun",
            value="`!joke` — Random dev joke\n`!advice` — Random advice\n`!inspire` — Motivational quote",
            inline=False
        )
        embed.add_field(
            name="🛡️ Moderation (Mods only)",
            value="`!warn` `!mute` `!unmute` `!kick` `!ban` `!clear`",
            inline=False
        )
        embed.set_footer(text="Type !command for details. Build What Matters 🔥")
        await ctx.send(embed=embed)

    # !resources command
    @commands.command()
    async def resources(self, ctx):
        embed = discord.Embed(
            title="📚 Resource Hub",
            color=0x6C63FF
        )
        embed.add_field(name="🐣 Beginners", value="[freeCodeCamp](https://freecodecamp.org)\n[CS50](https://cs50.harvard.edu)\n[The Odin Project](https://theodinproject.com)", inline=True)
        embed.add_field(name="🧱 Roadmaps", value="[roadmap.sh](https://roadmap.sh)\n[Web Dev](https://roadmap.sh/frontend)\n[Backend](https://roadmap.sh/backend)", inline=True)
        embed.add_field(name="🤖 AI/ML", value="[fast.ai](https://fast.ai)\n[Papers with Code](https://paperswithcode.com)", inline=True)
        embed.add_field(name="🚀 Startups", value="[YC Library](https://ycombinator.com/library)\n[Paul Graham](http://paulgraham.com/articles.html)", inline=False)
        await ctx.send(embed=embed)

    # !events command
    @commands.command()
    async def events(self, ctx):
        embed = discord.Embed(
            title="📅 Recurring Events",
            description=(
                "🔬 **Paper Discussion** — Every Wed @ 7PM IST\n"
                "💻 **Code & Chill** — Every Thu @ 9PM IST\n"
                "⚡ **Weekly Challenge** — Drops every Fri @ 6PM IST\n\n"
                "Check <#event-alerts> for upcoming special events!"
            ),
            color=0xFFC947
        )
        await ctx.send(embed=embed)

    # !ship command
    @commands.command()
    async def ship(self, ctx):
        embed = discord.Embed(
            title="🚀 How to Share Your Work",
            description=(
                "**1️⃣** Post in <#show-your-work> — WIP is welcome!\n"
                "> Format: **[Project Name]** — [Description] — [Status]\n\n"
                "**2️⃣** Request feedback in <#project-feedback>\n\n"
                "**3️⃣** When launched → post in <#launch-alerts>\n\n"
                "Every ship earns XP + could win Ship of the Week 🏆"
            ),
            color=0x00F5FF
        )
        await ctx.send(embed=embed)

    # !joke — developer jokes
    @commands.command()
    async def joke(self, ctx):
        jokes = [
            "Why do programmers prefer dark mode?\n> Because light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb?\n> None. That's a hardware problem.",
            "Why did the developer go broke?\n> Because he used up all his cache. 💸",
            "A SQL query walks into a bar, walks up to two tables and asks...\n> 'Can I JOIN you?'",
            "Why do Java developers wear glasses?\n> Because they don't C#. 👓",
            "I told my wife she should embrace her mistakes.\n> She gave me a hug. 🤗",
            "To understand recursion, you must first understand recursion.",
            "There are 10 types of people: those who understand binary and those who don't.",
            "A programmer's partner says: 'Go to the store, get a gallon of milk, and if they have eggs, get 12.'\n> The programmer comes home with 12 gallons of milk.",
        ]
        await ctx.send(random.choice(jokes))

    # !inspire — motivational quote for builders
    @commands.command()
    async def inspire(self, ctx):
        quotes = [
            ("Ship often. Ship lean. Learn always.", "Reid Hoffman"),
            ("The best time to start was yesterday. The next best time is now.", "Unknown"),
            ("Make something people want.", "Paul Graham"),
            ("Ideas are easy. Execution is everything.", "John Doerr"),
            ("Done is better than perfect.", "Sheryl Sandberg"),
            ("The only way to do great work is to love what you do.", "Steve Jobs"),
            ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
            ("First, solve the problem. Then, write the code.", "John Johnson"),
            ("Simplicity is the soul of efficiency.", "Austin Freeman"),
        ]
        quote, author = random.choice(quotes)
        embed = discord.Embed(
            description=f'*"{quote}"*\n\n— **{author}**',
            color=0x6C63FF
        )
        await ctx.send(embed=embed)

    # !poll — quick poll creator
    @commands.command()
    async def poll(self, ctx, *, question):
        embed = discord.Embed(
            title="📊 Community Poll",
            description=question,
            color=0x6C63FF
        )
        embed.set_footer(text=f"Poll by {ctx.author.display_name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        await msg.add_reaction("🤔")

    # !serverinfo — server statistics
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            title=f"📊 {guild.name} — Server Info",
            color=0x6C63FF
        )
        embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
        embed.add_field(name="💬 Channels", value=len(guild.channels), inline=True)
        embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="📅 Created", value=guild.created_at.strftime("%b %d, %Y"), inline=True)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))