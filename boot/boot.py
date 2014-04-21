#!/usr/bin/env python

import os, json
import urllib2
import subprocess
import yaml
from wifi import *

import vocabcompiler

def say(phrase, OPTIONS = " -vdefault+m3 -p 40 -s 160 --stdout > say.wav"):

    os.system("espeak " + json.dumps(phrase) + OPTIONS)
    os.system("aplay -D hw:1,0 say.wav")



def configure():
    try:

        print "COMPILING DICTIONARY"
        vocabcompiler.compile()

        print "STARTING CLIENT PROGRAM"

        try:
            os.system("/home/pi/jasper/client/start.sh &")
        except:
            os.system("/home/pi/jasper/backup/start.sh &")
        finally:
            return

   
if __name__ == "__main__":
    print "==========STARTING BUDDYBOT=========="
    print "=========================================="
    say("Hello.... I am Buddybot... Please wait one moment.")
    configure()
