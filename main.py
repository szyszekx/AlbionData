import logging
import logging.handlers
import os

import requests
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# try:
#     SOME_SECRET = os.environ["SOME_SECRET"]
# except KeyError:
#     SOME_SECRET = "Token not available!"
#     #logger.info("Token not available!")
#     #raise


if __name__ == "__main__":
    # logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://gameinfo-ams.albiononline.com/api/gameinfo/battles?range=day&sort=recent&limit=500')
    data = r.json()
    logger.info(f'Number of battles: {len(data)}')
    logger.info(f'{r.status_code} - {r.reason}')
    for battle in data:
        count = 0
        for x in battle["players"]:
            if battle["players"][x]["guildId"] == "wtqzxhOLStCwyD_ixIxC3A":
                count += 1
        if count > 15:
            logger.info(f'fightId: {battle["id"]} started {battle["startTime"]} end ended {battle["endTime"]}')
            logger.info(f'Total players found in guild: {count}')
    # if r.status_code == 200:
    #     data = r.json()
    #     temperature = data["forecast"]["temp"]
    #     logger.info(f'Weather in Berlin: {temperature}')
