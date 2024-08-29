import random
import os
from dotenv import load_dotenv
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow import dialogflow_response

load_dotenv()
vk_token = os.getenv('TOKEN_VK')


def echo(event, vk_api):
    project_id = os.getenv('DF_PROJECT_ID')
    text = event.text
    session_id = event.user_id
    response_text = dialogflow_response(project_id, session_id, text)
    if response_text:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)
    for event in long_poll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
