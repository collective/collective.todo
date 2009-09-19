"""Define a browser view for the 'Todo item' content type. In the FTI 
configured in profiles/default/types/*.xml, this is being set as the default
view of that content type.
"""

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Todo_itemView(BrowserView):
    """Default view of a Todo item
    """

    __call__ = ViewPageTemplateFile('todoitem.pt')

    def folder_listing(self):
        results = ''
        for i in self.context.objectIds():
            obj = self.context.unrestrictedTraverse('/'.join(self.context.getPhysicalPath()) + '/' + i)
            url = obj.absolute_url()
            num = self.getNum(obj)
            title = obj.Title()
            wftool = self.context.portal_workflow
            state = wftool.getInfoFor(obj, 'review_state')
            if not state == 'done':
                results += ("<li><a href='%s'>%s</a><span class='discreet'> (%s sub-item(s))</span></li>" % (url,title,num))
            else:
                results += ("<li><a href='%s'><strike>%s</strike></a><span class='discreet'> (%s sub-item(s))</span></li>" %
                    (url,title,num))
        return results
    
    def getNum(self, obj):
        num = 0
        wftool = self.context.portal_workflow
        for item in obj.objectIds(): 
            o = self.context.unrestrictedTraverse('/'.join(self.context.getPhysicalPath()) +
                '/' + obj.getId() + '/' + item)
            state = wftool.getInfoFor(o, 'review_state')
            if state is not 'done':
                num += 1
        
        return num

