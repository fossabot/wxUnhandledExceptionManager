Unhandled exception manager for wxPython
========================================

| A unhandled exception manager for wxPython. It's easy to use : install it, import it and call WxUnhandledExceptionManager.attach().
 
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
