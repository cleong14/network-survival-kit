#!/usr/bin/env python

def datacollector(mac_str, company_str, address_str)
  some_text = '\n\n====================\n\n' + mac_str + '\n' + company_str + '\n' + address_str

  fh = open('./datacollected.txt', 'a+')

  fh.writelines(some_text)

  fh.close()

  fh_reopen = open('./datacollected.txt', 'r')

  contents = fh_reopen.read()

  print(contents)