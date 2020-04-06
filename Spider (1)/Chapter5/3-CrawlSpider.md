# 3-CrawlSpider

在上一个糗事百科的爬虫案例中。我们是自己在解析完整个页面后获取下一页的url，然后重新发送一个请求。有时候我们想要这样做，只要满足某个条件的url，都给我进行爬取。那么这时候我们就可以通过`CrawlSpider`来帮我们完成了。`CrawlSpider`继承自`Spider`，只不过是在之前的基础之上增加了新的功能，可以定义爬取的url的规则，以后scrapy碰到满足条件的url都进行爬取，而不用手动的`yield Request`。

## CrawlSpider爬虫：

### 创建CrawlSpider爬虫：

之前创建爬虫的方式是通过`scrapy genspider [爬虫名字] [域名]`的方式创建的。如果想要创建`CrawlSpider`爬虫，那么应该通过以下命令创建：

```python
scrapy genspider -c crawl [爬虫名字] [域名]
```

### LinkExtractors链接提取器：

使用`LinkExtractors`可以不用程序员自己提取想要的url，然后发送请求。这些工作都可以交给`LinkExtractors`，他会在所有爬的页面中找到满足规则的`url`，实现自动的爬取。以下对`LinkExtractors`类做一个简单的介绍：

```python
class scrapy.linkextractors.LinkExtractor(
    allow = (),
    deny = (),
    allow_domains = (),
    deny_domains = (),
    deny_extensions = None,
    restrict_xpaths = (),
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)
```

主要参数讲解：

- allow：允许的url。所有满足这个正则表达式的url都会被提取。
- deny：禁止的url。所有满足这个正则表达式的url都不会被提取。
- allow_domains：允许的域名。只有在这个里面指定的域名的url才会被提取。
- deny_domains：禁止的域名。所有在这个里面指定的域名的url都不会被提取。
- restrict_xpaths：严格的xpath。和allow共同过滤链接。

### Rule规则类：

定义爬虫的规则类。以下对这个类做一个简单的介绍：

```python
class scrapy.spiders.Rule(
    link_extractor, 
    callback = None, 
    cb_kwargs = None, 
    follow = None, 
    process_links = None, 
    process_request = None
)
```

主要参数讲解：

- link_extractor：一个`LinkExtractor`对象，用于定义爬取规则。
- callback：满足这个规则的url，应该要执行哪个回调函数。因为`CrawlSpider`使用了`parse`作为回调函数，因此不要覆盖`parse`作为回调函数自己的回调函数。
- follow：指定根据该规则从response中提取的链接是否需要跟进。
- process_links：从link_extractor中获取到链接后会传递给这个函数，用来过滤不需要爬取的链接。