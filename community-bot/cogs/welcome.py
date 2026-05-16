import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Fires when a new member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        # --- Welcome message in #welcome channel ---
        channel = discord.utils.get(member.guild.channels, name='welcome')
        
        if channel:
            embed = discord.Embed(
                title=f"Welcome to The Builder Bloc, {member.display_name}! 🚀",
                description=(
                    f"Hey {member.mention}! We're so glad you're here.\n\n"
                    f"**Get started in 4 steps:**\n"
                    f"→ Read <#1503477465887281325>\n"
                    f"→ Introduce yourself in <#1503469985203486896>\n"
                    f"→ Pick your roles in <#1503478074837176350>\n"
                    f"→ Jump into any channel and say hi!\n\n"
                    f"Questions? Ask in <#1503477982738518220> 💬"
                ),
                color=0x6C63FF  # Your brand color
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Member #{member.guild.member_count}")
            await channel.send(embed=embed)

        # --- Private DM to new member ---
        try:
            dm_embed = discord.Embed(
                title="Welcome to The Builder Bloc! 🎉",
                description=(
                    "You've joined a community of builders, developers & founders.\n\n"
                    "**Quick start:**\n"
                    "📌 Read the rules first\n"
                    "👋 Post an intro — tell us who you are!\n"
                    "🎯 Grab your interest roles\n"
                    "💡 Type `!help` for available commands\n\n"
                    "We're excited to have you. Let's build something great! 🔥"
                ),
                color=0x6C63FF
            )
            await member.send(embed=dm_embed)
        except discord.Forbidden:
            pass  # Member has DMs disabled — that's okay

    # Fires when a member leaves
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='log-joins')
        if channel:
            embed = discord.Embed(
                description=f"👋 **{member.display_name}** left the server.",
                color=0xFF6B6B
            )
            embed.set_footer(text=f"Members remaining: {member.guild.member_count}")
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))