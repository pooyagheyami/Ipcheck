# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
#import wx.xrc
import wx.grid
import  wx.lib.masked as  masked

#from testlan import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 527,300 ), style = wx.TAB_TRAVERSAL )

		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		#self.SetLayoutDirection(wx.Right)
		self.addr1 = '192.168.1.1'
		self.addr2 = '192.168.1.20'

		
		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"بررسی شبکه", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )
		bSizer2.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		Choices = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
		self.chs1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, Choices, 0 )
		self.chs1.SetSelection( 0 )
		bSizer2.Add( self.chs1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"از شماره ip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )
		bSizer2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ip1 = wx.TextCtrl( self, wx.ID_ANY, self.addr1, wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.ip1 = masked.IpAddrCtrl( self, -1,'192.168.  1.  1', style = wx.TE_PROCESS_TAB ) 
		bSizer2.Add( self.ip1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"الی", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )
		bSizer2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ip2 = wx.TextCtrl( self, wx.ID_ANY, self.addr2, wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.ip2 = masked.IpAddrCtrl( self, -1,'192.168.  1.256', style = wx.TE_PROCESS_TAB )
		bSizer2.Add( self.ip2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lanlist = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		self.Listno = 7
		
		# Grid
		self.lanlist.CreateGrid( self.Listno,5 )
		self.lanlist.EnableEditing( False )
		self.lanlist.EnableGridLines( True )
		self.lanlist.EnableDragGridSize( False )
		self.lanlist.SetMargins( 0, 0 )
		
		# Columns
		self.lanlist.SetColSize( 0, 70 )
		self.lanlist.SetColSize( 1, 121 )
		self.lanlist.SetColSize( 2, 157 )
		self.lanlist.SetColSize( 3, 59 )
		self.lanlist.SetColSize( 4, 79 )
		self.lanlist.EnableDragColMove( False )
		self.lanlist.EnableDragColSize( True )
		self.lanlist.SetColLabelSize( 30 )
		self.lanlist.SetColLabelValue( 0, u"نام کاربر" )
		self.lanlist.SetColLabelValue( 1, u"آدرس شبکه ip" )
		self.lanlist.SetColLabelValue( 2, u"آدرس مک mac" )
		self.lanlist.SetColLabelValue( 3, u"وضعیت" )
		self.lanlist.SetColLabelValue( 4, u"زمان اتصال" )
		self.lanlist.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.lanlist.EnableDragRowSize( True )
		self.lanlist.SetRowLabelSize( 19 )
		self.lanlist.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.lanlist.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer3.Add( self.lanlist, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer10.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"بررسي", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"تنظیمات", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chk1 = wx.CheckBox( self, wx.ID_ANY, u"نمایش همه", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.chk1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn4 = wx.Button( self, wx.ID_ANY, u"تائید", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.chs1.Bind( wx.EVT_CHOICE, self.Onlan )
		self.btn1.Bind( wx.EVT_BUTTON, self.search )
		self.btn2.Bind( wx.EVT_BUTTON, self.Option )
		self.chk1.Bind( wx.EVT_CHECKBOX, self.showall )
		self.btn3.Bind( wx.EVT_BUTTON, self.Cancel )
		self.btn4.Bind( wx.EVT_BUTTON, self.Onokey )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Onlan( self, event ):
		print event
	
	def search( self, event ):
                
                self.addr1=self.ip1.GetValue()
                self.addr2=self.ip2.GetValue()
                t = testlan(self.addr1,self.addr2,80)
		#data=t.run(self.addr1,self.addr2)
		#print t.run2(self.addr1)
		#print t.network
		a = int(self.addr1.split('.')[3])
		b = int(self.addr2.split('.')[3])
		r=0
		c=0
		i=0
		for ip in range(a,b):
                        #print ip
                        addr = t.network + str(ip)
                        data = t.run2(addr)
                        #print data
                        self.m_gauge1.SetValue( ip*(100/b+1) )
                        self.Refresh()
                        for d in data:
                                #print r,i,d
                                self.lanlist.SetCellValue(r,c,d)
                                i = i + 1
                                #self.m_gauge1.SetValue( i*(ip/100) )
                                self.Refresh()
                                if i % 5 == 0 :
                                        r = r + 1
                                        c = 0
                                else:
                                        c = c + 1
	
	def Option( self, event ):
                gr = wx.Dialog(self)
		dlg = MyPanel2(gr)
		gr.SetSize((406,208))
		gr.ShowModal()
		gr.Destroy()
		
	
	def showall( self, event ):
		#print event.GetEventObject()
		#print self.chk1.GetValue()
		#print self.Listno
		if self.chk1.GetValue():
                        self.addr1=self.ip1.GetValue()
                        self.addr2=self.ip2.GetValue()
                        self.all =  int(self.addr2.split('.')[3])-int(self.addr1.split('.')[3])
                        self.Listno = self.all
                else:
                        self.Listno = 7
                print self.Listno        
	
	def Cancel( self, event ):
                #print event.GetEventObject()
		q = self.GetParent()
		#print q
		q.Close()
		return -1

	
	def Onokey( self, event ):
                #print event.GetEventObject()
		q = self.GetParent()
		q.Close()
		return -1




# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 406,208 ), style = wx.TAB_TRAVERSAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"نام کاربر", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.lbl1.Wrap( -1 )
		bSizer6.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn1 = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer6.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chk2 = wx.CheckBox( self, wx.ID_ANY, u"اتصال به برنامه...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.chk2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"آدرس شبکه", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.lbl2.Wrap( -1 )
		bSizer7.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.fld2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"آدرس مک", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		bSizer7.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.fld3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lbl4 = wx.StaticText( self, wx.ID_ANY, u"زمان مصرفی ", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.lbl4.Wrap( -1 )
		bSizer8.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fld4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.fld4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chk3 = wx.CheckBox( self, wx.ID_ANY, u"قطع اتوماتیک", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.chk3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn2 = wx.Button( self, wx.ID_ANY, u"انصراف", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn3 = wx.Button( self, wx.ID_ANY, u"تعریف شود", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.srch )
		self.chk2.Bind( wx.EVT_CHECKBOX, self.connect )
		self.chk3.Bind( wx.EVT_CHECKBOX, self.offlan )
		self.btn2.Bind( wx.EVT_BUTTON, self.cancel )
		self.btn3.Bind( wx.EVT_BUTTON, self.newuser )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def srch( self, event ):
		event.Skip()
	
	def connect( self, event ):
		event.Skip()
	
	def offlan( self, event ):
		event.Skip()
	
	def cancel( self, event ):
		q = self.GetParent()
		q.Close()
		return -1
	
	def newuser( self, event ):
		event.Skip()
	

###########################################################################
## Class Testlan
###########################################################################

#In the name of God
#!/usr/bin/env python

from socket import *
import os
from subprocess import *
import re
#from netaddr import *


class testlan(object):
    def __init__(self,addr1,addr2,port):
        self.addr1 = addr1
        self.addr2 = addr2
        self.prot = port
        self.network = addr1.split('.')[0]+'.'+addr1.split('.')[1]+'.'+addr1.split('.')[2]+'.'


    def pingit(self,addr):
        try:
            p = check_output("ping -n 1 -w 1 "+addr,shell=True)
            #print p.find('0% ')
            return True
        except:
            print 'error',addr
            return False

    def openport(self,addr):
        for i in [23,25,80,135,445,902]:
            sok = socket(AF_INET, SOCK_STREAM)
            sok.settimeout(0.1)
            if sok.connect_ex((addr,i)) == 0 :
                #print addr,i
                sok.close()
                return i
            else:
                sok.close()
                continue
        return 0

    def is_up(self,addr):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)    ## set a timeout of 0.01 sec
        self.port=self.openport(addr)
        #print self.port,'  ',addr
        if  self.port == 0:
            #print addr,self.port
            if self.pingit(addr):
                s.close()
                return 1
            else:
                s.close()
                #print self.port
                return 0
        elif not s.connect_ex((addr,self.port)) :  # connect to the remote host on port 135
            #s.bind((addr,port))
            #s.send("GET /HTTP /1.0\n\n")
            #print s.listen()
            s.close()    ## (port 135 is always open on Windows machines, AFAIK)
            return 1
        else:
            s.close()
            return 0

    def getmac(self,addr):
        arp_out =check_output(['arp','-a',addr])
        if len(arp_out)>30:
            m=re.search("([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}",arp_out)
            mac1= arp_out.splitlines()[3]
            mac = arp_out.splitlines()[3].split('    ')[2].lstrip(' ')
            #mac =  EUI(arp_out.splitlines()[3].split('     ')[1].lstrip(' '))
            #mac.dialect = mac_unix_expanded
            #print mac,mac1,m
            return mac
        else:
            arp_out =check_output(['getmac','-V'],shell=True)
            m=re.search("([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}",arp_out)
            #print arp_out.splitlines()
            return m.group()


    def run2(self,addr):
        #print addr
        #print self.is_up(addr)
        data = []    
        if self.is_up(addr):
           data.append(unicode(getfqdn(addr)))
           data.append(unicode(addr))
           data.append(unicode(self.getmac(addr)))
           data.append(unicode('Active'))
           data.append(unicode('Now'))
        return data   
                
            
            


    def run(self,addr1,addr2):
        a=int(addr1.split('.')[3])
        b=int(addr2.split('.')[3])
        self.all =  int(addr2.split('.')[3])-int(addr1.split('.')[3])
        network = self.network
        i = 0
        data = []
        for ip in xrange(a,b):
            self.addr = network + str(ip)
            #print self.addr
            if self.is_up(self.addr):
                #print '%s \t- %s' %(self.addr, getfqdn(self.addr))
                #print self.getmac(self.addr)
                data.append(unicode(getfqdn(self.addr)))
                data.append(unicode(self.addr))
                data.append(unicode(self.getmac(self.addr)))
                data.append(unicode('Active'))
                data.append(unicode('Now'))
        #print data
        return data       
