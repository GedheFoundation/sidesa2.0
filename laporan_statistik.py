#Boa:Frame:laporan_statistik_desa

import wx

def create(parent):
    return laporan_statistik_desa(parent)

[wxID_LAPORAN_STATISTIK_DESA, wxID_LAPORAN_STATISTIK_DESABUTTON1, 
 wxID_LAPORAN_STATISTIK_DESABUTTON2, wxID_LAPORAN_STATISTIK_DESABUTTON3, 
 wxID_LAPORAN_STATISTIK_DESABUTTON4, wxID_LAPORAN_STATISTIK_DESABUTTON5, 
 wxID_LAPORAN_STATISTIK_DESASTATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class laporan_statistik_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_STATISTIK_DESA,
              name=u'laporan_statistik_desa', parent=prnt, pos=wx.Point(549,
              286), size=wx.Size(321, 255), style=wx.FRAME_NO_TASKBAR,
              title=u'Laporan Statistik Desa')
        self.SetClientSize(wx.Size(321, 255))
        self.Center(wx.BOTH)

        self.staticBox1 = wx.StaticBox(id=wxID_LAPORAN_STATISTIK_DESASTATICBOX1,
              label=u'Laporan Statistik', name='staticBox1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(304, 200), style=0)

        self.button1 = wx.Button(id=wxID_LAPORAN_STATISTIK_DESABUTTON1,
              label=u'Cetak Laporan Statistik Penduduk', name='button1',
              parent=self, pos=wx.Point(32, 40), size=wx.Size(256, 30),
              style=0)

        self.button2 = wx.Button(id=wxID_LAPORAN_STATISTIK_DESABUTTON2,
              label=u'Cetak Laporan Statistik Kemiskinan', name='button2',
              parent=self, pos=wx.Point(32, 80), size=wx.Size(256, 30),
              style=0)

        self.button3 = wx.Button(id=wxID_LAPORAN_STATISTIK_DESABUTTON3,
              label=u'Cetak Laporan Statistik Administrasi', name='button3',
              parent=self, pos=wx.Point(32, 120), size=wx.Size(256, 30),
              style=0)

        self.button4 = wx.Button(id=wxID_LAPORAN_STATISTIK_DESABUTTON4,
              label=u'Cetak Laporan Statistik Potensi', name='button4',
              parent=self, pos=wx.Point(32, 160), size=wx.Size(256, 30),
              style=0)

        self.button5 = wx.Button(id=wxID_LAPORAN_STATISTIK_DESABUTTON5,
              label=u'Kembali Ke Menu Utama', name='button5', parent=self,
              pos=wx.Point(32, 216), size=wx.Size(256, 30), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_LAPORAN_STATISTIK_DESABUTTON5)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton5Button(self, event):
        self.Close()
