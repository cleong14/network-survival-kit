import urllib.request as urllib2
import json
import codecs
import time

def maclookup(maclookup_args):
  if maclookup_args.timer == True:
    # start timer
    start_time = time.time()

    print('Timer started...\n')
  
  print('MACLOOKUP ARGS', maclookup_args)
  # API URL
  url = 'https://macvendors.co/api/'

  # Mac address to lookup from vendor
  request = urllib2.Request(url + maclookup_args.mac[0], headers={'User-Agent': 'API Browser'})
  response = urllib2.urlopen(request)

  # Fix: json object must be str, not 'bytes
  reader = codecs.getreader('utf-8') # codecs module to decode response into str
  obj = json.load(reader(response)) # decode returned API response

  company_mac = 'Company MAC: ' + maclookup_args.mac[0]

  company_name = 'Company name: ' + obj['result']['company']

  company_address = 'Company address: ' + obj['result']['address']

  # Print company mac
  print(company_mac)

  # Print company name
  print(company_name)

  # Print company address
  print(company_address)

  if maclookup_args.timer == True:
    # total elapsed runtime
    elapsed_time = time.time() - start_time
    formatted_time = "{:.2f}".format(elapsed_time)

    print('Timer finished...\n')
    print('ELAPSED TIME', formatted_time)

  if maclookup_args.output != 0:
    output_text = '\n\n====================\n\n' + company_mac + '\n' + company_name + '\n' + company_address

    if maclookup_args.timer == True:
      output_text = '\n\n====================\n\n' + company_mac + '\n' + company_name + '\n' + company_address + '\n\n' + 'Total elapsed runtime: ' + str(formatted_time) + ' ms'

    output_file = open(maclookup_args.output[0], 'a+')

    output_file.writelines(output_text)

    output_file.close()

    output_file_reopen = open(maclookup_args.output[0], 'r')

    contents = output_file_reopen.read()

    print(contents)