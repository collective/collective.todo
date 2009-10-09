from setuptools import setup, find_packages
import os

version = '0.7'

setup(name='collective.todo',
      version=version,
      description="""Formerly Products.todo, this package aims to provide "simple" todo list functionality in Plone via a folderish (Dexterity) content type: Todo item.""",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords="""'project management' productivity""",
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='http://svn.plone.org/svn/collective/collective.todo/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      """,
      paster_plugins = ["ZopeSkel"],
      )
