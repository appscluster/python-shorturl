# -*- coding: utf-8 -*-
# URL shortener using short url services.
# Created By Abdul Hamid
# 06 March 2014
# ah@appscluster.com

import sys, time, os.path, getopt, socket
import urllib2, urllib

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36'}
HEADERS_MOBILE = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

MAX_ATTEMPTS = 3
VERSION = '0.0.4'

class ShortUrlPy():
    """docstring for ShortUrlPy"""
    def __init__(self, **arg):
        self.arg = arg

    def ShortenUrl(self, url, default='Any', login='', apikey=''):

        api_service = ''
        result=url
        for attempt in range(MAX_ATTEMPTS):
            if ((attempt==0 and default=='Any') or default=='tinyurl'):
                url_data = {'url': url}
                api_service = 'http://tinyurl.com/api-create.php'
            elif (default=='is.gd'):
                url_data = {'format':'simple', 'url': url}
                api_service = 'http://is.gd/create.php'
            elif (default=='bitly'):
                url_data = {'format':'txt', 'login': login, 'apiKey': apikey, 'longUrl': url}
                api_service = 'http://api.bit.ly/v3/shorten'
            else:
                url_data = {'format':'simple', 'url': url}
                api_service = 'http://is.gd/create.php'
            short_url = self.ProcessUrl(api_service, url_data).strip()

            if (short_url[:4]=='http'):
                result=short_url
                break
        
        return result

    def ProcessUrl(self, shorten_url, url_data):
        response = ''
        try_mobile_header=False
        url_data = urllib.urlencode(url_data)
        for attempt in range(MAX_ATTEMPTS):
            if (attempt==1):
                time.sleep(2)
            try:
                if (try_mobile_header==False):
                    req = urllib2.Request(url=shorten_url, data=url_data, headers=HEADERS)
                else:
                    req = urllib2.Request(url=shorten_url, data=url_data, headers=HEADERS_MOBILE)
                response = urllib2.urlopen(req, timeout=(5+attempt)).read()
                break
            except urllib2.URLError, e:
                sleep_secs = attempt ** 2
                print >> sys.stderr, 'ERROR: %s.\nRetrying in %s seconds...' % (e, sleep_secs)
                time.sleep(sleep_secs)
                if (attempt>2):
                    try_mobile_header=True
            except Exception, e:
                sleep_secs = attempt ** 2
                print >> sys.stderr, 'ERROR: %s.\nRetrying in %s seconds...' % (e, sleep_secs)
                time.sleep(sleep_secs)
                try_mobile_header=True
            except socket.timeout as e:
                sleep_secs = attempt ** 2
                print >> sys.stderr, 'ERROR: %s.\nRetrying in %s seconds...' % (e, sleep_secs)
                time.sleep(sleep_secs)
                try_mobile_header=True
        return response


def main(argv):
    url = None
    default = 'Any'
    login = ''
    apikey = ''
    try:
        script_file = os.path.basename(__file__)
        output = '\nPython URL shortener, Created By Abdul Hamid, 6 March 2014, Version:'+VERSION
        output+= '\nLast Modified 30 January 2016'
        output+= '\nEmail: ah@appscluster.com\n'
        output+= '\nUsage: '+script_file+' [-u] [-d] [-l] [-a]'
        output+= '\nOptions: \n'
        output+= '\n  -u  --url        Full URL http://www.google.co.uk'
        output+= '\n  -d  --default    Any, tinyurl, is.gd, bitly'
        output+= '\n  -l  --login      bitly Login'
        output+= '\n  -a  --apikey     bitly apikey'
        output+= '\n\nExamples:\n'
        output+= '\n  default: '+script_file+' -u http://www.appscluster.com'
        output+= '\n  tinyurl: '+script_file+' -u http://www.appscluster.com -d tinyurl'
        output+= '\n  is.gd: '+script_file+' -u http://www.appscluster.com -d is.gd'
        output+= '\n  bitly: '+script_file+' -u http://www.appscluster.com -d bitly -l xyz -a zyx_key \n'
        opts, args = getopt.getopt(argv,"hu:d:l:a:",["url=", "default=", "login=", "apikey="])
    except getopt.GetoptError, e:
        print 'ERROR: ', e
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print output
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-d", "--default"):
            default = arg
        elif opt in ("-l", "--login"):
            login = arg
        elif opt in ("-a", "--apikey"):
            apikey = arg
    
    if (url!=None and url[:4]=='http'):
        loadurl = ShortUrlPy()
        print loadurl.ShortenUrl(url, default, login, apikey)
    else:
        print 'ERROR: Please make sure the url is fully formed eg. http://www.google.co.uk\n'
        raw_input("Press Enter to continue...")
        print output

if __name__ == '__main__':
    main(sys.argv[1:])
