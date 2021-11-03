# -*- coding: utf-8 -*-

# author : cosrah

import requests

class FameAPICli:
    ENDPOINT = 'Server_URL'
    FAME_API_KEY = 'API_KEY'
    
    headers = {
        'Accept': "application/json",
        'X-API-KEY': FAME_API_KEY
    }
    
    params = {
        'options[allow_internet_access]':  "on",
        'options[magic_enabled]': "on",
        'options[analysis_time]': "300",
        'groups': "cert"
    }
    
    ###################################################
    
    def __init__(self, ENDPOINT=None, API_KEY=None):
        if ENDPOINT: self.ENDPOINT = ENDPOINT
        if API_KEY: self.FAME_API_KEY = API_KEY
    
    ###################################################
    # Only the submit API has been implemented.
    
    def submit(self, params, files=None):
        r = requests.post(self.ENDPOINT + 'analyses/', data=params, files=files, headers=self.headers)

        status_code = r.status_code
        if status_code != 200:
            return r.status_code, {'error_msg' : r.text}
        else:
            return r.status_code, r.json()
    
    def submit_file(self, filepath):
        res = None
        with open(filepath, 'rb') as f:
            files = {'file': f}
            res = self.submit(self.params, files)
        return res
            
    def submit_url(self, url):
        params = self.params.copy()
        params['url'] = url
        return self.submit(params)

    ###################################################

def submit_file(filepath):
    cli = FameAPICli()
    return cli.submit_file(filepath)

def submit_url(url):
    cli = FameAPICli()
    return cli.submit_url(url)

def main():
    pass

if __name__ == '__main__':
    main()
