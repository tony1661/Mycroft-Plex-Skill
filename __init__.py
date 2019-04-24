from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl
import xml.etree.ElementTree as ET #xml parser

class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")
        self.count = 0


    @intent_handler(IntentBuilder("").require("RefreshPlex"))
    def handle_refreshplex_intent(self, message):
        params = (
            ('X-Plex-Token', 'aW9gR8bPYbbpsQzZ3m7q'),
        )

        response = requests.get('http://192.168.88.22:32400/library/sections/1/refresh', params=params)
        print(str(response) + "Refreshed")
        self.speak_dialog("refreshing.plex")

    @intent_handler(IntentBuilder("").require("CountMovies"))
    def handle_refreshplex_intent(self, message):
        params = (
            ('X-Plex-Token', 'aW9gR8bPYbbpsQzZ3m7q'),
        )

        response = requests.get('http://192.168.88.22:32400/library/sections/1/all', params=params)
        print(response)
        self.speak_dialog("you.have.count.movies", data={"count": self.count})

def create_skill():
    return TemplateSkill() 
