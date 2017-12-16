from django.shortcuts import render

# Create your views here.
def ws_receive(message):
    message.reply_channel.send({
        'text': message.content['text'],
    })
