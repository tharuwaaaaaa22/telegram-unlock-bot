# Telegram Unlock Bot

## Features:
- Users must share to 3 different groups to unlock video
- Duplicate groups are not counted
- After 3 unique shares, the video is sent from a private channel

## Setup Instructions:
1. Install requirements: `pip install -r requirements.txt`
2. Set your environment variable: `BOT_TOKEN`
3. Run the bot: `python main.py`

Edit `VIDEO_MESSAGE_ID` in main.py to the message ID of the video in your private channel.
