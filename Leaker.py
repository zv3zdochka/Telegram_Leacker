import datetime
import aiofiles
from telethon.sync import TelegramClient
from asyncio import run, create_task
from math import ceil
import cryptg
import os.path

api_id = 0
api_hash = ""
name = "searcher"
chats = []
COWORKERS = 8


def chunk_into_n(lst, n):
    size = ceil(len(lst) / n)
    return list(map(lambda x: lst[x * size:x * size + size], list(range(n))))

async def get_all_chats(client: TelegramClient) -> list[int]:
    print("Extracting messages")
    i = 1
    async for dialog in client.iter_dialogs():
        try:
            print(f"{i}) {dialog.name}, {dialog.id}")
            chats.append(dialog.id)
            i += 1
        except:
            pass

    return chats


async def download_media(msg, path):
    try:
        await msg.download_media(path)
    except Exception as e:
        await msg.download_media(path)
    finally:
        pass


async def main(name, api_id, api_hash):
    async with aiofiles.open('dwarf.txt', 'w') as file:
        try:
            async with TelegramClient(name, api_id, api_hash) as client:
                if not os.path.isdir("./downloads"):
                    os.mkdir("./downloads")
                chats = await get_all_chats(client)

                async for msg in client.iter_messages(chats[int(input("Enter chat number: ")) - 1]):

                    if msg.photo and not os.path.isfile(f"./downloads/{msg.photo.id}{msg.file.ext}"):
                        create_task(download_media(msg, f"./downloads/{msg.photo.id}"))

                    elif msg.video and not os.path.isfile(f"./downloads/{msg.video.id}{msg.file.ext}"):
                        create_task(download_media(msg, f"./downloads/{msg.video.id}"))

                    elif msg.audio:
                        create_task(download_media(msg, f"./downloads/{msg.audio.id}"))

                    elif msg.voice:
                        create_task(download_media(msg, f"./downloads/{msg.voice.id}"))

                    elif msg.document:
                        create_task(download_media(msg, f"./downloads/{msg.document.id}"))

                    elif not msg.photo and not msg.video and not msg.document:
                        if msg.text is not None:
                            try:
                                await file.write(
                                    f"From {msg.peer_id} in {(msg.date + datetime.timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")}\n")
                                await file.write(str(msg.text) + '\n')
                                print(msg.text)
                            except Exception as e:
                                print(e, msg.id)
                    else:
                        print("Skipped media")

        except Exception as e:
            exit(e)


run(main(name, api_id, api_hash))
