from scrapy.spider	import Spider
from scrapy.selector	import Selector

from ppm.items		import PpmItem

class	PpmSpider(Spider):
	name = "ppm"
	allowed_domains = ["soccer.powerplaymanager.com"]
	start_urls = [
			"http://soccer.powerplaymanager.com/en/most-expensive.html?data=lastday",
			"http://soccer.powerplaymanager.com/en/most-expensive.html?data=lastday-2",
			"http://soccer.powerplaymanager.com/en/most-expensive.html?data=lastday-3",
			"http://soccer.powerplaymanager.com/en/most-expensive.html?data=lastday-4",
			"http://soccer.powerplaymanager.com/en/most-expensive.html?data=lastday-5",
			]

	def parse(self, response):
		sel = Selector(response)
		plyr = sel.xpath('//tr')
                items = []
		for p in plyr:
                    item = PpmItem()
                    item['age'] = p.xpath('td[@title="Age"]/text()').extract()
                    item['qtm'] = p.xpath('td[@title="Average quality"]/text()').extract()
                    item['lc']	= p.xpath('td[@title="Career longevity"]/span/text()').extract()
                    item['xp']	= p.xpath('td[@title="Experience"]/text()').extract()
                    item['tc']	= p.xpath('td[@title="Overall rating"]/text()').extract()
                    item['prix'] = p.xpath('td[@class="left_align"]/div/text()').re(r'(?<=Price: ).*')
                    items.append(item)
		return items
