import os
import asyncio
from pyrogram import Client

async def delete_file_after_delay(file_path):
    print('starting waiting time for files')
    await asyncio.sleep(60)
    print('--------------Time Completed for file deletion---------------')  # Wait for 1 minute (60 seconds)
    os.remove(file_path)
    print('============== Message Deleted successfully ===========')

async def delete_message_after_delay(client, message):
    print('starting waiting time for files')
    await asyncio.sleep(60)  # Wait for 1 hour
    print('--------------Time Completed for file deletion---------------')  # Wait for 1 minute (60 seconds)
    await message.delete()
    print('============== Message Deleted successfully ===========')
