__version__ = "0.2.4"
from geograpy_new.extraction import Extractor
from geograpy_new.places import PlaceContext
from geograpy_new.locator import Locator
from geograpy_new.labels import Labels

# Cell
def get_place_context(url=None, text=None,labels=Labels.default, debug=False):
    '''
    Get a place context for a given text with information
    about country, region, city and other
    based on NLTK Named Entities in the label set Geographic(GPE), 
    Person(PERSON) and Organization(ORGANIZATION).
    
    Args:
        url(String): the url to read text from (if any)
        text(String): the text to analyze
        debug(boolean): if True show debug information
    
    Returns:
        pc: 
            PlaceContext: the place context
    '''
    e = Extractor(url=url, text=text,debug=debug)
    e.find_entities(labels=labels)
    places=e.places
    pc = PlaceContext(places)
    pc.setAll()
    return pc

# Cell
def locateCity(location,correctMisspelling=False,debug=False):
    '''
    locate the given location string
    Args:
        location(string): the description of the location
    Returns:
        Locator: the location
    '''
    e = Extractor(text=location,debug=debug)
    e.split()
    loc=Locator.getInstance(correctMisspelling=correctMisspelling,debug=debug)
    city=loc.locateCity(e.places)
    return city