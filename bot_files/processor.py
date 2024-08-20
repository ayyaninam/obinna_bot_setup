import re
from decimal import Decimal
from base.models import RoomCreation, Channel

def extract_number_from_string(input_string):
    match = re.search(r'\d+(\.\d+)?', input_string)
    if match:
        number = float(match.group())
        formatted_number = f"{number:.2f}"
        return Decimal(formatted_number)
    else:
        return None
    

def get_room_creation_title_description():
    room_creation_query = RoomCreation.objects.all().order_by('-date_modified')[:1]
    if room_creation_query.exists():
        return [room_creation_query[0].title, room_creation_query[0].description]
    else:
        return [None, None]

def create_channel_in_db(channel_id, artist, influencer, artist_id, influencer_id):
    if (channel_id or artist or influencer or artist_id or influencer_id) == None:
        return None
    # create entry in db
    new_room = Channel.objects.create(channel_id=channel_id, artist=artist, influencer=influencer, artist_id=artist_id, influencer_id=influencer_id)
    return new_room