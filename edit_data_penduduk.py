#Boa:Frame:edit_penduduk

import wx
import wx.lib.buttons
import edit_kk_sementara
import frm_sideka_menu
import edit_kk_tetap
import edit_input_anggota_kk_sementara
import edit_input_anggota_kk_tetap
import input_penduduk
import edit_kejadian_kelahiran
import edit_kejadian_kematian
import edit_kejadian_lain

def create(parent):
    return edit_penduduk(parent)

[wxID_EDIT_PENDUDUK, wxID_EDIT_PENDUDUKKOTAK_PENAMBAHAN, 
 wxID_EDIT_PENDUDUKKOTAK_PERISTIWA, 
 wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_SEMENTARA, 
 wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_TETAP, wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN, 
 wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN, wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA, 
 wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN, wxID_EDIT_PENDUDUKTOMBOL_PINDAH, 
 wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA, 
 wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_TETAP, 
] = [wx.NewId() for _init_ctrls in range(12)]

class edit_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_PENDUDUK, name=u'edit_penduduk',
              parent=prnt, pos=wx.Point(622, 281), size=wx.Size(455, 252),
              style=wx.FRAME_NO_TASKBAR, title=u'Edit Data Penduduk')
        self.SetClientSize(wx.Size(455, 252))
        self.Center(wx.BOTH)

        self.kotak_penambahan = wx.StaticBox(id=wxID_EDIT_PENDUDUKKOTAK_PENAMBAHAN,
              label=u'Edit Penambahan', name=u'kotak_penambahan', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(200, 190), style=0)

        self.kotak_peristiwa = wx.StaticBox(id=wxID_EDIT_PENDUDUKKOTAK_PERISTIWA,
              label=u'Edit Peristiwa', name=u'kotak_peristiwa', parent=self,
              pos=wx.Point(232, 16), size=wx.Size(200, 190), style=0)

        self.tombol_buat_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_SEMENTARA,
              label=u'Edit KK Sementara', name=u'tombol_buat_kk_sementara',
              parent=self, pos=wx.Point(24, 40), size=wx.Size(184, 31),
              style=0)
        self.tombol_buat_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_sementaraButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_SEMENTARA)

        self.tombol_buat_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_TETAP, label=u'Edit KK Tetap',
              name=u'tombol_buat_kk_tetap', parent=self, pos=wx.Point(24, 80),
              size=wx.Size(184, 31), style=0)
        self.tombol_buat_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_tetapButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_BUAT_KK_TETAP)

        self.tombol_tambah_anggota_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA,
              label=u'Edit Anggota KKS',
              name=u'tombol_tambah_anggota_kk_sementara', parent=self,
              pos=wx.Point(24, 120), size=wx.Size(184, 31), style=0)
        self.tombol_tambah_anggota_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_sementaraButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA)

        self.tombol_tambah_anggota_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_TETAP,
              label=u'Edit Anggota KK Tetap',
              name=u'tombol_tambah_anggota_kk_tetap', parent=self,
              pos=wx.Point(24, 160), size=wx.Size(184, 31), style=0)
        self.tombol_tambah_anggota_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_tetapButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_TAMBAH_ANGGOTA_KK_TETAP)

        self.tombol_kelahiran = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN, label=u'Edit Kelahiran',
              name=u'tombol_kelahiran', parent=self, pos=wx.Point(240, 40),
              size=wx.Size(184, 31), style=0)
        self.tombol_kelahiran.Bind(wx.EVT_BUTTON, self.OnTombol_kelahiranButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN)

        self.tombol_kematian = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN, label=u'Edit Kematian',
              name=u'tombol_kematian', parent=self, pos=wx.Point(240, 80),
              size=wx.Size(184, 31), style=0)
        self.tombol_kematian.Bind(wx.EVT_BUTTON, self.OnTombol_kematianButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN)

        self.tombol_pindah = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_PINDAH, label=u'Edit Pindah',
              name=u'tombol_pindah', parent=self, pos=wx.Point(240, 120),
              size=wx.Size(184, 31), style=0)
        self.tombol_pindah.Bind(wx.EVT_BUTTON, self.OnTombol_pindahButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_PINDAH)

        self.tombol_peristiwa_lain = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN,
              label=u'Edit Peristiwa Lain', name=u'tombol_peristiwa_lain',
              parent=self, pos=wx.Point(240, 158), size=wx.Size(184, 31),
              style=0)
        self.tombol_peristiwa_lain.Bind(wx.EVT_BUTTON,
              self.OnTombol_peristiwa_lainButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN)

        self.tombol_ke_menu_utama = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA,
              label=u'Kembali Ke Menu Utama', name=u'tombol_ke_menu_utama',
              parent=self, pos=wx.Point(128, 216), size=wx.Size(208, 31),
              style=0)
        self.tombol_ke_menu_utama.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_utamaButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA)

    def __init__(self, parent):
        self._init_ctrls(parent)

   
    def OnTombol_tambah_anggota_kk_sementaraButton(self, event):
        self.main=edit_input_anggota_kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_tambah_anggota_kk_tetapButton(self, event):
        self.main=edit_input_anggota_kk_tetap.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_kelahiranButton(self, event):
        self.main=edit_kejadian_kelahiran.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_kematianButton(self, event):
        self.main=edit_kejadian_kematian.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_pindahButton(self, event):
        event.Skip()

    def OnTombol_peristiwa_lainButton(self, event):
        self.main=edit_kejadian_lain.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_ke_menu_utamaButton(self, event):
        self.Close()
        event.Skip()

    def OnTombol_buat_kk_sementaraButton(self, event):
        self.main=edit_kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_buat_kk_tetapButton(self, event):
        self.main=edit_kk_tetap.create(None)
        self.main.Show()
        self.Close()

   
