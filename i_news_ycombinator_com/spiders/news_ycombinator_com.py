import scrapy
from scrapy.crawler import CrawlerProcess
import re

from vi_news_ycombinator_com.i_news_ycombinator_com.spiders.locators import Locators
from vi_news_ycombinator_com.i_news_ycombinator_com.items import NewsYcombinatorComItem


class NewsYcombinatorComSpider(scrapy.Spider):
    name = 'news_ycombinator_com'
    start_urls = [
        'https://news.ycombinator.com/item?id=25632979',
        'https://news.ycombinator.com/item?id=25266287',
        'https://news.ycombinator.com/item?id=24969522',
        'https://news.ycombinator.com/item?id=24651637',
        'https://news.ycombinator.com/item?id=24342496'
    ]

    custom_settings = {
        # 'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': [
            'name',
            'person_id',
            'location',
            'remote',
            'willing_to_relocate',
            'technologies',
            'cv_link',
            'email',
            'linkedin',
            'summary',
            'about',
            'source',
        ]
    }

    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.141Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "en-US,en;q=0.9"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response, **kwargs):
        items = NewsYcombinatorComItem()

        comments = response.xpath(Locators.COMMENTS)
        for num, comment in enumerate(comments, 1):
            # if num == 5:
            #     break
            name = comment.xpath(Locators.NAME).get()
            person_id = comment.xpath(Locators.PERSON_ID).get()
            text = comment.xpath(f'(//tr[@class="athing comtr "])[{num}]//span[@class="commtext c00"]//text()').getall()
            location = re.search(Locators.LOCATION, '\n'.join(text))
            if location is not None:
                location = location.group(2)
            remote = re.search(Locators.REMOTE, '\n'.join(text))
            if remote is not None:
                remote = remote.group(2)
            willing_to_relocate = re.search(Locators.WILLING_TO_RELOCATE, '\n'.join(text))
            if willing_to_relocate is not None:
                willing_to_relocate = willing_to_relocate.group(2)
            technologies = re.search(Locators.TECHNOLOGIES, '\n'.join(text))
            cv_link = re.search(Locators.CV_LINK, '\n'.join(text))
            if cv_link is not None:
                cv_link = cv_link.group(2)
            email = re.search(Locators.EMAIL, '\n'.join(text))
            if email is not None:
                email = email.group(2)
            linkedin = ''.join(re.findall(Locators.LINKEDIN, '\n'.join(text)))
            about = []
            for i in text:
                if 'About:' in i:
                    about.append(i.strip())
                    continue
                if 'Location:' not in i and \
                        'Remote:' not in i and \
                        'Willing to relocate:' not in i and \
                        'Willing to Relocate:' not in i and \
                        'Technologies:' not in i and \
                        'Résumé/CV:' not in i and \
                        'Resume:' not in i and \
                        'Email:' not in i and \
                        'email:' not in i and \
                        'LinkedIn:' not in i and \
                        'Github:' not in i and \
                        'Personal Website:' not in i:
                    about.append(i.strip())
            about = '\n'.join(about)
            source = response.url

            items['name'] = name
            items['person_id'] = person_id
            items['location'] = location
            items['remote'] = remote
            items['willing_to_relocate'] = willing_to_relocate
            items['technologies'] = technologies
            items['cv_link'] = cv_link
            items['email'] = email
            items['linkedin'] = linkedin
            items['about'] = about
            items['source'] = source

            yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(NewsYcombinatorComSpider)
    process.start()
