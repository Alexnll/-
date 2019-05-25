# Scrapy相关知识梳理
## 框架架构
Scrapy框架主要分为以下及部分：
1. Engine
2. Item
3. Scheduler
4. Downduler
5. Spiders
6. Item Pipeline
7. Downloader Middlewares
8. Spider Middlewares

项目结构：
scrapy.cfg
project/
\- __init\__.py
\- items.py
\- pipelines.py
\- settings.py
\- middlewares.py
\- spiders/
\-\- __init\__.py
\-\- spider1.py
\-\- spider2.py
\-\- ...
## 框架安装
1. 安装anaconda框架并为创建虚拟环境
2. 安装lxml库(pip)
3. 安装pyOpenSSL库(pip)
4. 安装Twisted库(wheel+pip)
5. 安装PyWin32库(wheel+pip)
6. 安装Scrapy库(pip)