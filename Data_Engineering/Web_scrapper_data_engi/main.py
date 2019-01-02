import argparse
import logging

logging.basicConfig(level = logging.INFO)

from common import config

logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
	host = config()['new_sites'][news_site_uid]['url']

	logging.info('Beginning scraper for {}'.format(host))
    logging.info('Finding links in homepage...')

if __name__=='__main__':
	parser = argparse.ArgumentParser()

	new_sites_choices = list(config()['new_sites'].keys())


	parser.add_argument('news_site',
		help='The news site that you want to scrape',
		type=str,
		choices=new_sites_choices)

	args = parser.parse_args()
	_news_scraper(args.news_site)

