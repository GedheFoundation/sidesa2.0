#Boa:Frame:statistik_administrasi

import wx

def create(parent):
    return statistik_administrasi(parent)

[wxID_STATISTIK_ADMINISTRASI, wxID_STATISTIK_ADMINISTRASIBUTTON1, 
 wxID_STATISTIK_ADMINISTRASIBUTTON2, wxID_STATISTIK_ADMINISTRASIBUTTON3, 
 wxID_STATISTIK_ADMINISTRASISTATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class statistik_administrasi(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_STATISTIK_ADMINISTRASI,
              name=u'statistik_administrasi', parent=prnt, pos=wx.Point(544,
              323), size=wx.Size(327, 186), style=wx.FRAME_NO_TASKBAR,
              title=u'Data Statistik Administrasi')
        self.SetClientSize(wx.Size(327, 186))
        self.Center(wx.BOTH)

        self.staticBox1 = wx.StaticBox(id=wxID_STATISTIK_ADMINISTRASISTATICBOX1,
              label=u'Statistik Administrasi', name='staticBox1', parent=self,
              pos=wx.Point(8, 16), size=wx.Size(312, 112), style=0)

        self.button1 = wx.Button(id=wxID_STATISTIK_ADMINISTRASIBUTTON1,
              label=u'Perbandingan Surat Masuk Keluar', name='button1',
              parent=self, pos=wx.Point(24, 40), size=wx.Size(280, 30),
              style=0)

        self.button2 = wx.Button(id=wxID_STATISTIK_ADMINISTRASIBUTTON2,
              label=u'Perihal Surat Keluar', name='button2', parent=self,
              pos=wx.Point(24, 80), size=wx.Size(280, 30), style=0)

        self.button3 = wx.Button(id=wxID_STATISTIK_ADMINISTRASIBUTTON3,
              label=u'Kembali Ke Menu Utama', name='button3', parent=self,
              pos=wx.Point(24, 144), size=wx.Size(280, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_STATISTIK_ADMINISTRASIBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton3Button(self, event):
        self.Close()
