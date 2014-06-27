GFI Dashboard
=============

Use API calls to get XML Data out of GFI RMM, extract what we need
and display on a custom dashboard.

Requires:
---------
- Python (2 or 3)

- Beautiful Soup 4
- 

To run:
-------

- python printOverdueServers.py path-to-xml-file
- -   {u'CLIENTTWO': {u'SITENAMETWO': [u'SERVERTWO']}, u'CLIENTONE': {u'SITENAME1': [u'SERVERNAMEONE', u'SERVERNAMETWO']}}
- python printFailedCheck.py path-to-xml-file CHECKID (CHECKID currently: 1001(AV),1002(Backup),1020(CryptoLockerGPO)
- -   {'workstation': 2, 'server': 1}


TODO:
-----

Build dashboard to read in this data and display on a monitor
