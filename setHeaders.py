from bs4 import BeautifulSoup
import os
#establishes what the header tag should be
headerTag = 'header'
#establishes source file name to read the header from
sourceHeaderName = "template.html"
f = open(sourceHeaderName)
soup = BeautifulSoup(f.read())
f.close()
headerToBeApplied = soup.find("div", {"id":headerTag})
#gets all html docs in current directory
htmlFiles = [file for file in os.listdir(".") if file.endswith(".html")]
if sourceHeaderName in htmlFiles:
	htmlFiles.remove(sourceHeaderName)
for htmlFile in htmlFiles:
	g = open(htmlFile, 'r')
	doc = BeautifulSoup(g.read())
	g.close()
	#get current header on page
	currentHeader = doc.find("div", {"id":headerTag})
	#yolo
	currentHeader.replace_with(headerToBeApplied)
	#Reopens file so it can be rewritten and not just appended to!
	g = open(htmlFile, 'w')
	g.write(unicode(doc))
	g.close()




