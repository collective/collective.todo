
from Products.CMFCore.utils import getToolByName

import logging
logger = logging.getLogger('Products.todo')

def changeWorkflowStates(todo, event):

    wf = getToolByName(todo, 'portal_workflow')
    items = todo.ZopeFind(todo, obj_metatypes=['Todo item',], search_sub=1)
    for item in items:
        review_state = wf.getInfoFor(item[1], 'review_state')
        if review_state == 'not_done':
            wf.doActionFor(item[1],'done',wf_id='todo_list_workflow')
            logger.info('Marking %s as done.' % item[0])
