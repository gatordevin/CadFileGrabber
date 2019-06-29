import requests, zipfile, StringIO
r = requests.get('https://www.gobilda.com/content/step_files/1120-0001-0048.zip', stream=True)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall()
print(r)