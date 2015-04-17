#Boa:Frame:frm_kependudukan

import wx
import wx.lib.buttons
import kk_sementara
import frm_sideka_menu
import kk_tetap
import tambah_kk_sementara

def create(parent):
    return frm_kependudukan(parent)

[wxID_FRM_KEPENDUDUKAN, wxID_FRM_KEPENDUDUKANKOTAK_PENAMBAHAN, 
 wxID_FRM_KEPENDUDUKANKOTAK_PERISTIWA, wxID_FRM_KEPENDUDUKANLOGO, 
 wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA, 
 wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP, 
 wxID_FRM_KEPENDUDUKANTOMBOL_KELAHIRAN, wxID_FRM_KEPENDUDUKANTOMBOL_KEMATIAN, 
 wxID_FRM_KEPENDUDUKANTOMBOL_KE_MENU_UTAMA, 
 wxID_FRM_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN, 
 wxID_FRM_KEPENDUDUKANTOMBOL_PINDAH, 
 wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA, 
 wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP, 
] = [wx.NewId() for _init_ctrls in range(13)]

class frm_kependudukan(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRM_KEPENDUDUKAN,
              name=u'frm_kependudukan', parent=prnt, pos=wx.Point(487, 280),
              size=wx.Size(455, 316), style=wx.FRAME_NO_TASKBAR,
              title=u'Kependudukan')
        self.SetClientSize(wx.Size(455, 316))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRM_KEPENDUDUKANLOGO, name=u'logo',
              parent=self, pos=wx.Point(16, 8), size=wx.Size(260, 70), style=0)

        self.kotak_penambahan = wx.StaticBox(id=wxID_FRM_KEPENDUDUKANKOTAK_PENAMBAHAN,
              label=u'Penambahan', name=u'kotak_penambahan', parent=self,
              pos=wx.Point(16, 72), size=wx.Size(200, 190), style=0)

        self.kotak_peristiwa = wx.StaticBox(id=wxID_FRM_KEPENDUDUKANKOTAK_PERISTIWA,
              label=u'Peristiwa', name=u'kotak_peristiwa', parent=self,
              pos=wx.Point(232, 72), size=wx.Size(200, 190), style=0)

        self.tombol_buat_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA,
              label=u'Buat KK Sementara', name=u'tombol_buat_kk_sementara',
              parent=self, pos=wx.Point(24, 96), size=wx.Size(184, 31),
              style=0)
        self.tombol_buat_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_sementaraButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_SEMENTARA)

        self.tombol_buat_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP,
              label=u'Buat KK Tetap', name=u'tombol_buat_kk_tetap', parent=self,
              pos=wx.Point(24, 136), size=wx.Size(184, 31), style=0)
        self.tombol_buat_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_buat_kk_tetapButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_BUAT_KK_TETAP)

        self.tombol_tambah_anggota_kk_sementara = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA,
              label=u'Anggota KK Sementara',
              name=u'tombol_tambah_anggota_kk_sementara', parent=self,
              pos=wx.Point(24, 176), size=wx.Size(184, 31), style=0)
        self.tombol_tambah_anggota_kk_sementara.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_sementaraButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_SEMENTARA)

        self.tombol_tambah_anggota_kk_tetap = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP,
              label=u'Anggota KK Tetap', name=u'tombol_tambah_anggota_kk_tetap',
              parent=self, pos=wx.Point(24, 216), size=wx.Size(184, 31),
              style=0)
        self.tombol_tambah_anggota_kk_tetap.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_anggota_kk_tetapButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_TAMBAH_ANGGOTA_KK_TETAP)

        self.tombol_kelahiran = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_KELAHIRAN, label=u'Kelahiran',
              name=u'tombol_kelahiran', parent=self, pos=wx.Point(240, 96),
              size=wx.Size(184, 31), style=0)
        self.tombol_kelahiran.Bind(wx.EVT_BUTTON, self.OnTombol_kelahiranButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_KELAHIRAN)

        self.tombol_kematian = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_KEMATIAN, label=u'Kematian',
              name=u'tombol_kematian', parent=self, pos=wx.Point(240, 136),
              size=wx.Size(184, 31), style=0)
        self.tombol_kematian.Bind(wx.EVT_BUTTON, self.OnTombol_kematianButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_KEMATIAN)

        self.tombol_pindah = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_PINDAH, label=u'Pindah',
              name=u'tombol_pindah', parent=self, pos=wx.Point(240, 176),
              size=wx.Size(184, 31), style=0)
        self.tombol_pindah.Bind(wx.EVT_BUTTON, self.OnTombol_pindahButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_PINDAH)

        self.tombol_peristiwa_lain = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN,
              label=u'Peristiwa Lain', name=u'tombol_peristiwa_lain',
              parent=self, pos=wx.Point(240, 214), size=wx.Size(184, 31),
              style=0)
        self.tombol_peristiwa_lain.Bind(wx.EVT_BUTTON,
              self.OnTombol_peristiwa_lainButton,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_PERISTIWA_LAIN)

        self.tombol_ke_menu_utama = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRM_KEPENDUDUKANTOMBOL_KE_MENU_UTAMA,
              label=u'Kembali Ke Menu Utama', name=u'tombol_ke_menu_utama',
              parent=self, pos=wx.Point(120, 272), size=wx.Size(208, 31),
              style=0)
        self.tombol_ke_menu_utama.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_utamaButton,
              id=wxID_FRM_KEPENDUDUKANGENBITMAPTEXTBUTTON11)

    def __init__(self, parent):
        self._init_ctrls(parent)

   
    def OnTombol_tambah_anggota_kk_sementaraButton(self, event):
        self.main=tambah_kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_tambah_anggota_kk_tetapButton(self, event):
        event.Skip()

    def OnTombol_kelahiranButton(self, event):
        event.Skip()

    def OnTombol_kematianButton(self, event):
        event.Skip()

    def OnTombol_pindahButton(self, event):
        event.Skip()

    def OnTombol_peristiwa_lainButton(self, event):
        event.Skip()

    def OnTombol_ke_menu_utamaButton(self, event):
        event.Skip()

    def OnTombol_buat_kk_sementaraButton(self, event):
        self.main=kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_buat_kk_tetapButton(self, event):
        self.main=kk_tetap.create(None)
        self.main.Show()
        self.Close()
