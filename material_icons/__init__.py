from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import etree

MYPATTERN = r'!material(\-(large))?:(\w+)'

class MaterialIconsExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(IconCreator(MYPATTERN), 'material_icons', 1)

class IconCreator(InlineProcessor):
    def handleMatch(self, m, data):
        style = ''
        if m.groups()[1] == 'large':
            style += 'font-size: 2rem;'
        el = etree.Element('i', attrib={'class': 'md-icon', 'style': style})
        el.text = m.groups()[2]
        return el, m.start(0), m.end(0)

def makeExtension(*args, **kwargs):
    return MaterialIconsExtension(*args, **kwargs)