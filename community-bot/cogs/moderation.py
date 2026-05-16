import discord
from discord.ext import commands
from datetime import timedelta

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Helper: check if user is a mod
    def is_mod():
        async def predicate(ctx):
            return any(role.name in ['Moderator', 'Senior Moderator', 'Core Team', 'Founder', 'FOUNDER']
                      for role in ctx.author.roles)
        return commands.check(predicate)

    # !warn command
    @commands.command()
    @is_mod()
    async def warn(self, ctx, member: discord.Member, *, reason="No reason given"):
        embed = discord.Embed(
            title="⚠️ Warning Issued",
            description=f"**Member:** {member.mention}\n**Reason:** {reason}\n**By:** {ctx.author.mention}",
            color=0xFFC947
        )
        await ctx.send(embed=embed)
        
        # DM the warned member
        try:
            await member.send(f"⚠️ You received a warning in **{ctx.guild.name}**.\n**Reason:** {reason}")
        except:
            pass

    # !mute command (timeout)
    @commands.command()
    @is_mod()
    async def mute(self, ctx, member: discord.Member, minutes: int = 10, *, reason="No reason given"):
        duration = timedelta(minutes=minutes)
        await member.timeout(duration, reason=reason)
        
        embed = discord.Embed(
            title="🔇 Member Muted",
            description=f"**Member:** {member.mention}\n**Duration:** {minutes} minutes\n**Reason:** {reason}",
            color=0xFF6B6B
        )
        await ctx.send(embed=embed)

    # !unmute command
    @commands.command()
    @is_mod()
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"✅ {member.mention} has been unmuted.")

    # !kick command
    @commands.command()
    @is_mod()
    async def kick(self, ctx, member: discord.Member, *, reason="No reason given"):
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="👢 Member Kicked",
            description=f"**Member:** {member.display_name}\n**Reason:** {reason}",
            color=0xFF6B6B
        )
        await ctx.send(embed=embed)

    # !ban command
    @commands.command()
    @is_mod()
    async def ban(self, ctx, member: discord.Member, *, reason="No reason given"):
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="🔨 Member Banned",
            description=f"**Member:** {member.display_name}\n**Reason:** {reason}",
            color=0xFF0000
        )
        await ctx.send(embed=embed)

    # !clear command
    @commands.command()
    @is_mod()
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"✅ Deleted {amount} messages.")
        await msg.delete(delay=3)  # Auto-delete confirmation after 3s

    # Error handler for missing permissions
    @warn.error
    @mute.error
    @kick.error
    @ban.error
    async def mod_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("❌ You don't have permission to use this command.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
