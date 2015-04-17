#Boa:Frame:pelaporan_administrasi

import wx

def create(parent):
    return pelaporan_administrasi(parent)

[wxID_PELAPORAN_ADMINISTRASI, wxID_PELAPORAN_ADMINISTRASIBUTTON1, 
 wxID_PELAPORAN_ADMINISTRASIBUTTON2, wxID_PELAPORAN_ADMINISTRASIBUTTON3, 
 wxID_PELAPORAN_ADMINISTRASIBUTTON4, wxID_PELAPORAN_ADMINISTRASILISTCTRL1, 
 wxID_PELAPORAN_ADMINISTRASISTATICTEXT1, 
 wxID_PELAPORAN_ADMINISTRASISTATICTEXT2, wxID_PELAPORAN_ADMINISTRASITEXTCTRL1, 
 wxID_PELAPORAN_ADMINISTRASITEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(10)]

class pelaporan_administrasi(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PELAPORAN_ADMINISTRASI,
              name=u'pelaporan_administrasi', parent=prnt, pos=wx.Point(300,
              208), size=wx.Size(911, 296), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Pelaporan Administrasi')
        self.SetClientSize(wx.Size(911, 296))
        self.Center(wx.BOTH)

        self.listCtrl1 = wx.ListCtrl(id=wxID_PELAPORAN_ADMINISTRASILISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(896, 152), style=wx.LC_ICON)

        self.staticText1 = wx.StaticText(id=wxID_PELAPORAN_ADMINISTRASISTATICTEXT1,
              label=u'Jumlah Surat Masuk', name='staticText1', parent=self,
              pos=wx.Point(16, 200), size=wx.Size(128, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PELAPORAN_ADMINISTRASISTATICTEXT2,
              label=u'Jumlah Surat Keluar', name='staticText2', parent=self,
              pos=wx.Point(488, 200), size=wx.Size(126, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_PELAPORAN_ADMINISTRASITEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(168, 200),
              size=wx.Size(144, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_PELAPORAN_ADMINISTRASIBUTTON1,
              label=u'Lihat', name='button1', parent=self, pos=wx.Point(320,
              200), size=wx.Size(104, 24), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_PELAPORAN_ADMINISTRASITEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(664, 200),
              size=wx.Size(128, 25), style=0, value='')

        self.button2 = wx.Button(id=wxID_PELAPORAN_ADMINISTRASIBUTTON2,
              label=u'Lihat', name='button2', parent=self, pos=wx.Point(800,
              200), size=wx.Size(85, 24), style=0)

        self.button3 = wx.Button(id=wxID_PELAPORAN_ADMINISTRASIBUTTON3,
              label=u'Cetak Laporan Administrasi', name='button3', parent=self,
              pos=wx.Point(256, 256), size=wx.Size(192, 30), style=0)

        self.button4 = wx.Button(id=wxID_PELAPORAN_ADMINISTRASIBUTTON4,
              label=u'Kembali Ke Menu', name='button4', parent=self,
              pos=wx.Point(456, 256), size=wx.Size(216, 30), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_PELAPORAN_ADMINISTRASIBUTTON4)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton4Button(self, event):
        self.Close()
