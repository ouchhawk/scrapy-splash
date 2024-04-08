import scrapy
from scrapy_splash import SplashRequest

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['scrollmagic.io']
    start_urls = ['https://scrollmagic.io/examples/advanced/infinite_scrolling.html']

    lua_script = """
    function main(splash, args)
        splash:go(args.url)
    
        local num_scrolls = 8
        local wait_after_scroll = 1.0
    
        local scroll_to = splash:jsfunc("window.scrollTo")
        local get_body_height = splash:jsfunc(
            "function() { return document.body.scrollHeight; }"
        )
    
        -- scroll to the end for "num_scrolls" time
        for _ = 1, num_scrolls do
            scroll_to(0, get_body_height())
            splash:wait(wait_after_scroll)
        end       
         
        return splash:html()
    end
        """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url,
                self.parse,
                endpoint='execute',
                args={
                    'lua_source': self.lua_script,
                    'num_scrolls': 1,  # Adjust based on the number of scrolls needed
                    'scroll_delay': 1.0,  # Adjust based on the website's loading speed
                }
            )

    def parse(self, response):
        # links = response.xpath("//a[not(contains(substring-after(@href, '/'), '.'))]/@href").getall()
        colors = response.xpath("//div/@style").extract()
        print(colors)
