from ui import MainFrame
from storage.storage import Storage
import wx


class Main(MainFrame):
    ABOUT_LICENSE = "(under the BSD License)"
    ABOUT_URL    = "https://github.com/DarkCthulhu/PyNote"
    
    # constructor
    def __init__(self):
        MainFrame.__init__(self, None)
        self.store = Storage()
        self.populate_list()
    
    # shows an info-message            
    def show_info(self, message):
        wx.MessageBox(message, 'Info', wx.OK | wx.ICON_INFORMATION)
    
    # Find the entries from the sqlite database and populate
    def populate_list(self):
        notes = self.store.list_notes()
        notes_list = [note[0] for note in notes]
        self.m_noteList.InsertItems(notes_list, 0)
    
    # called when the list needs to be refreshed
    def list_modified(self):
        # if not deselected, it remembers selection even after element is deleted
        self.m_noteList.Deselect(self.m_noteList.GetSelection())
        self.m_noteList.Clear()
        self.populate_list()
        
    # overrides for UI events
    def list_itemclick(self, event):
        selected = self.m_noteList.GetStringSelection()
        self.m_noteName.SetValue(selected)
        self.m_noteContent.SetValue(self.store.retrieve_file(selected))
    
    #handler for the about button click in the Help menu
    def about_click( self, event ):
        about_str = Main.ABOUT_URL +"\n"+ Main.ABOUT_LICENSE
        self.show_info(about_str)
	
    #on clicking save button on the UI
    def save_click( self, event ):
        #TODO: Validation
        operation_state = self.store.save_file(self.m_noteName.GetValue(), self.m_noteContent.GetValue())
        if(operation_state):
            self.list_modified()
            self.m_statusBar.SetStatusText("Saved Successfully", 0)
        else:
            self.show_info("An Error Occurred")
        
    # click handler for the delete button on the UI
    def delete_click(self, event):
        selected = self.m_noteList.GetStringSelection()
        operation_state = self.store.delete_file(selected)
        if(operation_state):
            self.list_modified()
            self.m_statusBar.SetStatusText("Deleted Successfully", 0)
        else:
            self.show_info("An Error Occurred")
    
    # click handler for the new button on the UI        
    def new_click(self, event):
        self.m_noteName.Clear()
        self.m_noteContent.Clear()
        self.m_noteContent.SetFocus()
        
        
    # filtering through titles
    def search_event( self, event ):
        # deselect current selection and clear the list
        self.m_noteList.Deselect(self.m_noteList.GetSelection())
        self.m_noteList.Clear()
        
        notes = self.store.list_notes(self.m_search.GetValue())
        notes_list = [note[0] for note in notes]
        self.m_noteList.InsertItems(notes_list, 0)
        
def main():
    app = wx.PySimpleApp(0)
    frame = Main()
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
