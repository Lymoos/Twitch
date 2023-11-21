import requests
#Taking your oauth token with twich api
def taking_oauth_id(client_id,client_secret):
    response = requests.post("https://id.twitch.tv/oauth2/token",
                         params={"client_id": client_id,
                                 "client_secret": client_secret,
                                 "grant_type": "client_credentials"})
    data = response.json()
    access_token = data["access_token"]
    return access_token

#to determine if the stream is running now
def streaming_now(client_id,client_secret):
    channel_name="jesusavgn"
    oauth_token = taking_oauth_id(client_id=client_id,client_secret=client_secret)
    headers = {"Client-ID": client_id,
           "Authorization": f"Bearer {oauth_token}"}
    
    response = requests.get(f"https://api.twitch.tv/helix/streams?user_login={channel_name}",
                        headers=headers)
    data = response.json()["data"]
    return data

def is_channel_exists(channel_name,client_id,client_secret):
    oauth_token = taking_oauth_id(client_id=client_id,client_secret=client_secret)
    headers = {"Client-ID": client_id,
           "Authorization": f"Bearer {oauth_token}"}
    try:
        response = requests.get(f"https://api.twitch.tv/helix/users?login={channel_name}",
                            headers=headers)
        data = response.json()["data"]
        return data[0]['login']
    except:
        return None