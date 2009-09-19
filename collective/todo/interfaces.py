from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from Products.todo import todoMessageFactory as _

# -*- extra stuff goes here -*-

class ITodoitem(Interface):
    """Todo item"""

class ITodofolder(Interface):
    """Todo folder"""
