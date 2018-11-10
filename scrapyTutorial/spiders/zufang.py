# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import scrapy
from scrapy.http import Request
from scrapyTutorial.items import ZuFangItem

class ZuFangSpiders(scrapy.Spider):
    name = "zufang"
    allowed_domains = ["zu.fang.com"]
    firstUrl = "http://zu.fang.com"
    preFixUrl = "http://zu.fang.com/house/i3"
    sufFixUrl = "/"
    start_urls = ["http://zu.fang.com/house/"]

    def parse(self, response):
        bs = BeautifulSoup(response.text,"lxml")
        houseList = bs.select_one(".houseList").findAll("dd")
        for house in houseList:
            if house is None:
                continue
            url = "http://zu.fang.com"+house.find("a")["href"]
            title = house.find("a")["title"]
            zuFangType = house.select_one(".font15").text.strip().split("|")[0]
            fangJianType = house.select_one(".font15").text.strip().split("|")[1]
            size = house.select_one(".font15").text.strip().split("|")[2]
            chaoXiang = house.select_one(".font15").text.strip().split("|")[3]
            area1 = house.select_one(".gray6").findAll("a")[0].span.string
            area2 = house.select_one(".gray6").findAll("a")[1].span.string
            area3 = house.select_one(".gray6").findAll("a")[2].span.string
            jiaoTongJuLi = house.div.select_one(".note")
            if jiaoTongJuLi is None:
                jiaoTongJuLi = ""
            else:
                jiaoTongJuLi = jiaoTongJuLi.text
            liangDianTag = house.select_one("p.mt12 .note.colorGreen")
            liangDian = ""
            if liangDianTag is not None:
                liangDian = liangDianTag.string.strip()+","
                for l in liangDianTag.next_siblings:
                    liangDian = liangDian + l.string.strip()+","
                liangDian = liangDian[:-1]
            price = house.select_one(".price").text
            houseAttr = {}
            houseAttr["title"] = title
            houseAttr["url"] = url
            houseAttr["zuFangType"] = zuFangType
            houseAttr["fangJianType"] = fangJianType
            houseAttr["size"] = size
            houseAttr["chaoXiang"] = chaoXiang
            houseAttr["area1"] = area1
            houseAttr["area2"] = area2
            houseAttr["area3"] = area3
            houseAttr["jiaoTongJuLi"] = jiaoTongJuLi
            houseAttr["liangDian"] = liangDian
            houseAttr["price"] = price
            print(houseAttr)



