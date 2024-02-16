from pyrogram import Client

api_id = '25789625'
api_hash = '3a161749a26291b8315e7769251dea3a'
phone_number = '+37122233543'

# Replace 'YOUR_CHANNEL_USERNAME' with the actual username of the channel you want to fetch messages from
channel_username = 'sdsfsasd'

with Client("my_account", api_id, api_hash) as app:
    # Get the recent messages in the channel
    messages = app.get_chat_history(channel_username, limit=1)

    # Check if there is any message
    if messages:
        # Get the last message
        last_message = messages[0]

        # Check if the last message has media
        if last_message.media:
            # Download the media file
            media = app.download_media(last_message)

            # Take a screenshot of the media file
            screenshot = app.screenshot(media)

            # Save the screenshot
            screenshot.save("last_event_screenshot.jpg")

            print("Screenshot saved successfully.")
