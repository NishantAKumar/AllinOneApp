import requests
import json
from isodate import parse_duration
search_url = 'https://www.googleapis.com/youtube/v3/search'
video_url = 'https://www.googleapis.com/youtube/v3/videos'

def search(query):
    search_params = {
        'part' : 'snippet',
        'q'    : query,
        'key'  : 'AIzaSyD9h6pRuMomwT3dAJK1A-Af6sHYaCH-Z58',
        'maxResults' : 99,
        'type' : 'video'
    }   

    video_id = []
    request = requests.get(search_url, params=search_params)
    items = request.json()['items']

    for each in items:
        video_id.append(each['id']['videoId'])

    video_params = {

        'part' : 'snippet,contentDetails',
        'key'  : 'AIzaSyD9h6pRuMomwT3dAJK1A-Af6sHYaCH-Z58',
        'id'   : ','.join(video_id),
        'maxResults' : 99
    }

    r = requests.get(video_url, params=video_params)

    videos = r.json()['items']

    required_videos = []
    for each in videos:
        video_data = {
            'title' : each['snippet']['title'],
            'id'    : each['id'],
            'url'   : f"https://www.youtube.com/watch?v={ each['id'] }",
            'duration' : parse_duration(each['contentDetails']['duration']),
            'thumbnails' : each['snippet']['thumbnails']['high']['url']
        }
        required_videos.append(video_data)

    return required_videos