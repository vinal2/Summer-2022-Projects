import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
import youtube_dl
import os

DISCORD_TOKEN = 'insert discord token'
api_key = 'insert bot api key'
bot = commands.Bot(command_prefix="=")

class Music(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx, url : str):
        songExists = os.path.isfile("song.mp3")
        '''try:
            if songExists:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("wait for current music to end or use stop")
            return'''
        
        channel = ctx.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            if voice.is_playing():
                voice.stop()
                await voice.move_to(channel)                
        else:
            voice = await channel.connect()
            if songExists:
                os.remove("song.mp3")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("the bot cant leave retard")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("cant pau- :mute:")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("cant play :mute:")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        voice.stop()

@bot.listen('on_message')
async def on_message(message):
    if message.content == "horny":
        await message.channel.send("el trole?", reference=message)

@bot.event
async def on_message(ctx):
    author=str(ctx.author)
        

bot.add_cog(Music(bot))

bot.run(DISCORD_TOKEN)
