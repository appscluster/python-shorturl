
===============
Python-ShortUrl 0.0.4
===============

A python library to shorten urls using one of three url shortening services

Supports the following services:

    -tinyurl.com
    
    -bit.ly, j.mp, bitly.com (must use login and apikey)
    
    -is.gd


Installation
============

To install Python-ShortUrl:

    pip install python-shorturl


Alternatively:

    wget https://github.com/appscluster/python-shorturl/archive/master.zip

    7z x master.zip ( if you don't have 7z : sudo apt-get install p7zip-full )

    cd python-shorturl-master/

    python setup.py install


Usage
=====

Command line:

Usage: shorturlpy.py [-u] [-d] [-l] [-a]

Options:

    -u  --url        Full URL http://www.google.co.uk
    -d  --default    Any, tinyurl, is.gd, bitly
    -l  --login      bitly Login
    -a  --apikey     bitly apikey

Examples:
    
    default: 
    python -m shorturlpy.shorturlpy -u http://www.appscluster.com
    
    tinyurl: 
    python -m shorturlpy.shorturlpy -u http://www.appscluster.com -d tinyurl
    
    is.gd: 
    python -m shorturlpy.shorturlpy -u http://www.appscluster.com -d is.gd

    bitly: 
    python -m shorturlpy.shorturlpy -u http://www.domain.co -d bitly -l xyz_login -a zyx_key

    Note: replace xyz_login and zyx_key with your own bitly account details


Within your application:

    import shorturlpy
    
    loadurl = shorturlpy.ShortUrlPy()
    
    print loadurl.ShortenUrl('http://www.appscluster.com')

    print loadurl.ShortenUrl('http://www.appscluster.com', 'tinyurl')

    print loadurl.ShortenUrl('http://www.appscluster.com', 'is.gd')

    print loadurl.ShortenUrl('http://www.appscluster.com', 'bitly', 'xyz_login', 'zyx_key')

    Note: replace xyz_login and zyx_key with your own bitly account details
    
Tested on Python 2.7

Developed by Abdul Hamid https://twitter.com/AbdulHamidCEO
