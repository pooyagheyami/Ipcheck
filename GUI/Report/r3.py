#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import report3
from  Config.Init import *

class telframe(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)
        self.parent=parent

        
               
        self.panel = report3.MyPanel1(self)
        self.panel.SetLayoutDirection(2)

        
    def closeit(self):
        self.Close(True)

def size():
    return (527,300)

def main(panel=None ):
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    
    parent =  panel.GetParent()
    
    frame = telframe(parent )
    frame.SetTitle(u'اعلان')
    frame.SetSize(size())
    frame.Show()
    

    

if __name__ == '__main__':
    #app = wx.App(False) 
    main()
    #app.MainLoop()
    
