<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SuMuMusic - Discord Bot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 2rem;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2 {
      color: #2c3e50;
    }
    code {
      background-color: #eee;
      padding: 2px 4px;
      border-radius: 4px;
      font-family: Consolas, monospace;
    }
    pre {
      background-color: #eee;
      padding: 1em;
      overflow-x: auto;
      border-radius: 6px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 0.5em;
    }
    th {
      background-color: #ddd;
    }
  </style>
</head>
<body>

  <h1>🎵 SuMuMusic - A Discord Music Bot with Queue & Audio Filters</h1>
  <p><strong>SuMuMusic</strong> is a lightweight and powerful Discord music bot built in Python. It supports YouTube audio playback, a server-based song queue, and enhanced audio quality using FFmpeg filters. Optimized for clear vocals and balanced bass — perfect for any community voice channel.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li>✅ Play music from YouTube links</li>
    <li>📥 Add songs to a <strong>server-specific queue</strong></li>
    <li>🔁 Automatically plays next song after current ends</li>
    <li>⏭️ Skip, ⏹️ Stop, and 👋 Leave voice channel anytime</li>
    <li>🔊 <strong>Custom equalizer settings</strong> for crisp vocals and tuned bass</li>
    <li>📄 View queue with <code>!queue</code></li>
    <li>⚙️ Built with <code>discord.py</code>, <code>yt-dlp</code>, and <code>FFmpeg</code></li>
  </ul>

  <h2>📦 Requirements</h2>
  <ul>
    <li>Python 3.8+</li>
    <li>FFmpeg (installed locally or in the cloud)</li>
    <li><code>discord.py</code></li>
    <li><code>yt-dlp</code></li>
    <li><code>python-dotenv</code></li>
  </ul>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h2>🛠️ Setup</h2>
  <ol>
    <li>Clone this repository:
      <pre><code>git clone https://github.com/yourusername/sumumusic.git
cd sumumusic</code></pre>
    </li>
    <li>Create a <code>.env</code> file and add your bot token:
      <pre><code>DISCORD_TOKEN=your_discord_token_here</code></pre>
    </li>
    <li>Run the bot:
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>🖥️ Hosting</h2>
  <p>This bot is ready to be deployed on platforms like:</p>
  <ul>
    <li><a href="https://render.com" target="_blank">Render</a></li>
    <li><a href="https://replit.com" target="_blank">Replit</a></li>
    <li><a href="https://heroku.com" target="_blank">Heroku (deprecated free tier)</a></li>
  </ul>

  <h2>🧠 Commands</h2>
  <table>
    <thead>
      <tr><th>Command</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr><td><code>!join</code></td><td>Joins your current voice channel</td></tr>
      <tr><td><code>!play &lt;url&gt;</code></td><td>Plays the song or queues it</td></tr>
      <tr><td><code>!queue</code></td><td>Shows current queue</td></tr>
      <tr><td><code>!skip</code></td><td>Skips the current song</td></tr>
      <tr><td><code>!stop</code></td><td>Stops playback and clears queue</td></tr>
      <tr><td><code>!leave</code></td><td>Leaves the voice channel</td></tr>
    </tbody>
  </table>

  <h2>🎚️ Audio Tuning</h2>
  <p>FFmpeg is used with finely tuned EQ filters:</p>
  <ul>
    <li>✅ Reduced muddy bass (<code>60Hz</code>, <code>170Hz</code>)</li>
    <li>✅ Boosted mids (<code>1kHz</code>, <code>3kHz</code>) for vocals</li>
    <li>✅ Slight high cut to reduce hiss</li>
  </ul>

  <h2>👤 Credits</h2>
  <p>Bot by <a href="https://github.com/YOUR_GITHUB_ID" target="_blank">Balchander Reddy Yedla</a><br />
     Inspired by open-source Discord music bots and tailored for quality.</p>

</body>
</html>
