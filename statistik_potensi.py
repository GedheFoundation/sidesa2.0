#Boa:Frame:statistik_potensi_data

import wx

def create(parent):
    return statistik_potensi_data(parent)

[wxID_STATISTIK_POTENSI_DATA, wxID_STATISTIK_POTENSI_DATABUTTON1, 
 wxID_STATISTIK_POTENSI_DATABUTTON2, wxID_STATISTIK_POTENSI_DATABUTTON3, 
 wxID_STATISTIK_POTENSI_DATABUTTON4, wxID_STATISTIK_POTENSI_DATABUTTON5, 
 wxID_STATISTIK_POTENSI_DATASTATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class statistik_potensi_data(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_STATISTIK_POTENSI_DATA,
              name=u'statistik_potensi_data', parent=prnt, pos=wx.Point(543,
              307), size=wx.Size(307, 256), style=wx.FRAME_NO_TASKBAR,
              title=u'Data Statistik Potensi Desa')
        self.SetClientSize(wx.Size(307, 256))
        self.Center(wx.BOTH)

        self.staticBox1 = wx.StaticBox(id=wxID_STATISTIK_POTENSI_DATASTATICBOX1,
              label=u'Statistik Potensi', name='staticBox1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(288, 192), style=0)

        self.button1 = wx.Button(id=wxID_STATISTIK_POTENSI_DATABUTTON1,
              label=u'Statistik Potensi Ekonomi', name='button1', parent=self,
              pos=wx.Point(24, 32), size=wx.Size(256, 30), style=0)

        self.button2 = wx.Button(id=wxID_STATISTIK_POTENSI_DATABUTTON2,
              label=u'Statistik Potensi Lahan', name='button2', parent=self,
              pos=wx.Point(24, 72), size=wx.Size(256, 30), style=0)

        self.button3 = wx.Button(id=wxID_STATISTIK_POTENSI_DATABUTTON3,
              label=u'Statistik Potensi Tambak', name='button3', parent=self,
              pos=wx.Point(24, 112), size=wx.Size(256, 30), style=0)

        self.button4 = wx.Button(id=wxID_STATISTIK_POTENSI_DATABUTTON4,
              label=u'Statistik Potensi Pariwisata', name='button4',
              parent=self, pos=wx.Point(24, 152), size=wx.Size(256, 30),
              style=0)

        self.button5 = wx.Button(id=wxID_STATISTIK_POTENSI_DATABUTTON5,
              label=u'Kembali Ke Menu Utama', name='button5', parent=self,
              pos=wx.Point(24, 208), size=wx.Size(256, 30), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_STATISTIK_POTENSI_DATABUTTON5)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton5Button(self, event):
        self.Close()
