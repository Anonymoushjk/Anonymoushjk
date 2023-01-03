import requests
import telegram

from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hi there! Use the /download command to download a video or audio file from a URL.')

def download(update, context):
    # Get the URL of the file to download
    url = context.args[0]

    # Use the requests library to download the file
    response = requests.get(url)
    file = response.content

    # Check if the URL is for a video or audio file
    if url.endswith('.mp4'):
        # Send the video file as a Telegram video
        context.bot.send_video(chat_id=update.effective_chat.id, video=file)
    elif url.endswith('.mp3'):
        # Send the audio file as a Telegram audio message
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=file)

def main():
    # Create a Telegram bot using the bot token
    bot = telegram.Bot(token='YOUR_BOT_TOKEN_HERE')

    # Create a Telegram updater to handle incoming messages
    updater = Updater(bot=bot, use_context=True)

    # Add a command handler for the /start and /download commands
    start_handler = CommandHandler('start', start)
    download_handler = CommandHandler('download', download)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(download_handler)

    # Start the updater to begin polling for messages
    updater.start_polling()

if __name__ == '__main__':
    main()
