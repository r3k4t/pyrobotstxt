import urllib3
import pyfiglet
banner=pyfiglet.figlet_format("PyRobotsTxt",font="standard")
print(banner)
print("             Author : Rahat Khan Tusar(rkt)")
print("             Github : https://github.com/r3k4t")
print
url=raw_input("Enter a url(Ex:https://google.com/robots.txt) : ")
https=urllib3.PoolManager()
robots_txt=https.request('GET',url)
print
print(robots_txt.data)
raw_input(chr(27)+"[32m"+"Press Enter Key To Exit.......")



