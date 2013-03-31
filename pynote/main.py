from ui import mainFrame
import wx

class Main(mainFrame):
    def __init__(self):
        mainFrame.__init__(self, None)
        
    def about_click( self, event ):
        print("AboutDialog")
	
def main():
    app = wx.PySimpleApp(0)
    frame = Main()
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
