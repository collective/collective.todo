"""Definition of the Todo item content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
#from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.todo import todoMessageFactory as _
from Products.todo.interfaces import ITodoitem
from Products.todo.config import PROJECTNAME

TodoitemSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
#    atapi.BooleanField(
#        name='done',
#        storage = atapi.AnnotationStorage(),
#        required=False,
#        #searchable=1,
#        #default='',
#        #schemata ='default',
#        widget=atapi.BooleanWidget(
#            label=_(u"Done"),
#            #description=_(u"Done?"),
#        ),
#    ),

    atapi.TextField(
        name='notes',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        #default='',
        #schemata ='default',
        widget=atapi.RichWidget(
            description=_(u"Notes for this todo item."),
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TodoitemSchema['title'].storage = atapi.AnnotationStorage()
TodoitemSchema['title'].widget.label = 'Todo'
TodoitemSchema['description'].storage = atapi.AnnotationStorage()
TodoitemSchema['description'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}

schemata.finalizeATCTSchema(TodoitemSchema, moveDiscussion=False)

class Todoitem(folder.ATFolder):
    """Description of the Example Type"""
    implements(ITodoitem)

    portal_type = "Todo item"
    meta_type = "Todo item"
    schema = TodoitemSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(Todoitem, PROJECTNAME)
