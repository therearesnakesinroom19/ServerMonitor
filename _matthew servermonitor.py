#!/usr/bin/env python3

"""
This program monitors the server and outputs to screen, to HTML.
"""
from rebecca import *
from matthew import *
from time import sleep

# add your import

interval = 5 * 60  # 5 minutes in seconds
speech = True

while True:
    message = "SERVER MONITOR 0.1\n"
    message += "\nUptime is " + up_time()  # rebecca
    # add your message contribution here

    html = "<html><head><title>Server Monitor Report</title></head><body>"
    html += "<h1>SERVER MONITOR 0.1</h1><hr>"
    html += "<p><b>Uptime</b> is " + up_time()  # rebecca
    # add your HTML contribution here
    html += "</body></html>"

    print(message)
    report = open("servermonitor.html", "w")
    print(html, file=report)
    report.close()

    if speech:
        speak(message + "\nThis message will self destruct in 5 seconds, 4, 3, 2, 1, boom")

    # add any testing function here

    sleep(interval)
