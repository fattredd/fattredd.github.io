# Salty API bitch
import requests, pickle
from BeautifulSoup import BeautifulSoup
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
resp = br.open('http://saltybet.com/authenticate?signin=1')
soup = BeautifulSoup(resp.get_data())
resp.set_data(soup.prettify())
br.set_response(resp)
br.select_form(nr=0)
br['email'] = 'dome@mailinator.com'
br['pword'] = '12345'
returns = br.submit()
resp = br.open('http://saltybet.com')
page = BeautifulSoup(resp.read())
