from telethon.sync import TelegramClient
from telethon.tl.functions.photos import GetUserPhotosRequest
import asyncio

api_id = '25789625'
api_hash = '3a161749a26291b8315e7769251dea3a'
phone_number = '37122233543'

# Replace 'sdsfsasd' with the actual username of the channel you want to capture the screenshot from
channel_username = ''

client = TelegramClient(phone_number, api_id, api_hash)

async def capture_last_event_screenshot():
    # Get the channel entity
    channel = await client.get_entity(channel_username)

    # Get the recent messages in the channel
    messages = await client.get_messages(channel, limit=1)

    # Check if there is any message
    if messages:
        # Get the last message
        last_message = messages[0]

        # Check if the last message has media
        if last_message.media:
            # Download the media file
            media = await last_message.download_media()

            # Take a screenshot of the media file
            screenshot = await client.takeout_file(media)

            # Save the screenshot
            with open('last_event_screenshot.jpg', 'wb') as f:
                f.write(screenshot)

            print("Screenshot saved successfully.")

with client:
    client.loop.run_until_complete(capture_last_event_screenshot())
