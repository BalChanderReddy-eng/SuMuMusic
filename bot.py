import discord
from discord.ext import commands
import yt_dlp
import os
from dotenv import load_dotenv
from collections import deque

# Load token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Setup bot
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Song queue and status
guild_queues = {}
playing_status = {}

def get_guild_queue(guild_id):
    if guild_id not in guild_queues:
        guild_queues[guild_id] = deque()
    return guild_queues[guild_id]

def is_playing(guild_id):
    return playing_status.get(guild_id, False)

def set_playing(guild_id, status):
    playing_status[guild_id] = status

async def play_next(ctx):
    queue = get_guild_queue(ctx.guild.id)
    if queue and ctx.voice_client:
        url, title = queue.popleft()

        ffmpeg_opts = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn -af "equalizer=f=60:t=q:w=1:g=-12,equalizer=f=170:t=q:w=1:g=-10,equalizer=f=1000:t=q:w=1:g=3,equalizer=f=3000:t=q:w=1:g=2,equalizer=f=10000:t=q:w=1:g=-2"'
        }

        source = discord.FFmpegPCMAudio(url, **ffmpeg_opts)

        def after_playing(error):
            if error:
                print(f"⛔ Error in player: {error}")
            set_playing(ctx.guild.id, False)
            # Avoid calling directly from another thread
            bot.loop.create_task(play_next(ctx))

        set_playing(ctx.guild.id, True)
        ctx.voice_client.play(source, after=after_playing)
        await ctx.send(f"🎶 Now Playing: **{title}**")
    else:
        set_playing(ctx.guild.id, False)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("🔊 Joined your voice channel.")
    else:
        await ctx.send("❌ You're not in a voice channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        get_guild_queue(ctx.guild.id).clear()
        set_playing(ctx.guild.id, False)
        await ctx.send("👋 Left the voice channel and cleared the queue.")
    else:
        await ctx.send("❌ I'm not in a voice channel.")

@bot.command()
async def play(ctx, url: str):
    if not ctx.author.voice:
        await ctx.send("❌ You need to be in a voice channel.")
        return

    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            title = info.get('title', 'Unknown Title')

        queue = get_guild_queue(ctx.guild.id)
        queue.append((audio_url, title))

        if not is_playing(ctx.guild.id):
            await play_next(ctx)
        else:
            await ctx.send(f"📥 Added to queue: **{title}**")

    except Exception as e:
        print(f"❌ Error: {e}")
        await ctx.send("❌ Could not play the song. Try another link.")

@bot.command()
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏭️ Skipped current song.")
    else:
        await ctx.send("❌ No song is playing.")

@bot.command()
async def stop(ctx):
    queue = get_guild_queue(ctx.guild.id)
    queue.clear()
    if ctx.voice_client:
        ctx.voice_client.stop()
        set_playing(ctx.guild.id, False)
        await ctx.send("⏹️ Stopped and cleared queue.")

@bot.command()
async def queue(ctx):
    queue = get_guild_queue(ctx.guild.id)
    if not queue:
        await ctx.send("📭 Queue is empty.")
    else:
        queue_list = [f"{idx+1}. {title}" for idx, (_, title) in enumerate(queue)]
        await ctx.send("📃 **Song Queue:**\n" + "\n".join(queue_list))

bot.run(TOKEN)
