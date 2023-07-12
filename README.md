python-yt-downloader

Simple Youtube downloader app in Python.

Simply write in your CLI python3 yt-downloader.py "youtube video url".

In Pytube version 15.0.0, you just need to remove ; in line 287 of cipher.py file.

Change r'var {nfunc}\s*=\s*(\[.+?\];)'.format( to r'var {nfunc}\s*=\s*(\[.+?\])'.format(
