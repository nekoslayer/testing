import os
import re
import time
import requests



##buraya webhooktan gelen bilgileri alıp hwidiyle keyini matchleyip var olan key'i değiştirecek kod gerekiyor


Func = open("index.html","w")
   
Func.write("""<head>\n <title>testsite</title>\n <meta name="description" content="keys goes here"> \n <meta name="keywords" content="keying"> \n </head>\n <body> <br>64848744<br>54987464<br>testtintest<br> </body>\n </html>""")
              
Func.close()


## sende git path'i kurulu olmadığı için bu alttaki kısım çalışmayabilir html'i local açsan da olur
## bu kısım hem linux hem windowsta çalışıyor %100
##time.sleep(5)
##
##
##GITHUB_TOKEN = "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"
##API_URL ="https://api.github.com"
##payload = '{"name": "Testname"}'
##headers= {
##             "Authorization": "token " + GITHUB_TOKEN,
##             "Accept": "application/vnd.github.v3.json"
##}
##
##
##
##r = requests.post(API_URL+"/user/repos", data=payload, headers=headers)
##
##
##print(r.json())


##time.sleep(1)
##os.system(curl -i -u nekoslayer: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 https://api.github.com/users/nekoslayer)
##



print("done")
input()
