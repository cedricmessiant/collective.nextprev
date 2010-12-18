from zope.interface import implements
from zope.component import adapts
from Products.Archetypes.atapi import BooleanField, BooleanWidget
from Products.ATContentTypes.content import topic
from Products.ATContentTypes.interface import IATTopic
from Products.ATContentTypes import ATCTMessageFactory as _at
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.app.folder import folder

def getNextPreviousEnabled(self):
    return self.getField('nextPreviousEnabled').get(self)

def setNextPreviousEnabled(self, value):
    self.getField('nextPreviousEnabled').set(self, value)

def patch():
    topic.ATTopic.getNextPreviousParentValue = (folder.ATFolder.getNextPreviousParentValue.im_func)
    topic.ATTopic.getNextPreviousEnabled = getNextPreviousEnabled
    topic.ATTopic.setNextPreviousEnabled = setNextPreviousEnabled 
    
def unpatch():
    del topic.ATTopic.getNextPreviousParentValue
    del topic.ATTopic.getNextPreviousEnabled
    del topic.ATTopic.setNextPreviousEnabled

class ExBooleanField(ExtensionField, BooleanField):
    """ A lines field """

class TopicSchemaExtender(object):
    adapts(IATTopic)
    implements(ISchemaExtender)
        
    fields = [
        ExBooleanField('nextPreviousEnabled',
            #required = False,
            languageIndependent = True,
            schemata = 'settings',
            widget = BooleanWidget(
                description=_at(u'help_nextprevious', default=u'This enables next/previous widget on content items contained in this folder.'),
                label = _at(u'label_nextprevious', default=u'Enable next previous navigation'),
                visible={'view' : 'hidden',
                         'edit' : 'visible'},
            ),
            default_method="getNextPreviousParentValue"
        ),
    ]
    
    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
