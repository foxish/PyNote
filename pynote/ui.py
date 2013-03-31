# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 803,553 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menubar.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem5 )
		
		self.m_menubar.Append( self.m_menu2, u"Preferences" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem6 )
		
		self.m_menu3.AppendSeparator()
		
		self.m_menubar.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_search = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_search.SetMinSize( wx.Size( 200,-1 ) )
		
		fgSizer6.Add( self.m_search, 0, wx.ALL, 5 )
		
		self.m_noteName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_noteName.SetMinSize( wx.Size( 575,-1 ) )
		
		fgSizer6.Add( self.m_noteName, 0, wx.ALL, 5 )
		
		m_noteListChoices = []
		self.m_noteList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_noteListChoices, 0 )
		self.m_noteList.SetMinSize( wx.Size( 200,400 ) )
		
		fgSizer6.Add( self.m_noteList, 0, wx.ALL, 5 )
		
		self.m_noteContent = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.m_noteContent.SetMinSize( wx.Size( 575,400 ) )
		
		fgSizer6.Add( self.m_noteContent, 0, wx.ALL, 5 )
		
		self.m_newNote = wx.Button( self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_newNote, 0, wx.ALL, 5 )
		
		self.m_saveNote = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_saveNote, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.about_click, id = self.m_menuItem6.GetId() )
		self.m_search.Bind( wx.EVT_KEY_DOWN, self.search_perform )
		self.m_newNote.Bind( wx.EVT_BUTTON, self.new_note_event )
		self.m_saveNote.Bind( wx.EVT_BUTTON, self.save_note_event )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def about_click( self, event ):
		event.Skip()
	
	def search_perform( self, event ):
		event.Skip()
	
	def new_note_event( self, event ):
		event.Skip()
	
	def save_note_event( self, event ):
		event.Skip()

