from telethon import TelegramClient
from config import api_id, api_hash, bot_token, group_id

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def kick_all_members():
    try:
        async for member in client.iter_participants(group_id):
            try:
                await client.kick_participant(group_id, member.id)
                print(f"Kicked user {member.id}")
            except Exception as e:
                print(f"Failed to kick user {member.id}. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

with client:
    client.loop.run_until_complete(kick_all_members())
