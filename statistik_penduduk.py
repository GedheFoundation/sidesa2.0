#Boa:Frame:data_statistik_penduduk

import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return data_statistik_penduduk(parent)

[wxID_DATA_STATISTIK_PENDUDUK, 
 wxID_DATA_STATISTIK_PENDUDUKKOTAK_STATISTIK_PENDUDUK, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_GIZI, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK, 
] = [wx.NewId() for _init_ctrls in range(11)]

class data_statistik_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_DATA_STATISTIK_PENDUDUK,
              name=u'data_statistik_penduduk', parent=prnt, pos=wx.Point(520,
              209), size=wx.Size(306, 420), style=wx.FRAME_NO_TASKBAR,
              title=u'Data Statistik Penduduk')
        self.SetClientSize(wx.Size(306, 420))
        self.Center(wx.BOTH)

        self.kotak_statistik_penduduk = wx.StaticBox(id=wxID_DATA_STATISTIK_PENDUDUKKOTAK_STATISTIK_PENDUDUK,
              label=u'Statistik Penduduk', name=u'kotak_statistik_penduduk',
              parent=self, pos=wx.Point(16, 16), size=wx.Size(272, 352),
              style=0)

        self.tombol_piramida_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK,
              label=u'Piramida Penduduk', name=u'tombol_piramida_penduduk',
              parent=self, pos=wx.Point(32, 40), size=wx.Size(240, 31),
              style=0)
        self.tombol_piramida_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_piramida_pendudukButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK)

        self.tombol_perbandingan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN,
              label=u'Perbandingan Kepala Keluarga',
              name=u'tombol_perbandingan', parent=self, pos=wx.Point(32, 80),
              size=wx.Size(240, 31), style=0)
        self.tombol_perbandingan.Bind(wx.EVT_BUTTON,
              self.OnTombol_perbandinganButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN)

        self.tombol_pendidikan_akhir = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR,
              label=u'Pendidikan Terakhir', name=u'tombol_pendidikan_akhir',
              parent=self, pos=wx.Point(32, 120), size=wx.Size(240, 31),
              style=0)
        self.tombol_pendidikan_akhir.Bind(wx.EVT_BUTTON,
              self.OnTombol_pendidikan_akhirButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR)

        self.tombol_pendidikan_sedang = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG,
              label=u'Pendidikan Sedang Ditempuh',
              name=u'tombol_pendidikan_sedang', parent=self, pos=wx.Point(32,
              160), size=wx.Size(240, 31), style=0)
        self.tombol_pendidikan_sedang.Bind(wx.EVT_BUTTON,
              self.OnTombol_pendidikan_sedangButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG)

        self.tombol_kehamilan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN,
              label=u'Kehamilan', name=u'tombol_kehamilan', parent=self,
              pos=wx.Point(32, 200), size=wx.Size(240, 31), style=0)
        self.tombol_kehamilan.Bind(wx.EVT_BUTTON, self.OnTombol_kehamilanButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN)

        self.tombol_kontrasepsi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'tombol_kontrasepsi',
              parent=self, pos=wx.Point(32, 240), size=wx.Size(240, 31),
              style=0)
        self.tombol_kontrasepsi.Bind(wx.EVT_BUTTON,
              self.OnTombol_kontrasepsiButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI)

        self.tombol_gizi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_GIZI, label=u'Gizi Balita',
              name=u'tombol_gizi', parent=self, pos=wx.Point(32, 280),
              size=wx.Size(240, 31), style=0)
        self.tombol_gizi.Bind(wx.EVT_BUTTON, self.OnTombol_giziButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_GIZI)

        self.tombol_kepemilikan_dokumen = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'tombol_kepemilikan_dokumen',
              parent=self, pos=wx.Point(32, 320), size=wx.Size(240, 31),
              style=0)
        self.tombol_kepemilikan_dokumen.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN)

        self.tombol_menu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_menu', parent=self,
              pos=wx.Point(32, 376), size=wx.Size(240, 31), style=0)
        self.tombol_menu.Bind(wx.EVT_BUTTON, self.OnTombol_menuButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU)

    def __init__(self, parent):
        self._init_ctrls(parent)


    def OnTombol_piramida_pendudukButton(self, event):
        event.Skip()

    def OnTombol_perbandinganButton(self, event):
        event.Skip()

    def OnTombol_pendidikan_akhirButton(self, event):
        event.Skip()

    def OnTombol_pendidikan_sedangButton(self, event):
        event.Skip()

    def OnTombol_kehamilanButton(self, event):
        event.Skip()

    def OnTombol_kontrasepsiButton(self, event):
        event.Skip()

    def OnTombol_giziButton(self, event):
        event.Skip()

    def OnTombol_kepemilikan_dokumenButton(self, event):
        event.Skip()

    def OnTombol_menuButton(self, event):
        self.Close()
