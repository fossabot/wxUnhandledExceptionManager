[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcforgeard%2FwxUnhandledExceptionManager.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcforgeard%2FwxUnhandledExceptionManager?ref=badge_shield)

Unhandled exception manager for wxPython
========================================

| An unhandled exception manager for wxPython. It's easy to use : install it, import it and call WxUnhandledExceptionManager.attach().
 
| When an unhandled exception occurs, a dialog is opened and shows the type of the exception, the message and the stack trace.

Use it
------ 
.. code-block:: python

  from wxUnhandledExceptionManager import WxUnhandledExceptionManager
  import wx

  app = wx.App() #Create wxApp BEFORE attach()
  WxUnhandledExceptionManager.attach()

Message sample
--------------
.. code-block:: text

  An unhandled exception occurred !

  Type : <class 'ValueError'>

  Message : invalid literal for int() with base 10: 'p'

  Stack trace :
    File "D:/Projects/PTS4/Main.py", line 76, in <module>
      fun()
    File "D:/Projects/PTS4/Main.py", line 68, in fun
      int("p")
    
`Image link <https://i.imgur.com/53GwCEE.png>`_

Credits and licence
-------------------

| MIT Licence
| @ FORGEARD Clément 2018


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcforgeard%2FwxUnhandledExceptionManager.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcforgeard%2FwxUnhandledExceptionManager?ref=badge_large)