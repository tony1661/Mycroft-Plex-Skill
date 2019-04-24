from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl

class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")


    @intent_handler(IntentBuilder("").require("RefreshPlex"))
    def handle_refreshplex_intent(self, message):
        params = (
            ('X-Plex-Token', 'aW9gR8bPYbbpsQzZ3m7q'),
        )

        response = requests.get('http://192.168.88.22:32400/library/sections/1/refresh', params=params)
        print(str(response) + "Refreshed")
        self.speak_dialog("refreshing.plex")

def create_skill():
    return TemplateSkill()
