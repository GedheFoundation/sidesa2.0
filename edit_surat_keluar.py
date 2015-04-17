#Boa:Frame:edit_surat_keluar

import wx
import input_edit_surat

def create(parent):
    return edit_surat_keluar(parent)

[wxID_EDIT_SURAT_KELUAR, wxID_EDIT_SURAT_KELUARBUTTON1, 
 wxID_EDIT_SURAT_KELUARBUTTON2, wxID_EDIT_SURAT_KELUARSTATICTEXT1, 
 wxID_EDIT_SURAT_KELUARSTATICTEXT2, wxID_EDIT_SURAT_KELUARSTATICTEXT3, 
 wxID_EDIT_SURAT_KELUARSTATICTEXT4, wxID_EDIT_SURAT_KELUARSURAT_KELUAR, 
 wxID_EDIT_SURAT_KELUARTEXTCTRL1, wxID_EDIT_SURAT_KELUARTEXTCTRL2, 
 wxID_EDIT_SURAT_KELUARTEXTCTRL3, wxID_EDIT_SURAT_KELUARTOMBOL_KE_MENU, 
] = [wx.NewId() for _init_ctrls in range(12)]

class edit_surat_keluar(wx.Frame):
    def _init_coll_surat_keluar_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor Surat', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Perihal', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Tanggal', width=160)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Kepada',
              width=290)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_SURAT_KELUAR,
              name=u'edit_surat_keluar', parent=prnt, pos=wx.Point(451, 206),
              size=wx.Size(798, 402), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Edit Surat Keluar')
        self.SetClientSize(wx.Size(798, 402))
        self.Center(wx.BOTH)

        self.surat_keluar = wx.ListCtrl(id=wxID_EDIT_SURAT_KELUARSURAT_KELUAR,
              name=u'surat_keluar', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(784, 232), style=wx.LC_REPORT)
        self._init_coll_surat_keluar_Columns(self.surat_keluar)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_SURAT_KELUARSTATICTEXT1,
              label=u'Nomor Surat', name='staticText1', parent=self,
              pos=wx.Point(344, 256), size=wx.Size(83, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_EDIT_SURAT_KELUARTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(440, 248),
              size=wx.Size(248, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_EDIT_SURAT_KELUARBUTTON1,
              label=u'Cari', name='button1', parent=self, pos=wx.Point(696,
              248), size=wx.Size(85, 30), style=0)

        self.staticText2 = wx.StaticText(id=wxID_EDIT_SURAT_KELUARSTATICTEXT2,
              label=u'Nomor Surat', name='staticText2', parent=self,
              pos=wx.Point(16, 288), size=wx.Size(83, 15), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EDIT_SURAT_KELUARSTATICTEXT3,
              label=u'Perihal', name='staticText3', parent=self,
              pos=wx.Point(16, 328), size=wx.Size(46, 15), style=0)

        self.staticText4 = wx.StaticText(id=wxID_EDIT_SURAT_KELUARSTATICTEXT4,
              label=u'Tanggal', name='staticText4', parent=self,
              pos=wx.Point(440, 280), size=wx.Size(51, 15), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_EDIT_SURAT_KELUARTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(120, 288),
              size=wx.Size(264, 25), style=0, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_EDIT_SURAT_KELUARTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(120, 320),
              size=wx.Size(264, 25), style=0, value='')

        self.button2 = wx.Button(id=wxID_EDIT_SURAT_KELUARBUTTON2,
              label=u'Simpan Perubahan', name='button2', parent=self,
              pos=wx.Point(192, 360), size=wx.Size(184, 30), style=0)

        self.tombol_ke_menu = wx.Button(id=wxID_EDIT_SURAT_KELUARTOMBOL_KE_MENU,
              label=u'Batal Simpan / Ke Menu', name=u'tombol_ke_menu',
              parent=self, pos=wx.Point(392, 360), size=wx.Size(248, 30),
              style=0)
        self.tombol_ke_menu.Bind(wx.EVT_BUTTON, self.OnTombol_ke_menuButton,
              id=wxID_EDIT_SURAT_KELUARTOMBOL_KE_MENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_ke_menuButton(self, event):
        self.main=input_edit_surat.create(None)
        self.main.Show()
        self.Close()
