from scrapy.item import Item, Field

class PpmItem(Item):
    prix = Field()
    hour = Field()
    age = Field()
    qtm = Field()
    lc	= Field()
    xp	= Field()
    tc	= Field()
