from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class ParticleTypesParser(HTMLParser):
    """
    Parsing http://pdg8.lbl.gov/rpp2012v5/pdgLive/Viewer.action
    for particle types
    """

    detecting = False # raise this flag if inside <li>

    def handle_starttag(self, tag, attrs):
        if tag == 'li' or self.detecting:
            print "Encountered a particle type!"
            self.detecting = True
        #print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        if self.detecting:
            if tag == "li":
                self.detecting = False
            print "Encountered an end tag :", tag
    def handle_data(self, data):
        if self.detecting:
            print "Encountered some data  :", data.strip()
