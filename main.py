import requests
from loguru import logger
import os

from Crawler import Crawler
from Env import Env


def run(env: Env, crawler: Crawler):
    debug = crawler.debug
    debug("请求开始...")

    debug(env.data)

    

if __name__ == "__main__":
    file_path = os.path.join(os.path.abspath(__file__), "..","env", "base.json")
    env = Env.loadFromJson(file_path)
    
    session = requests.Session()
    crawler = Crawler(session, logger)
    
    run(env, crawler)

    