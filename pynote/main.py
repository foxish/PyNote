from ui import MainFrame
from storage.storage import Storage
import wx


class Main(MainFrame):
    ABOUT_LICENSE = "(under the BSD License)"
    ABOUT_URL    = "https://github.com/DarkCthulhu/PyNote"
    
    def __init__(self):
        MainFrame.__init__(self, None)
        self.store = Storage()
        self.populate_list()
                
    def show_info(self, message):
        wx.MessageBox(message, 'Info', wx.OK | wx.ICON_INFORMATION)

    def populate_list(self):
        notes = self.store.list_notes()
        notes_list = [note[0] for note in notes]
        self.m_noteList.InsertItems(notes_list, 0)
    
    # called when the list needs to be refreshed
    def list_modified(self):
        self.m_noteList.Clear()
        self.populate_list()
        
    # overrides for UI events
    def list_itemclick(self, event):
        selected = self.m_noteList.GetStringSelection()
        self.m_noteName.SetValue(selected)
        self.m_noteContent.SetValue(self.store.retrieve_file(selected))
    
    def about_click( self, event ):
        about_str = Main.ABOUT_URL +"\n"+ Main.ABOUT_LICENSE
        self.show_info(about_str)
	
    def save_note_event( self, event ):
        #TODO: Validation
        save_state = self.store.save_file(self.m_noteName.GetValue(), self.m_noteContent.GetValue())
        if(save_state):
            self.list_modified()
            self.show_info("Saved Successfully")
        else:
            self.show_info("An Error Occurred")
        
    
    
def main():
    app = wx.PySimpleApp(0)
    frame = Main()
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
