from html.parser import HTMLParser

TAG_NEW_ENTRY="tr"
TAG_NEW_FIELD="td"

ENTRY_INTERESTED_ATTR="class"
ENTRY_INTERESTED_VALS=["odd", "even"]

FIELD_INTERESTED_ATTR="class"
FIELD_INTERESTED_CLASS_PREFIX="views-field-"

class RosterHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._entries = []
        self._current_key = None
        self._current_entry = None

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag, attrs)
        for (a, val) in attrs:
            if tag == TAG_NEW_ENTRY and a == ENTRY_INTERESTED_ATTR:
                if val in ENTRY_INTERESTED_VALS:
                    self._current_entry = {}

            if tag == TAG_NEW_FIELD and a == FIELD_INTERESTED_ATTR:
                for prop in val.split():
                    if prop.startswith(FIELD_INTERESTED_CLASS_PREFIX):
                        self._current_key = prop[len(FIELD_INTERESTED_CLASS_PREFIX):]

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        if tag == TAG_NEW_ENTRY and self._current_entry:
            self._entries.append(self._current_entry)
            self._current_entry = None

    def handle_data(self, data):
        #print("Encountered some data  :", data, html.unescape(data))
        if not data.strip():
            return

        if self._current_entry is not None:
            if self._current_key not in self._current_entry:
                self._current_entry[self._current_key] = data.strip()
            else:
                self._current_entry[self._current_key] += "; " + data.strip()

def parse(fp):
    parser = RosterHTMLParser()
    parser.feed(fp.read())
    return parser._entries
