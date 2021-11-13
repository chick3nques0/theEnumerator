#!/usr/bin/env python3

import whois
import pydig

cmd = input('CMD: ')

if(cmd == 'whois'):
    domain = input('Domain: ')
    whoisQ = whois.query(domain)
    info_dict = whoisQ.__dict__

    print('Name: ', info_dict['name'])
    print('Registrar: ', info_dict['registrar'])
    print('Country: ', info_dict['registrant_country'])
    print('Registered on: ', info_dict['creation_date'])
    print('Expires on: ', info_dict['expiration_date'])
    print('Status: ', info_dict['status'])
    print('DNSSEC: ', info_dict['dnssec'])
    print('Name servers: ', info_dict['name_servers'])
    print('Registrant: ', info_dict['registrant'])

elif (cmd == 'dig'):
       domain = input('Domain: ')
       digQ = pydig.query(domain, '#query')
