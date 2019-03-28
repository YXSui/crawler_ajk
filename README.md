# crawler_ajk
HousePrice crawler of Xi'An

author@suiyuxuan

## **项目依赖库**
> scrapy

> json

> re

## **创建scrapy项目**

    scrapy startproject projectname

##**项目结构**

#####crawler_ajk
>**spider/**
>>init.py

>>spider.py


>init.py

>items.py

>middlewares.py

>pipelines.py

>settings.py

### spider/spider.py
存储爬虫代码的文件。此文件是整个爬虫的发起点，启动爬虫时会从此文件中的start_urls里的url地址开始爬，中间经过了 爬虫》引擎》调度器》下载器》引擎》爬虫，此时会返回一个response即为start_urls对应的网页文件，在此爬虫文件里还有一个parse函数，带有response这个参数，专门用来解析返回文件的处理，解析后的结果经提取处理后可存放到items.py定义的字段里（需要引入items.py中相应的类实例），如果要想将数据转存到数据库或其他格式，只需将item放出 （yield item），它会被pipelines.py自动捕获进行处理。

**参数**
>**class Spider**:定义爬虫类

>**def start_request**:定义请求网址的函数，函数里主要定义网址，头文件等

>**def parse_info**:定义解析函数，主要用来解析我们需要爬取网址的字段，并存入items之前定义好的字段中，通常会用到正则表达式的方法进行网页字段提取。

>**name**:定义爬虫名字,name='ajk'

>**allowed_domains**:定义要爬取的域名范围,allowed_domains='anjuke.com'

>**start_urls**:定义初始爬取的网址，start_urls=['https://xa.anjuke.com/sale/xianzhoubianc/']

>**headers**:请求头文件，用来模拟浏览行为，headers={'User-Agent':"'Mozilla/5.0'"}

>**item**: 获取在items.py中定义的数据字段，item=AjkItem()

>**xpath**：提取字段的一种方法

### __init__.py
此文件为项目的初始化文件，主要写的是一些项目的初始化信息。

### items.py
爬虫项目的数据容器文件，主要用来定义我们要获取的数据
items.py 中定义了储存数据的字段名，在编辑此文件前需先分析要提取那些信息，定义好名称即可。

### middlewares.py
中间件，创建项目时自动生成

### pipelines.py
爬虫项目的管道文件，主要用来对items里面定义的数据进行进一步的加工与处理。此文件是用来处理提取的数据的，可以将数据转存为其他格式或数据库中,如果要启用此文件需要先在settings.py中指明pipelines.py中的类，并且如果有多个类的话还要定义优先级，就是后面的数字，越小优先级越高， 
在每个pipeline类中必有一个process_item的函数，此函数是数据处理的具体流程。此文件自动生成，可以不进行修改。

### settings.py
爬虫项目的设置文件，主要为爬虫项目的一些设置信息。如爬取间隔，请求时间，中文获取等。
