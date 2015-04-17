#Boa:Frame:laporan_potensi

import wx

def create(parent):
    return laporan_potensi(parent)

[wxID_LAPORAN_POTENSI, wxID_LAPORAN_POTENSIBUTTON1, 
 wxID_LAPORAN_POTENSIBUTTON2, wxID_LAPORAN_POTENSIEKONOMI, 
 wxID_LAPORAN_POTENSILAHAN, wxID_LAPORAN_POTENSIPARIWISATA, 
 wxID_LAPORAN_POTENSISTATICTEXT1, wxID_LAPORAN_POTENSISTATICTEXT2, 
 wxID_LAPORAN_POTENSISTATICTEXT3, wxID_LAPORAN_POTENSISTATICTEXT4, 
 wxID_LAPORAN_POTENSITAMBAK, 
] = [wx.NewId() for _init_ctrls in range(11)]

class laporan_potensi(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_POTENSI,
              name=u'laporan_potensi', parent=prnt, pos=wx.Point(393, 31),
              size=wx.Size(911, 684), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Potensi Desa')
        self.SetClientSize(wx.Size(911, 684))
        self.Center(wx.BOTH)

        self.ekonomi = wx.ListCtrl(id=wxID_LAPORAN_POTENSIEKONOMI,
              name=u'ekonomi', parent=self, pos=wx.Point(8, 32),
              size=wx.Size(896, 120), style=wx.LC_REPORT)

        self.lahan = wx.ListCtrl(id=wxID_LAPORAN_POTENSILAHAN, name=u'lahan',
              parent=self, pos=wx.Point(8, 184), size=wx.Size(896, 120),
              style=wx.LC_REPORT)

        self.tambak = wx.ListCtrl(id=wxID_LAPORAN_POTENSITAMBAK, name=u'tambak',
              parent=self, pos=wx.Point(8, 336), size=wx.Size(896, 120),
              style=wx.LC_REPORT)

        self.pariwisata = wx.ListCtrl(id=wxID_LAPORAN_POTENSIPARIWISATA,
              name=u'pariwisata', parent=self, pos=wx.Point(8, 488),
              size=wx.Size(896, 120), style=wx.LC_REPORT)

        self.button1 = wx.Button(id=wxID_LAPORAN_POTENSIBUTTON1,
              label=u'Cetak Laporan Keseluruhan', name='button1', parent=self,
              pos=wx.Point(248, 632), size=wx.Size(192, 30), style=0)

        self.button2 = wx.Button(id=wxID_LAPORAN_POTENSIBUTTON2,
              label=u'Kembali Ke Menu', name='button2', parent=self,
              pos=wx.Point(448, 632), size=wx.Size(248, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_LAPORAN_POTENSIBUTTON2)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_POTENSISTATICTEXT1,
              label=u'Potensi Ekonomi Dan Budaya', name='staticText1',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(189, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_POTENSISTATICTEXT2,
              label=u'Potensi Lahan / Sumber Air', name='staticText2',
              parent=self, pos=wx.Point(8, 160), size=wx.Size(175, 15),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_POTENSISTATICTEXT3,
              label=u'Potensi Tambak', name='staticText3', parent=self,
              pos=wx.Point(8, 312), size=wx.Size(101, 15), style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_POTENSISTATICTEXT4,
              label=u'Potensi Pariwisata', name='staticText4', parent=self,
              pos=wx.Point(8, 464), size=wx.Size(115, 15), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        self.Close()
