headsup
=======

HTML Header Updater written in Python

What is headsup?
----------------

Headsup is a script I wrote to automatically update all 'headers' for HTML documents in a single project, basing off a template.html file. 
Most HTML documents (should be) are written in the format 
1. Header
2. Main
3. Footer
Since all documents in a single project generally have the same header, and footer, they can be homogenised into a single template.html file, which you can then update and then apply to all using this tool! This saves you from having to make individual changes and/or copy-paste the document yourself. 
I wrote it in Python because I'm familiar with the syntax and plugins involved, and I wanted a quick and easy solution. 

How to use
----------------------

Headsup requires Python (should work on 2.x and 3.x) as well as the BeautifulSoup4 library, so be sure to install those before you give it a go. 
Pending a UI release, all optional settings must be changed through the setHeaders.py file, but here's a list of things you can change:
- header: defines the div id that you use to enclose your header in both the template and project pages (default: "header")
- sourceHeaderName: defines the template HTML document that you use as source for header to be applied (default: "template.html")
