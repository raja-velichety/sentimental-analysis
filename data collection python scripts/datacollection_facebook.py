# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:51:19 2019

@author: Raja Ravichandra
"""

import requests # pip install requests
import json

base_url = 'https://graph.facebook.com/me'
ACCESS_TOKEN      = 'EAAF89mZC2SzIBAAUbkok7eqZAxmqRjK8XTCZCTuUg8FlnTZBejjFj381JAHLxnLULUpZB9bSdTXLsyymZBhnbbkG3xETVnW1y6M72njbcccroHsZCWuRp76jPExrzZCTODm4ls6CltqwyGDOWYOrjLa1YgQP014CZA7mb3vuW6ZCYGoAxLIRWrOq3sIN7BVGVDzAjgzSla5V2O2T2qqVZADneII'
        
# Specify which fields to retrieve
fields = 'id,name,likes.limit(10){about}'

url = '{0}?fields={1}&access_token={2}'.format(base_url, fields, ACCESS_TOKEN)

# This API is HTTP-based and could be requested in the browser,
# with a command line utlity like curl, or using just about
# any programming language by making a request to the URL.
# Click the hyperlink that appears in your notebook output
# when you execute this code cell to see for yourself...
print(url)

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
print(json.dumps(content, indent=1))