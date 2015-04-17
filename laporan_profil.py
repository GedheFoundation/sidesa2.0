#Boa:Frame:laporan_profil_desa

import wx
import sqlite3

def connect():
    db = sqlite3.connect('sidesa')
    return db     
    db.close()


  

def create(parent):
    return laporan_profil_desa(parent)

[wxID_LAPORAN_PROFIL_DESA, wxID_LAPORAN_PROFIL_DESAINPUT_ALAMAT, 
 wxID_LAPORAN_PROFIL_DESAINPUT_DESA, wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_1, 
 wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_2, wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_3, 
 wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_4, wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_5, 
 wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_6, 
 wxID_LAPORAN_PROFIL_DESAINPUT_KABUPATEN, wxID_LAPORAN_PROFIL_DESAINPUT_KADES, 
 wxID_LAPORAN_PROFIL_DESAINPUT_KECAMATAN, wxID_LAPORAN_PROFIL_DESAINPUT_KODE, 
 wxID_LAPORAN_PROFIL_DESAINPUT_PROPINSI, wxID_LAPORAN_PROFIL_DESAINPUT_SEKDES, 
 wxID_LAPORAN_PROFIL_DESAINPUT_WEB, wxID_LAPORAN_PROFIL_DESALABEL_ALAMAT, 
 wxID_LAPORAN_PROFIL_DESALABEL_DUKUH, wxID_LAPORAN_PROFIL_DESALABEL_KADES, 
 wxID_LAPORAN_PROFIL_DESALABEL_KECAMATAN, 
 wxID_LAPORAN_PROFIL_DESALABEL_KODE_DESA, 
 wxID_LAPORAN_PROFIL_DESALABEL_NAMA_DESA, 
 wxID_LAPORAN_PROFIL_DESALABEL_PROPINSI, wxID_LAPORAN_PROFIL_DESALABEL_SEKDES, 
 wxID_LAPORAN_PROFIL_DESALABEL_WEB, wxID_LAPORAN_PROFIL_DESALABLE_KABUPATEN, 
 wxID_LAPORAN_PROFIL_DESALOGO, wxID_LAPORAN_PROFIL_DESASTATICTEXT1, 
 wxID_LAPORAN_PROFIL_DESASTATICTEXT3, wxID_LAPORAN_PROFIL_DESASTATICTEXT4, 
 wxID_LAPORAN_PROFIL_DESASTATICTEXT5, wxID_LAPORAN_PROFIL_DESASTATICTEXT6, 
 wxID_LAPORAN_PROFIL_DESASTATICTEXT7, 
 wxID_LAPORAN_PROFIL_DESATOMBOL_CETAK_LAPORAN, 
 wxID_LAPORAN_PROFIL_DESATOMBOL_KEMBALI, 
] = [wx.NewId() for _init_ctrls in range(35)]

class laporan_profil_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_PROFIL_DESA,
              name=u'laporan_profil_desa', parent=prnt, pos=wx.Point(324, 272),
              size=wx.Size(911, 325), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Laporan Profil Desa')
        self.SetClientSize(wx.Size(911, 325))
        self.Center(wx.BOTH)

        self.logo = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_LAPORAN_PROFIL_DESALOGO, name=u'logo', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(152, 144), style=0)

        self.label_nama_desa = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(73, 17), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 80), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(192, 112), size=wx.Size(51, 17), style=0)

        self.input_desa = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DESA,
              name=u'input_desa', parent=self, pos=wx.Point(280, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kabupaten = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_KABUPATEN,
              name=u'input_kabupaten', parent=self, pos=wx.Point(280, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_propinsi = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_PROPINSI,
              name=u'input_propinsi', parent=self, pos=wx.Point(280, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.input_web = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_WEB,
              name=u'input_web', parent=self, pos=wx.Point(656, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kode = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_KODE,
              name=u'input_kode', parent=self, pos=wx.Point(656, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kades = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_KADES,
              name=u'input_kades', parent=self, pos=wx.Point(656, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_sekdes = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_SEKDES,
              name=u'input_sekdes', parent=self, pos=wx.Point(656, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.label_web = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(544, 16), size=wx.Size(104, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(544, 48), size=wx.Size(91, 17), style=0)

        self.label_kades = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_KADES,
              label=u'Nama KADES', name=u'label_kades', parent=self,
              pos=wx.Point(544, 80), size=wx.Size(88, 17), style=0)

        self.label_sekdes = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_SEKDES,
              label=u'Nama SEKDES', name=u'label_sekdes', parent=self,
              pos=wx.Point(544, 112), size=wx.Size(96, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 144), size=wx.Size(47, 17), style=0)

        self.label_dukuh = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESALABEL_DUKUH,
              label=u'Daftar Nama Dusun / Dukuh', name=u'label_dukuh',
              parent=self, pos=wx.Point(24, 184), size=wx.Size(576, 17),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(16,
              208), size=wx.Size(13, 17), style=0)

        self.input_dukuh_1 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_1,
              name=u'input_dukuh_1', parent=self, pos=wx.Point(40, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dukuh_2 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_2,
              name=u'input_dukuh_2', parent=self, pos=wx.Point(40, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dukuh_3 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_3,
              name=u'input_dukuh_3', parent=self, pos=wx.Point(336, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dukuh_4 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_4,
              name=u'input_dukuh_4', parent=self, pos=wx.Point(336, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dukuh_5 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_5,
              name=u'input_dukuh_5', parent=self, pos=wx.Point(640, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dukuh_6 = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_DUKUH_6,
              name=u'input_dukuh_6', parent=self, pos=wx.Point(640, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_alamat = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(280, 144),
              size=wx.Size(616, 24), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT3,
              label=u'2.', name='staticText3', parent=self, pos=wx.Point(16,
              240), size=wx.Size(13, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT4,
              label=u'3.', name='staticText4', parent=self, pos=wx.Point(312,
              208), size=wx.Size(13, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT5,
              label=u'4.', name='staticText5', parent=self, pos=wx.Point(312,
              240), size=wx.Size(13, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT6,
              label=u'5.', name='staticText6', parent=self, pos=wx.Point(616,
              208), size=wx.Size(13, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_PROFIL_DESASTATICTEXT7,
              label=u'6.', name='staticText7', parent=self, pos=wx.Point(616,
              240), size=wx.Size(13, 17), style=0)

        self.input_kecamatan = wx.TextCtrl(id=wxID_LAPORAN_PROFIL_DESAINPUT_KECAMATAN,
              name=u'input_kecamatan', parent=self, pos=wx.Point(280, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.tombol_kembali = wx.Button(id=wxID_LAPORAN_PROFIL_DESATOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(480, 280), size=wx.Size(184, 30), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_LAPORAN_PROFIL_DESATOMBOL_KEMBALI)

        self.tombol_cetak_laporan = wx.Button(id=wxID_LAPORAN_PROFIL_DESATOMBOL_CETAK_LAPORAN,
              label=u'Cetak Laporan', name=u'tombol_cetak_laporan', parent=self,
              pos=wx.Point(248, 280), size=wx.Size(216, 30), style=0)
        self.tombol_cetak_laporan.Bind(wx.EVT_BUTTON,
              self.OnTombol_cetak_laporanButton,
              id=wxID_LAPORAN_PROFIL_DESATOMBOL_CETAK_LAPORAN)

    def __init__(self, parent):
        self._init_ctrls(parent)
            
        

    def OnTombol_kembaliButton(self, event):
        self.Close()

    def OnTombol_cetak_laporanButton(self, event):
        event.Skip()

   
