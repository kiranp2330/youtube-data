import requests
import pandas as pd

API_KEY = 'your_youtube_api_key'
channel_ids = ['UC_x5XG1OV2P6uZZ5FSM9Ttw']  # Example channel IDs

# Function to collect channel data
def collect_channel_data(channel_ids):
    channel_data = []
    for channel_id in channel_ids:
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()
        subscriber_count = data['items'][0]['statistics']['subscriberCount']
        channel_data.append({'channel_id': channel_id, 'subscriber_count': subscriber_count})
    return channel_data

# Collect data
data = collect_channel_data(channel_ids)
df = pd.DataFrame(data)
df.to_csv('youtube_channel_data.csv', index=False)
print("Channel data collected and saved to 'youtube_channel_data.csv'")
