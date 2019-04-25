from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl
import xml.etree.ElementTree as ET #xml parser

# Variables
XPlexToken = 'aW9gR8bPYbbpsQzZ3m7q'
host = '192.168.88.22'

class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")


    @intent_handler(IntentBuilder("").require("RefreshPlex"))
    def handle_refreshplex_intent(self, message):
        params = (
            ('X-Plex-Token', XPlexToken),
        )
        response = requests.get('http://' + host + ':32400/library/sections/1/refresh', params=params)
        
        self.speak_dialog("refreshing.plex")

    @intent_handler(IntentBuilder("").require("CountMovies"))
    def handle_refreshplex_intent(self, message):
        count = 0
        params = (
            ('X-Plex-Token', XPlexToken),
        )
        response = requests.get('http://' + host + ':32400/library/sections/1/all', params=params)
        root = ET.fromstring(response.content)
        
        for video in root.findall('Video'):
            count = count + 1
        
        self.speak_dialog("you.have.count.movies", data={"count": count})

def create_skill():
    return TemplateSkill() 
