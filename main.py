from pypresence import Presence
import time

client_id  = "" #Application id

RPC = Presence(client_id = client_id)
RPC.connect()

RPC.update(buttons = [{"label": "Islamic Discord Server", "url": "https://discord.gg/islam"}])

while 1:
    time.sleep(15)
