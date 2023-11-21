import requests,alltwitch.twichDefs as twichDefs,time
# TAE:
# 0 - default
# 1 - channel don't streaming now
# 2 - channel is streaming now and we don't have
def watchingStreams(client_id,secret_id):
    tae = 0
    lstart = 0
    lend = 0
    while True:
        data =  twichDefs.streaming_now(client_id=client_id,client_secret=secret_id)
        if len(data)>0:
            tae = 2
        else:
            tae = 1
        if tae == 2 and lstart==0:
            print("CHANNEL START HIS STREAM")
            lstart=1
        elif lstart==1 and tae==1:
            print("Channel end his stream")
            lstart=0
        elif tae == 1 and lend == 0:
            print("channel don't streaming now. We are waiting a new steam.")
            lstart=0
            lend = 1
            tae = 1
        else:
            pass
        time.sleep(1)
