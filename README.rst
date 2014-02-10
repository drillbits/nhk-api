=======
nhk-api
=======

.. image:: https://drone.io/github.com/drillbits/nhk-api/status.png
   :target: https://drone.io/github.com/drillbits/nhk-api/latest

Python client for NHK API.

Requirements
============

- Python 3.3

Installation
============

::

   $ pip install nhk-api

Usage
=====

::

   from datetime import date
   from nhk import ProgramGuide
   
   
   client = ProgramGuide(api_key='YOUR_API_KEY')
   
   # Get program list
   # http://api-portal.nhk.or.jp/doc_list-v1_con
   program_list = client.pg_list('130', 'g1', date.today())
   # or
   # program_list = client.pg_list('東京', 'ＮＨＫ総合１', date.today())
   
   # Get program list by genre
   # http://api-portal.nhk.or.jp/doc_genre-v1_con
   program_list_by_genre = client.pg_genre('130', 'g1', '0700', date.today())
   # or
   # program_list_by_genre = client.pg_genre('東京', 'ＮＨＫ総合１', 'アニメ／特撮(国内アニメ)', date.today())
   
   # Get program information
   # http://api-portal.nhk.or.jp/doc_info-v1_con
   program_info = client.pg_info('130', 'g1', '2014021499999')
   # or
   # program_info = client.pg_info('東京', 'ＮＨＫ総合１', '2014021499999')
   
   # Get information of program that is broadcasting now
   # http://api-portal.nhk.or.jp/doc_now-v1_con
   program_now = client.pg_now('130', 'g1')
   # or
   # program_now = client.pg_now('東京', 'ＮＨＫ総合１')
