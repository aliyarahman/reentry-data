# Imports lxml's HTML parser, regex, and request tools
import lxml.html
import requests
import re

# Grabs all HTML from the page (Ohio DRC's Halfway Houses directory by region) and converts to a tree
url = "http://www.drc.ohio.gov/Public/HalfwayHouse/hwh_regions.htm"
page = requests.get(url)
tree = lxml.html.fromstring(page.content)


# Gets the counties from the body of the page
counties = tree.xpath('//h4/text()')

# Gets the HWH names
houses_dirty = tree.xpath("//table//tr[1]//a/text()")

for h in houses_dirty:
     house = {}
     house['name'] = re.sub('\s+',' ',h).strip()
     print house['name']