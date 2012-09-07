import requests
from parser import ParticleTypesParser

r = requests.get('http://pdg8.lbl.gov/rpp2012v5/pdgLive/Viewer.action')

parser = ParticleTypesParser()
parser.feed(r.text)