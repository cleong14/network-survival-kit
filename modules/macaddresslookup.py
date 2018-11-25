import urllib.request as urllib2
import json
import codecs

def maclookup(mac_address):
  # API URL
  url = 'https://macvendors.co/api/'

  # Mac address to lookup from vendor
  request = urllib2.Request(url + mac_address, headers={'User-Agent': 'API Browser'})
  response = urllib2.urlopen(request)

  # Fix: json object must be str, not 'bytes
  reader = codecs.getreader('utf-8') # codecs module to decode response into str
  obj = json.load(reader(response)) # decode returned API response

  company_mac = 'Company MAC: ' + mac_address
  company_name = 'Company name: ' + obj['result']['company']
  company_address = 'Company address: ' + obj['result']['address']

  # Print company name
  print(company_name)

  # Print company address
  print(company_address)