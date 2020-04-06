# 4-ScrapyShell

我们想要在爬虫中使用xpath、beautifulsoup、正则表达式、css选择器等来提取想要的数据。但是因为`scrapy`是一个比较重的框架。每次运行起来都要等待一段时间。因此要去验证我们写的提取规则是否正确，是一个比较麻烦的事情。因此`Scrapy`提供了一个shell，用来方便的测试规则。当然也不仅仅局限于这一个功能。

## 打开Scrapy Shell：

打开cmd终端，进入到`Scrapy`项目所在的目录，然后进入到`scrapy`框架所在的虚拟环境中，输入命令`scrapy shell [链接]`。就会进入到scrapy的shell环境中。在这个环境中，你可以跟在爬虫的`parse`方法中一样使用了。 