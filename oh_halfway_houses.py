# Imports lxml's HTML parsing tools
import lxml.html
import requests


# Grabs all HTML from the page (Ohio DRC's Halfway Houses directory by region) and converts to a tree
url = "http://www.drc.ohio.gov/Public/HalfwayHouse/hwh_regions.htm"
page = requests.get(url)
tree = lxml.html.fromstring(page.content)


# Pulls the counties from the body of the page
counties = tree.xpath('//h4/text()')

for c in counties:
  print c
