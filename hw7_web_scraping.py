"""
Created on 10/18/2020

@author: Donald
"""

"""
***Question***
You are writing a simple script that determines if a user-supplied URL can be retrieved.
 Your script
should loop until the user wants to exit.
1. Prompt the user for input
a. If the input is “q”, “x”, or “exit”, end the program.
b. Any other input should be treated as a URL

2. Attempt to retrieve the URL
a. You can base your program on one of two packages; urllib.request or requests
i. urllib.request documentation:
https://docs.python.org/3/library/urllib.request.html
ii. requests documentation: https://requests.readthedocs.io/en/master

3. Print the status code
a. Only status codes of 200 indicate a successful retrieval

4. If the retrieval is successful, use the BeautifulSoup library to print out the “prettify” version of
the HTML data from the URL.
a. Documentation on the BeautifulSoup library can be found at:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
5. Make sure that nothing crashes your script – the script should only exit if the user gives one of
the exit inputs.

"""
from bs4 import BeautifulSoup
import urllib.request

print("\n***Examples of accepted url_format 'http://www.voidspace.org.uk' \
or https://google.com***")

while True:
    try:
        
        url = input("Enter url: ").strip()
        
        if url in ["q","x","exit"]:
            print("Program Ended!!")
            break
            
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        page = response.read()
        status_code = response.getcode() 
        #print(page)
        #print(type(status_code))
        if status_code == 200:
            print(20* "=")
            print("Status code: {}".format(status_code))
            print(20* "=")
            soup = BeautifulSoup(page, 'html.parser')
            print(soup.prettify())
    except Exception as e:
        print("Error encountered: {}".format(e))