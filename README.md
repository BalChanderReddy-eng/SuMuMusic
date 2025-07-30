🎵 SuMuMusic - A Discord Music Bot with Queue & Audio Filters


SuMuMusic is a lightweight and powerful Discord music bot built in Python. It supports YouTube audio playback, a server-based song queue, and enhanced audio quality using FFmpeg filters. Optimized for clear vocals and balanced bass — perfect for any community voice channel.



🚀 Features
✅ Play music from YouTube links

📥 Add songs to a server-specific queue

🔁 Automatically plays next song after current ends

⏭️ Skip, ⏹️ Stop, and 👋 Leave voice channel anytime

🔊 Custom equalizer settings for crisp vocals and tuned bass

📄 View queue with !queue

⚙️ Built with discord.py, yt-dlp, and FFmpeg

📦 Requirements
Python 3.8+

FFmpeg (installed locally or in the cloud)

discord.py

yt-dlp

python-dotenv

Install them via:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ Setup
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/sumumusic.git
cd sumumusic
Create a .env file and add your bot token:

env
Copy
Edit
DISCORD_TOKEN=your_discord_token_here
Run the bot:

bash
Copy
Edit
python main.py
