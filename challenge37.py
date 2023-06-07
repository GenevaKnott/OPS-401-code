#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra, and Nick A
# https://stackoverflow.com/questions/31554771/how-can-i-use-cookies-in-python-requests

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

print("Target site is " + targetsite)
print(cookie)


# - Send the cookie back to the site and receive a HTTP response
new_response = requests.get(targetsite, cookies=cookie)

# - Generate a .html file to capture the contents of the HTTP response
page = new_response.text
with open(r'C:\Users\maldo\OneDrive\Documents\Github\Ops-401\Code\cookie.html', 'w') as file:
    file.write(page)
    
# - Open it with Firefox
webbrowser.get('firefox').open('cookie.html')
