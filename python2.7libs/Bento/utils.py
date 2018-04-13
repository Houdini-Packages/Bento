import os
import ConfigParser

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    
    def __init__(self):
        self.config = None


    def clear(self):
        self.config = None


    def loadConfig(self):
        self.clear()

        if os.environ.get('BENTO_CONFIG_PATH'):
            self.config = configparser.ConfigParser()
            self.config.read(os.path.join(os.environ.get('BENTO_CONFIG_PATH'), 'bento_config.ini'))
            return True
        else:
            return None


    def getConfigNodeColor(self):
        result = self.loadConfig()

        if not result:
            return

        node_colors = self.config['Node_Colors']
        return node_colors
        