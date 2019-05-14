## Plex Mycroft Skill
Control Plex using Mycroft

## Description 
A custom Mycroft skill I created to control my plex server.

## Installation
Installation can be done through the mycroft website or via the linux shell:

cd /opt/mycroft/skills/
git clone https://github.com/tony1661/Mycroft-Plex-Skill.git
sudo chown mycroft:mycroft Mycroft-Plex-Skill/*


## Configurations
To get your Movies and TV ID numbers use the following command:
* curl --request GET "http://ip-address:32400/library/sections?X-Plex-Token=token"

## Examples 
* "Refresh Plex"
* "How many movies do I have downloaded?"
* "count my movies"
* "how many movies do I have"
* "how many movies do I have downloaded"
* "how many movies do I have on plex"

## Credits 
Tony Fernandez
