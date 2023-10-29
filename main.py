import wacthingstream
from tokens import client_id,client_secret

choose_of_channel = input()
wacthingstream.watchingStreams(chanel_name=choose_of_channel,client_id=client_id,secret_id=client_secret)