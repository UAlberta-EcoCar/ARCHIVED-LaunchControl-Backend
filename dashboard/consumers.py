from channels import Group

from .models import DataPipeline
from channels.sessions import channel_session

import json

def ws_message(message):
    # message.reply_channel.send({
    #     "text": message.content['text'],
    # })
    Group(message.content['text']).add(message.reply_channel)