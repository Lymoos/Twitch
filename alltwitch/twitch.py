import alltwitch.wacthingstream as wacthingstream


def TwitchStart(client_id,client_secret):
    wacthingstream.watchingStreams(client_id=client_id,secret_id=client_secret)