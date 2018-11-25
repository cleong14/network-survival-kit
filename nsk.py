#!/usr/bin/env python

import argparse
import modules.macaddresslookup as ml

def maclookup(args):
  print('MACLOOKUP ARGS', args)
  ml.maclookup(args.mac[0])

  if args.o == '--output' || args.o == '-O':
    print('OUTPUT PLEASE')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='Network Survival Kit', description='Command line network toolkit')

  subparsers = parser.add_subparsers(help='Module specific utilities')

  # maclookup parser
  parser_maclookup = subparsers.add_parser('maclookup', help='Perform mac address lookup')
  parser_maclookup.add_argument('mac', nargs=1, help='Target mac address')
  parser.maclookup.add_argument('o', nargs=1, help='File name to write results to')
  parser_maclookup.set_defaults(func=maclookup)

  args = parser.parse_args()
  args.func(args)
  print('Arguments: {}'.format(args))