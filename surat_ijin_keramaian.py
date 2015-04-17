#Boa:Frame:surat_ijin_keramaian

import wx
import wx.lib.buttons

def create(parent):
    return surat_ijin_keramaian(parent)

[wxID_SURAT_IJIN_KERAMAIAN, wxID_SURAT_IJIN_KERAMAIANKOTAK_PENGISIAN, 
 wxID_SURAT_IJIN_KERAMAIANLABEL_CARI_NIK, 
 wxID_SURAT_IJIN_KERAMAIANLABEL_MASUKAN_NIK, 
 wxID_SURAT_IJIN_KERAMAIANLABEL_NOMOR, 
 wxID_SURAT_IJIN_KERAMAIANLABEL_SURAT_IJIN_KERAMAIAN, 
 wxID_SURAT_IJIN_KERAMAIANSTATICTEXT1, wxID_SURAT_IJIN_KERAMAIANSTATICTEXT2, 
 wxID_SURAT_IJIN_KERAMAIANSTATICTEXT3, wxID_SURAT_IJIN_KERAMAIANSTATICTEXT4, 
 wxID_SURAT_IJIN_KERAMAIANSTATICTEXT5, wxID_SURAT_IJIN_KERAMAIANTEXTCTRL1, 
 wxID_SURAT_IJIN_KERAMAIANTEXTCTRL2, wxID_SURAT_IJIN_KERAMAIANTEXTCTRL3, 
 wxID_SURAT_IJIN_KERAMAIANTEXTCTRL4, wxID_SURAT_IJIN_KERAMAIANTEXTCTRL5, 
 wxID_SURAT_IJIN_KERAMAIANTEXTCTRL6, wxID_SURAT_IJIN_KERAMAIANTEXTCTRL7, 
 wxID_SURAT_IJIN_KERAMAIANTOMBOL_CARI, 
] = [wx.NewId() for _init_ctrls in range(19)]

class surat_ijin_keramaian(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SURAT_IJIN_KERAMAIAN,
              name=u'surat_ijin_keramaian', parent=prnt, pos=wx.Point(295, 51),
              size=wx.Size(911, 654), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Surat Ijin Keramaian')
        self.SetClientSize(wx.Size(911, 654))

        self.label_cari_nik = wx.StaticBox(id=wxID_SURAT_IJIN_KERAMAIANLABEL_CARI_NIK,
              label=u'Cari NIK', name=u'label_cari_nik', parent=self,
              pos=wx.Point(408, 8), size=wx.Size(488, 100), style=0)

        self.label_masukan_nik = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANLABEL_MASUKAN_NIK,
              label=u'Masukan NIK', name=u'label_masukan_nik', parent=self,
              pos=wx.Point(432, 48), size=wx.Size(82, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(528, 40),
              size=wx.Size(240, 25), style=0, value='textCtrl1')

        self.tombol_cari = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_IJIN_KERAMAIANTOMBOL_CARI, label=u'Cari',
              name=u'tombol_cari', parent=self, pos=wx.Point(776, 40),
              size=wx.Size(104, 31), style=0)

        self.kotak_pengisian = wx.StaticBox(id=wxID_SURAT_IJIN_KERAMAIANKOTAK_PENGISIAN,
              label=u'Pengisian Surat Ijin Keramaian', name=u'kotak_pengisian',
              parent=self, pos=wx.Point(16, 112), size=wx.Size(880, 488),
              style=0)

        self.label_surat_ijin_keramaian = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANLABEL_SURAT_IJIN_KERAMAIAN,
              label=u'SURAT PENGANTAR IJIN KERAMAIAN',
              name=u'label_surat_ijin_keramaian', parent=self, pos=wx.Point(320,
              128), size=wx.Size(220, 17), style=0)

        self.label_nomor = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANLABEL_NOMOR,
              label=u'Nomor', name=u'label_nomor', parent=self,
              pos=wx.Point(296, 152), size=wx.Size(44, 17), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(352, 144),
              size=wx.Size(200, 25), style=0, value='textCtrl2')

        self.staticText1 = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANSTATICTEXT1,
              label=u'Yang bertanda tangan dibawah ini', name='staticText1',
              parent=self, pos=wx.Point(40, 184), size=wx.Size(203, 17),
              style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(248, 176),
              size=wx.Size(184, 25), style=0, value='textCtrl3')

        self.staticText2 = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANSTATICTEXT2,
              label=u'desa', name='staticText2', parent=self, pos=wx.Point(440,
              184), size=wx.Size(29, 17), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(472, 176),
              size=wx.Size(104, 25), style=0, value='textCtrl4')

        self.staticText3 = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANSTATICTEXT3,
              label=u'Kecamatan', name='staticText3', parent=self,
              pos=wx.Point(584, 184), size=wx.Size(68, 17), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(656, 176),
              size=wx.Size(224, 25), style=0, value='textCtrl5')

        self.staticText4 = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANSTATICTEXT4,
              label=u'Kabupaten', name='staticText4', parent=self,
              pos=wx.Point(40, 216), size=wx.Size(67, 17), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(112, 208),
              size=wx.Size(192, 25), style=0, value='textCtrl6')

        self.staticText5 = wx.StaticText(id=wxID_SURAT_IJIN_KERAMAIANSTATICTEXT5,
              label=u'Provinsi', name='staticText5', parent=self,
              pos=wx.Point(312, 216), size=wx.Size(48, 17), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_SURAT_IJIN_KERAMAIANTEXTCTRL7,
              name='textCtrl7', parent=self, pos=wx.Point(368, 208),
              size=wx.Size(192, 25), style=0, value='textCtrl7')

    def __init__(self, parent):
        self._init_ctrls(parent)
