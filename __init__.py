from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests # for curl
import xml.etree.ElementTree as ET #xml parser

# General Variables
host = '192.168.88.22'
# Plex Variables
XPlexToken = 'aW9gR8bPYbbpsQzZ3m7q'
# Radarr Variables
radarr_port = '7878'
radarr_api_key = '528d3d2326734853a39d6a38feec02d0'

class TemplateSkill(MycroftSkill):

    def __init__(self):
        super(TemplateSkill, self).__init__(name="TemplateSkill")
        self.test = ''

    @intent_handler(IntentBuilder("").require("AddMovie"))
    def handle_addamovie_intent(self, message):
        self.speak_dialog("which.movie")
        #self.speak_dialog("which.movie")
        #r = self.get_response('which.movie', num_retries=1)
        #print(r)
        # params = (
        #     ('X-Plex-Token', XPlexToken),
        # )
        # response = requests.get('http://' + host + ':32400/library/sections/1/refresh', params=params)
        
        

    @intent_handler(IntentBuilder("").require("RefreshPlex"))
    def handle_refreshplex_intent(self, message):
        params = (
            ('X-Plex-Token', XPlexToken),
        )
        response = requests.get('http://' + host + ':32400/library/sections/1/refresh', params=params)
        
        self.speak_dialog("refreshing.plex")

    @intent_handler(IntentBuilder("").require("CountMovies"))
    def handle_countmovies_intent(self, message):
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
