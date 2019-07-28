# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import re


class ArticleItemLoader(ItemLoader):

    default_output_processor = TakeFirst()


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


def strip_str(value):
    if value is not None:
        return value.strip()


def get_sex(value):
    match_re = re.match(".*?articleGender (.*?)Icon", value)
    if match_re:
        return match_re.group(1)


class QsbkItem(scrapy.Item):
    # define the fields for your item here like:
    head_image = scrapy.Field()
    age = scrapy.Field(input_processor=MapCompose(get_nums))
    sex = scrapy.Field(input_processor=MapCompose(get_sex))
    user_name = scrapy.Field(input_processor=MapCompose(strip_str))
    content = scrapy.Field(input_processor=MapCompose(strip_str))
    funny_num = scrapy.Field(input_processor=MapCompose(get_nums))
    comment_num = scrapy.Field(input_processor=MapCompose(get_nums))
