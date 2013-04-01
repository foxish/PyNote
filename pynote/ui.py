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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyNote", pos = wx.DefaultPosition, size = wx.Size( 803,566 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Sync now", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menubar.Append( self.m_menu1, u"File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Git Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Add Remote...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem5 )
		
		self.m_menubar.Append( self.m_menu2, u"Preferences" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem6 )
		
		self.m_menuItem61 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Website...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem61 )
		
		self.m_menubar.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Search:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_search = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,-1 ), wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.m_search, 0, wx.ALL, 5 )
		
		
		fgSizer6.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Title:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_noteName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 535,-1 ), 0 )
		fgSizer3.Add( self.m_noteName, 0, wx.ALL, 5 )
		
		
		fgSizer6.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		m_noteListChoices = []
		self.m_noteList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_noteListChoices, 0 )
		self.m_noteList.SetMinSize( wx.Size( 200,400 ) )
		
		fgSizer6.Add( self.m_noteList, 0, wx.ALL, 5 )
		
		self.m_noteContent = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.m_noteContent.SetMinSize( wx.Size( 575,400 ) )
		
		fgSizer6.Add( self.m_noteContent, 0, wx.ALL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_newNote = wx.Button( self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_newNote, 0, wx.ALL, 5 )
		
		self.m_deleteNote = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_deleteNote, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer6.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_saveNote = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_saveNote, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_minimize = wx.Button( self, wx.ID_ANY, u"Minimize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_minimize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer6.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.about_click, id = self.m_menuItem6.GetId() )
		self.m_search.Bind( wx.EVT_TEXT_ENTER, self.search_event )
		self.m_noteList.Bind( wx.EVT_LISTBOX, self.list_itemclick )
		self.m_newNote.Bind( wx.EVT_BUTTON, self.new_click )
		self.m_deleteNote.Bind( wx.EVT_BUTTON, self.delete_click )
		self.m_saveNote.Bind( wx.EVT_BUTTON, self.save_click )
		self.m_minimize.Bind( wx.EVT_BUTTON, self.minimize_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def about_click( self, event ):
		event.Skip()
	
	def search_event( self, event ):
		event.Skip()
	
	def list_itemclick( self, event ):
		event.Skip()
	
	def new_click( self, event ):
		event.Skip()
	
	def delete_click( self, event ):
		event.Skip()
	
	def save_click( self, event ):
		event.Skip()
	
	def minimize_click( self, event ):
		event.Skip()
	

