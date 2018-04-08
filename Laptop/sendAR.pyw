import urllib.request, urllib.parse, sys
url = "https://autoremotejoaomgcd.appspot.com/sendmessage?key=[redacted]&message={}&sender=CLIP"
#f=open('clip.txt')
#message = f.read()
#f.close()
try:
    message = sys.argv[1]
    message = urllib.parse.quote(message,"")
    urllib.request.urlopen(url.format(message))
except Exception as e:
    f=open('err.txt','w')
    f.write(str(e))
    f.close()
