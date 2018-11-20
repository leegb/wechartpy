import os
from wxpy import Bot
from PyQt5.QtCore import QObject,pyqtSignal
#WX=Bot(cache_path='/mnt/HDD/QUANTPI/wxpy.pkl')
##str(WX.messages[-1]).split(':')[-1].split('(')[0]

class wechartclient(QObject):
    def __init__(self):
        self.client = dict()
    def login(self):
        try:
            self.clieant = Bot(cache_path='./wxpy.pkl')
        except:
            os.remove('./wxpy.pkl')
            self.client = Bot(cache_path='./wxpy.pkl')
        self.premessage = None
    def relogin(self):
        if isinstance(self.client,dict) or (not self.client.alive):
            self.client = Bot(cache_path=True)
    def get_messege(self):
        self.relogin()
        if len(self.client.messages):
            wxmessage = str(self.client.messages[-1])
            return wxmessage
        else:
            return None
    def hand_messege(self):
        if ':' in wxmessage:
            _wxmessage = wxmessage.split(':')[-1].split('(')[0].lstrip().strip()
            if (_wxmessage in all_stocklist) & (_wxmessage != self.premessage):
                self.premessage = _wxmessage
                print(self.premessage)
            else:
                pass
        
