import logging
import traceback

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from src import config
from src.utils import create_tg_post


# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt='%H:%M:%S',
)


def run_polling(lp: VkBotLongPoll):
    for event in lp.listen():
        try:
            if event.type == VkBotEventType.WALL_POST_NEW:
                attachments = []

                if 'attachments' in event.object:
                    for attach in event.object['attachments']:
                        if attach['type'] == 'photo':
                            attachments.append(attach['photo']['sizes'][-1]['url'])

                if attachments:
                    create_tg_post(attachments, event.object['text'])
                elif (event.object['text'] and not 'attachments' in event.object):
                    create_tg_post([], event.object['text'])
        except Exception as err:
            logging.error(traceback.format_exc())


def main() -> None:
    vk = vk_api.VkApi(
        token=config.VK_TOKEN,
        api_version=config.VK_API_VERSION
    )
    api = vk.get_api()
    group = api.groups.getById()[0]
    longpoll = VkBotLongPoll(vk, group['id'])

    logging.info('VK Group <%s> (vk.com/%s) listening', group['name'], group['screen_name'])

    run_polling(longpoll)


if __name__ == '__main__':
    try:
        main()
    except:
        logging.error(traceback.format_exc())
