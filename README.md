
===============
Python-ShortUrl
===============

A python library to shorten urls using one of three url shortening services

Supports the following services:

    -tinyurl.com
    -bit.ly, j.mp, bitly.com (must use login and apikey)
    -is.gd

Installation
============

To install Python-ShortUrl:

    python setup.py install

Usage
=====

Usage: shorturlpy.py [-u] [-d] [-l] [-a]

Options:

    -u  --url        Full URL http://www.google.co.uk
    -d  --default    Any, tinyurl, is.gd, bitly
    -l  --login      bitly Login
    -a  --apikey     bitly apikey

Examples:

    default: shorturlpy.py -u http://www.appscluster.com
    
    tinyurl: shorturlpy.py -u http://www.appscluster.com -d tinyurl
    
    is.gd: shorturlpy.py -u http://www.appscluster.com -d is.gd

    bitly: shorturlpy.py -u http://www.appscluster.com -d bitly -l xyz -a zyx_key
