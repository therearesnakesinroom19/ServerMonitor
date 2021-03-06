#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""
from shutdown import *
from time import sleep
# add your import

interval = 5 * 60 # 5 minutes in seconds

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\n Shutdown " + str(shut_down("shut")) # Daniel

    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><b>Shutdown </b> is " + str(shut_down("shut")) # Daniel

    # add your HTML contribution here
    html += "</body></html>"

    print(message)
    report = open("shutdown.html", "w")
    print(html, file=report)
    report.close()

    # add any testing function here

    sleep(interval)