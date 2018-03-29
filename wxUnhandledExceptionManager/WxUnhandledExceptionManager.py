# coding=utf-8
import wx
import wx.lib.dialogs
import textwrap
import traceback
import sys


def attach():
    sys.excepthook = _custom_excepthook


def _custom_excepthook(exception_type, value, tb):
    dlg_content = textwrap.dedent("""\
    An unhandled exception occurred !
    
    Type : {}
    
    Message : {}
    
    Stack trace :
    {}\
    """).format(exception_type, value, ''.join(traceback.format_tb(tb)))

    dlg = wx.lib.dialogs.ScrolledMessageDialog(None, dlg_content, "Unhandled exception", size=(700, 500),
                                               style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
    dlg.ShowModal()
    dlg.Destroy()
