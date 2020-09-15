import wx

class ImagePanel(wx.Panel):
    
    def __init__(self, parent):
        """
        Panel constructor - initializes all the widgets on the panel
        """
        super().__init__(parent)
        self.max_size = 240
        
        # wx.Image holds the image in memory
        img = wx.Image(240, 240)
        # wx.StaticBitmap displays the image to the user
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))
        
        browse_btn = wx.Button(self, label='Browse')
        browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)
        
        self.photo_txt = wx.TextCtrl(self, size=(200, -1))
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)
        hsizer.Add(browse_btn, 0, wx.ALL, 5)
        hsizer.Add(self.photo_txt, 0, wx.ALL, 5)
        main_sizer.Add(hsizer)
        
        # Apply the sizer to the panel
        self.SetSizer(main_sizer)
        # Fit the widgets in the sizer to the frame (i.e. parent)
        main_sizer.Fit(parent)
        self.Layout()
        
    def on_browse(self, event):
        """
        Open up a file dialog and browse for an image file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        with wx.FileDialog(None, 'Choose a file',
                           wildcard=wildcard,
                           style=wx.ID_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_txt.SetValue(dialog.GetPath())
                self.load_image()
                
    def load_image(self):
        """
        Load the selected image into the user interface
        """
        filepath = self.photo_txt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        
        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()
        

class MainFrame(wx.Frame):
    """
    Creates the main window of the application
    """
    
    def __init__(self):
        super().__init__(None, title='Image Viewer')
        panel = ImagePanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(redirect=False)  
    frame = MainFrame()  # load the frame
    app.MainLoop()  # event loop is started