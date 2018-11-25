import urllib.request as urllib2
import json
import codecs

def maclookup(mac_address):
  # API URL
  url = 'https://macvendors.co/api/'

  # Mac address to lookup from vendor
  address = mac_address # grab mac address from user

  request = urllib2.Request(url + address, headers={'User-Agent': 'API Browser'})
  response = urllib2.urlopen(request)

  # Fix: json object must be str, not 'bytes
  reader = codecs.getreader('utf-8') # codecs module to decode response into str
  obj = json.load(reader(response)) # decode returned API response

  # Print company name
  print('Company name: ' + obj['result']['company'])

  # Print company address
  print('Company address: ' + obj['result']['address'])