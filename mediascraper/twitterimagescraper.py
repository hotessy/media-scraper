import sys
sys.path.append('../')

import argparse
import mediascrapers
from mediascrapers import TwitterImageScraper

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url-list", required=True,
                           help="Path of file")
    args = vars(ap.parse_args())
    filepath = args["url_list"]

    scraper = TwitterImageScraper(driver='chrome', mode='verbose', debug=True)
    file = open(filepath, 'r')
    URLs = file.readlines()

    for url in URLs:
        print(url)
        tasks = scraper.scrape(url)
        scraper.download(tasks=tasks, path='.\\download\\general')
