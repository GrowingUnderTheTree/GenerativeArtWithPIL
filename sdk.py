# https://discord.com/developers/applications/918847155278598174/rich-presence/assets
from pypresence import Presence
import time


def sdk():
    print("xd")


client_id = "918847155278598174"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image
RPC.update(large_image="big-image", large_text="Makkau hijau sim",
           small_image="small-image", small_text="bapakkau hijau")

while 1:
    time.sleep(15)  # Can only update presence every 15 seconds
