"""Define a browser view for the 'Todo folder' content type. In the FTI 
configured in profiles/default/types/*.xml, this is being set as the default
view of that content type.
"""

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.content.browser.foldercontents import FolderContentsView

class Todo_list_toolView(BrowserView):
    """Todo list tool view
    """

    __call__ = ViewPageTemplateFile('todo_list_tool.pt')

    def label(self):
        return 'Todo list preferences'

    def description(self):
        return 'This preference panel allows you to configure your todo list (coming soon).'
