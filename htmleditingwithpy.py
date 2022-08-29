import os
import re
import time
import requests



##buraya webhooktan gelen bilgileri alıp hwidiyle keyini matchleyip var olan key'i değiştirecek kod gerekiyor


Func = open("index.html","w")
   
Func.write("""<head>\n <title>testsite</title>\n <meta name="description" content="keys goes here"> \n <meta name="keywords" content="keying"> \n </head>\n <body> <br>64848744<br>54987464<br>does it work?<br> </body>\n </html>""")
              
Func.close()



print("done")
input()
