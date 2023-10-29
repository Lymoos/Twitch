import twichDefs.wacthingstream as wacthingstream
from tokens import client_id,client_secret
from fastapi import FastAPI

app = FastAPI()

choose_of_channel = input()
wacthingstream.watchingStreams(chanel_name=choose_of_channel,client_id=client_id,secret_id=client_secret)