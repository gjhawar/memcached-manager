'''
Created on Jul 14, 2010

@author: nick
'''
from distutils.core import setup
import MemcachedManager.Main

setup(name="Memcached Manager",
      version=MemcachedManager.Main.__version__,
      description="Memcached Server Manager allows you to view stats about your Memcached cluster and Manage the data in that cluster and much more.",
      author="Nick Verbeck",
      author_email="nerdynick@gmail.com",
      url="http://code.google.com/p/memcached-manager",
      packages=['MemcachedManager', 'MemcachedManager.Tabs','MemcachedManager.memcached','MemcachedManager.Dialogs'],
      scripts=['scripts/MemcachedManager'],
      package_data={'MemcachedManager': ['Icons/Active.png',
                        'Icons/Add.png',
                        'Icons/Globe.png',
                        'Icons/Remove.png',
                        'Icons/UnActive.png']}
      )