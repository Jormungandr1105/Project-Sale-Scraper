"""
@author: jormungandr1105
@desc: main launcher for sale scraper
@created: 05/27/2022
"""
import os
import os.path as path
import praw
from dotenv import load_dotenv
import time
from Scraper import Scraper
from DiscordBot import DiscordBot


def startup():
	env_file = path.join(path.dirname(path.dirname(path.abspath(__file__))),"data/.env")
	load_dotenv(env_file)
	reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('SECRET'), user_agent=os.getenv('USER_AGENT'))
	return reddit


def main(reddit, config, discordbot):
	scraper = Scraper(config, reddit)
	while True:
		for sub in scraper.conf:
			scraper.getXPosts(20, sub, discordbot)
		time.sleep(120)


if __name__ == '__main__':
	reddit = startup()
	bot = DiscordBot(os.getenv("DISCORD_TOKEN"),os.getenv("DISCORD_CHANNEL"))
	main(reddit, "searches.json", bot)
