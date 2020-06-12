# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- codnig: utf-8 -*-

import wx
import os
import sys

import GUI.window as window
#from  Config.Init import *
#import Utility.user as user

class mainApp(wx.App):

    def OnInit(self):
        #check directory and path in config file and program

        #check Databases of program

        #check Date,Time,propertis of file

        #Inter username and password of users
               

        #Check lock if nassesry

        #check hardware and connection
        SIZE = wx.DisplaySize()
        #print SIZE

        #do main windows of program 

        frame = window.MainWin()
        frame.SetSize(SIZE)
        frame.SetPosition((1,1))
        #frame.CenterOnScreen()
        
        frame.Show()


        '''
        userid = user.Checkpass()
        if  userid == 'No':
            #frame.Destroy()
            q= wx.GetActiveWindow()
            print q
            if str(q) == 'None':
                self.Exit()
            else:
                q.Destroy()
                self.Exit()
       ''' 

        
        return True
  



if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
