from datetime import datetime, timedelta
import json

import requests


# Festival programme

url = 'https://graphql.primaverasound.com/prod/graphql?query=query%20Get(%24name%3A%20String!)%20%7B%0A%20%20getLineupEvent(name%3A%20%24name)%20%7B%0A%20%20%20%20artists%20%7B%0A%20%20%20%20%20%20fontRatio%0A%20%20%20%20%20%20artistSlugName%0A%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20artistReadableName%20%7B%0A%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20image%20%7B%0A%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20postUri%0A%20%20%20%20%20%20duration%0A%20%20%20%20%20%20venues%20%7B%0A%20%20%20%20%20%20%20%20duration%0A%20%20%20%20%20%20%20%20venueSlugName%0A%20%20%20%20%20%20%20%20artistSetSlugName%0A%20%20%20%20%20%20%20%20artistSetName%0A%20%20%20%20%20%20%20%20artistSetGenres%0A%20%20%20%20%20%20%20%20artistSetIsFavorite%0A%20%20%20%20%20%20%20%20shortTitle%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20shortTitle%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20smallText%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20artistSetReadableName%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20image%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20dateTimeStartReal%0A%20%20%20%20%20%20%20%20dateTimeStartHuman%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20venues%0A%20%20%20%20showDate%0A%20%20%20%20showDateTime%0A%20%20%20%20showVenue%0A%20%20%20%20showTicket%0A%20%20%20%20timezone%0A%20%20%7D%0A%7D%0A&operationName=Get&variables=%7B%22name%22%3A%22primavera-sound-2023-barcelona%22%7D'
response = requests.get(url)
data = response.json()

venues = json.loads(data['data']['getLineupEvent']['venues'])

artists = data['data']['getLineupEvent']['artists']


artists_list = []

for a in artists:
    name = a['artistName']
    for v in a['venues']:
        artists_list.append({
            'name': name,
            'stage': venues[v['venueSlugName']]['venueReadableName']['ca'],
            'stage_pos': venues[v['venueSlugName']]['position'],
            'start': datetime.fromtimestamp(int(v['dateTimeStartReal'])/1000),
            'end': datetime.fromtimestamp(int(v['dateTimeStartReal'])/1000) + timedelta(minutes=v['duration']),
        })




# Primavera a la ciutat programme

url = 'https://graphql.primaverasound.com/prod/graphql?query=query%20Get(%24name%3A%20String!)%20%7B%0A%20%20getLineupEvent(name%3A%20%24name)%20%7B%0A%20%20%20%20artists%20%7B%0A%20%20%20%20%20%20fontRatio%0A%20%20%20%20%20%20artistSlugName%0A%20%20%20%20%20%20artistName%0A%20%20%20%20%20%20artistReadableName%20%7B%0A%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20image%20%7B%0A%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20postUri%0A%20%20%20%20%20%20duration%0A%20%20%20%20%20%20venues%20%7B%0A%20%20%20%20%20%20%20%20duration%0A%20%20%20%20%20%20%20%20venueSlugName%0A%20%20%20%20%20%20%20%20artistSetSlugName%0A%20%20%20%20%20%20%20%20artistSetName%0A%20%20%20%20%20%20%20%20artistSetGenres%0A%20%20%20%20%20%20%20%20artistSetIsFavorite%0A%20%20%20%20%20%20%20%20shortTitle%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20shortTitle%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20smallText%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20artistSetReadableName%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20image%20%7B%0A%20%20%20%20%20%20%20%20%20%20es%0A%20%20%20%20%20%20%20%20%20%20en%0A%20%20%20%20%20%20%20%20%20%20ca%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20dateTimeStartReal%0A%20%20%20%20%20%20%20%20dateTimeStartHuman%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20venues%0A%20%20%20%20showDate%0A%20%20%20%20showDateTime%0A%20%20%20%20showVenue%0A%20%20%20%20showTicket%0A%20%20%20%20timezone%0A%20%20%7D%0A%7D%0A&operationName=Get&variables=%7B%22name%22%3A%22primavera-a-la-ciutat-2023-barcelona%22%7D'
response = requests.get(url)
data = response.json()

venues = json.loads(data['data']['getLineupEvent']['venues'])

artists = data['data']['getLineupEvent']['artists']

for a in artists:
    name = a['artistName']
    for v in a['venues']:
        artists_list.append({
            'name': name,
            'stage': venues[v['venueSlugName']]['venueReadableName']['ca'],
            'stage_pos': venues[v['venueSlugName']]['position'],
            'start': datetime.fromtimestamp(int(v['dateTimeStartReal'])/1000),
            'end': datetime.fromtimestamp(int(v['dateTimeStartReal'])/1000) + timedelta(minutes=v['duration']),
        })





# Print in clashfinder style format

newlist = sorted(artists_list, key=lambda d: (d['stage_pos'], d['stage'], d['start']))

last_stage = None
for a in newlist:
    if last_stage != a['stage']:
        print('\n')
    last_stage = a['stage']

    line = 'act = {{"start":"{start_str}","end":"{end_str}","stage":"{stage}","act":"{artist}"}}'.format(
        artist=a['name'],
        stage=a['stage'],
        start_str=a['start'].strftime('%Y-%m-%d %H:%M'),
        end_str=a['end'].strftime('%Y-%m-%d %H:%M'))

    print(line)