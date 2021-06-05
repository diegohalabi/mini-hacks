# download photos from NASA and generate an html file, coding = utf-8
__author__ = 'Diego Halabi'

# load libraries
import json
import requests

key = input('Enter your API Key:\n')

def req(requested_url):
  params_nasa = {'api_key': key}
  response = requests.request('GET', requested_url, params = params_nasa)
  return json.loads(response.text)

data_nasa = req('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos')['latest_photos'][:15]

# generate web
def build_web_page(data):
  html = '<html>\n<head>\n</head>\n<body>\n<ul>\n'
  html_below = '</ul>\n</body>\n</head>\n</html>'
  for photo in data_nasa:
    html += '\t<li><img src="{}"></li>\n'.format(photo['img_src'])
  html += html_below
  with open('output.html', 'w') as f:
    f.write(html)

# build web
build_web_page(data_nasa)
print('Done!')