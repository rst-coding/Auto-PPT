import os
import codecs
import configparser
config = configparser.ConfigParser()
# 指定编码为 UTF-8


class MyConfig:
    Real_File: str = None
    OPENAI_BASE_URL: str = None
    OPENAI_API_KEY: str = None
    UNSPLASH_ENABLE: str = None
    UNSPLASH_API_KEYS: list = None
    REDIS_ENABLE: str = None
    REDIS_URL: str = None
    AI_INTERFACE: str = None  # 新增配置项

    def __init__(self):
        # 获取当前脚本所在的目录
        base_path = os.path.dirname(os.path.abspath(__file__))
        # 构建 config.ini 的完整路径
        config_path = os.path.join(base_path, '..', 'config.ini')

        config.read_file(codecs.open(config_path, 'r', 'utf-8-sig'))
        self.Real_File = config.get('Credentials', 'Real_File')
        if self.Real_File == "config.ini":
            self.OPENAI_BASE_URL = config.get('Credentials', 'OPENAI_BASE_URL')
            self.OPENAI_API_KEY = config.get('Credentials', 'OPENAI_API_KEY')
            # self.UNSPLASH_API_KEYS = config.get('Credentials', 'UNSPLASH_API_KEYS').split(',')
            self.UNSPLASH_ENABLE = config.get('Credentials', 'UNSPLASH_ENABLE')
            self.REDIS_ENABLE = config.get('Credentials', 'REDIS_ENABLE')
            self.REDIS_URL = config.get('Credentials', 'REDIS_URL')
            self.AI_INTERFACE = config.get('Credentials', 'AI_INTERFACE')  # 读取AI_INTERFACE配置项
        else:
            config.read_file(codecs.open(self.Real_File, 'r', 'utf-8-sig'))
            self.OPENAI_BASE_URL = config.get('Credentials', 'OPENAI_BASE_URL')
            self.OPENAI_API_KEY = config.get('Credentials', 'OPENAI_API_KEY')
            # self.UNSPLASH_API_KEYS = config.get('Credentials', 'UNSPLASH_API_KEYS').split(',')
            self.UNSPLASH_ENABLE = config.get('Credentials', 'UNSPLASH_ENABLE')
            self.REDIS_ENABLE = config.get('Credentials', 'REDIS_ENABLE')
            self.REDIS_URL = config.get('Credentials', 'REDIS_URL')
            self.AI_INTERFACE = config.get('Credentials', 'AI_INTERFACE')  # 读取AI_INTERFACE配置项
        print(self.OPENAI_API_KEY)

if __name__ == '__main__':
    my_config = MyConfig()
    print(my_config.REDIS_ENABLE)
