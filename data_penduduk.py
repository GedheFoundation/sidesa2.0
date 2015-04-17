#Boa:Frame:menu_data_kependudukan

import wx
import wx.lib.buttons
import kk_sementara
import frm_sideka_menu
import kk_tetap
import tambah_kk_sementara
import tambah_kk_tetap
import input_penduduk
import pecah_keluarga
import kejadian_kelahiran
import kejadian_kematian
import kejadian_lain

def create(parent):
    return menu_data_kependudukan(parent)

[wxID_MENU_DATA_KEPENDUDUKAN, wxID_MENU_DATA_KEPENDUDUKANKOTAK_PENAMBAHAN, 
 wxID_MENU_DATA_KEPENDUDUKANKOTAK_PERISTIWA, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KELAHIRAN, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KEMATIAN, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KE_MENU_UTAMA, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PECAH_KELUARGA, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PINDAH, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA, 
 wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP, 
] = [wx.NewId() for _init_ctrls in range(13)]

class menu_data_kependudukan(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MENU_DATA_KEPENDUDUKAN,
              name=u'menu_data_kependudukan', parent=prnt, pos=wx.Point(622,
              249), size=wx.Size(455, 316), style=wx.FRAME_NO_TASKBAR,
              title=u'Kependudukan')
        self.SetClientSize(wx.Size(455, 316))
        self.Center(wx.BOTH)

        self.kotak_penambahan = wx.StaticBox(id=wxID_MENU_DATA_KEPENDUDUKANKOTAK_PENAMBAHAN,
              label=u'Penambahan', name=u'kotak_penambahan', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(200, 232), style=0)

        self.kotak_peristiwa = wx.StaticBox(id=wxID_MENU_DATA_KEPENDUDUKANKOTAK_PERISTIWA,
              label=u'Peristiwa', name=u'kotak_peristiwa', parent=self,
              pos=wx.Point(232, 16), size=wx.Size(200, 232), style=0)

        self.tombol_buat_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA,
              label=u'Buat KK Sementara', name=u'tombol_buat_kk_sementara',
              parent=self, pos=wx.Point(24, 40), size=wx.Size(184, 31),
              style=0)
        self.tombol_buat_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_sementaraButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA)

        self.tombol_buat_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP,
              label=u'Buat KK Tetap', name=u'tombol_buat_kk_tetap', parent=self,
              pos=wx.Point(24, 80), size=wx.Size(184, 31), style=0)
        self.tombol_buat_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_tetapButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP)

        self.tombol_tambah_anggota_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA,
              label=u'Anggota KK Sementara',
              name=u'tombol_tambah_anggota_kk_sementara', parent=self,
              pos=wx.Point(24, 120), size=wx.Size(184, 31), style=0)
        self.tombol_tambah_anggota_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_sementaraButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA)

        self.tombol_tambah_anggota_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP,
              label=u'Anggota KK Tetap', name=u'tombol_tambah_anggota_kk_tetap',
              parent=self, pos=wx.Point(24, 160), size=wx.Size(184, 31),
              style=0)
        self.tombol_tambah_anggota_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_tetapButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP)

        self.tombol_kelahiran = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KELAHIRAN,
              label=u'Kelahiran', name=u'tombol_kelahiran', parent=self,
              pos=wx.Point(240, 40), size=wx.Size(184, 31), style=0)
        self.tombol_kelahiran.Bind(wx.EVT_BUTTON, self.OnTombol_kelahiranButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KELAHIRAN)

        self.tombol_kematian = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KEMATIAN, label=u'Kematian',
              name=u'tombol_kematian', parent=self, pos=wx.Point(240, 80),
              size=wx.Size(184, 31), style=0)
        self.tombol_kematian.Bind(wx.EVT_BUTTON, self.OnTombol_kematianButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KEMATIAN)

        self.tombol_pindah = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PINDAH, label=u'Pindah',
              name=u'tombol_pindah', parent=self, pos=wx.Point(240, 120),
              size=wx.Size(184, 31), style=0)
        self.tombol_pindah.Bind(wx.EVT_BUTTON, self.OnTombol_pindahButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PINDAH)

        self.tombol_peristiwa_lain = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN,
              label=u'Peristiwa Lain', name=u'tombol_peristiwa_lain',
              parent=self, pos=wx.Point(240, 158), size=wx.Size(184, 31),
              style=0)
        self.tombol_peristiwa_lain.Bind(wx.EVT_BUTTON,
              self.OnTombol_peristiwa_lainButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN)

        self.tombol_ke_menu_utama = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KE_MENU_UTAMA,
              label=u'Kembali Ke Menu Utama', name=u'tombol_ke_menu_utama',
              parent=self, pos=wx.Point(120, 272), size=wx.Size(208, 31),
              style=0)
        self.tombol_ke_menu_utama.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_utamaButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_KE_MENU_UTAMA)

        self.tombol_pecah_keluarga = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PECAH_KELUARGA,
              label=u'Pecah Keluarga', name=u'tombol_pecah_keluarga',
              parent=self, pos=wx.Point(24, 200), size=wx.Size(184, 31),
              style=0)
        self.tombol_pecah_keluarga.Bind(wx.EVT_BUTTON,
              self.OnTombol_pecah_keluargaButton,
              id=wxID_MENU_DATA_KEPENDUDUKANTOMBOL_PECAH_KELUARGA)

    def __init__(self, parent):
        self._init_ctrls(parent)

   
    def OnTombol_tambah_anggota_kk_sementaraButton(self, event):
        self.main=tambah_kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_tambah_anggota_kk_tetapButton(self, event):
        self.main=tambah_kk_tetap.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_kelahiranButton(self, event):
        self.main=kejadian_kelahiran.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_kematianButton(self, event):
        self.main=kejadian_kematian.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_pindahButton(self, event):
        event.Skip()

    def OnTombol_peristiwa_lainButton(self, event):
        self.main=kejadian_lain.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_ke_menu_utamaButton(self, event):
        self.Close()

    def OnTombol_buat_kk_sementaraButton(self, event):
        self.main=kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_buat_kk_tetapButton(self, event):
        self.main=kk_tetap.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_pecah_keluargaButton(self, event):
        self.main=pecah_keluarga.create(None)
        self.main.Show()
        self.Close()
