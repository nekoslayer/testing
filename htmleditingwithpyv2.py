import os
import re
import time
import requests
import base64
from github import Github
from github import InputGitTreeElement


##buraya webhooktan gelen bilgileri alıp hwidiyle keyini matchleyip var olan key'i değiştirecek kod gerekiyor


##Func = open("index.html","w")
##   
##Func.write("""<head>\n<title>testsite</title>\n<meta name="description" content="keys goes here">\n<meta name="keywords" content="keying">\n</head>\n<body>\nişeyarıyormu<br>64848744<br>54987464<br>testtintest<br>\n</body>\n</html>""")
##              
##Func.close()


## bu kısım hem linux hem windowsta çalışıyor %100
time.sleep(5)


user = "nekoslayer"
password = "315269babaananısiksin"
g = Github(user,password)
repo = g.get_user().get_repo('git-test') # repo name
file_list = [
    "C:\\Users\gorke\Desktop\finalgit\index.html"]


file_names = [
    'index.html']

commit_message = 'uptating'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)
print("hey")





##time.sleep(1)
##os.system(curl -i -u nekoslayer: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 https://api.github.com/users/nekoslayer)
##



print("done")
input()
