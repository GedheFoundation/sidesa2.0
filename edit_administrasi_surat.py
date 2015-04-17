#Boa:Frame:administrasi_surat

import wx
import wx.lib.buttons

def create(parent):
    return administrasi_surat(parent)

[wxID_ADMINISTRASI_SURAT, 
 wxID_ADMINISTRASI_SURATKOTAK_ADMINISTRASI_KEPENDUDUKAN, 
 wxID_ADMINISTRASI_SURATKOTAK_EDIT_SURAT, 
 wxID_ADMINISTRASI_SURATKOTAK_LAYANAN_UMUM, 
 wxID_ADMINISTRASI_SURATKOTAK_PERIJINAN, wxID_ADMINISTRASI_SURATLOGO, 
 wxID_ADMINISTRASI_SURATTOMBOL_ADM_LAINNYA, 
 wxID_ADMINISTRASI_SURATTOMBOL_DOMISILI, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_IJIN_LAINNYA, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTP, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTR, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTR_LAINNYA, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_MENEBANG, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SKCK, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SURAT_KELUAR, 
 wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SURAT_MASUK, 
 wxID_ADMINISTRASI_SURATTOMBOL_KEMBALI_KEMENU, 
] = [wx.NewId() for _init_ctrls in range(17)]

class administrasi_surat(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ADMINISTRASI_SURAT,
              name=u'administrasi_surat', parent=prnt, pos=wx.Point(493, 263),
              size=wx.Size(469, 368), style=wx.FRAME_NO_TASKBAR,
              title=u'Edit Administrasi Persuratan')
        self.SetClientSize(wx.Size(469, 368))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ADMINISTRASI_SURATLOGO, name=u'logo',
              parent=self, pos=wx.Point(24, 0), size=wx.Size(288, 65), style=0)

        self.kotak_edit_surat = wx.StaticBox(id=wxID_ADMINISTRASI_SURATKOTAK_EDIT_SURAT,
              label=u'Edit Persuratan', name=u'kotak_edit_surat', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(200, 100), style=0)

        self.kotak_administrasi_kependudukan = wx.StaticBox(id=wxID_ADMINISTRASI_SURATKOTAK_ADMINISTRASI_KEPENDUDUKAN,
              label=u'Administrasi Kependudukan',
              name=u'kotak_administrasi_kependudukan', parent=self,
              pos=wx.Point(24, 168), size=wx.Size(200, 152), style=0)

        self.tombol_edit_surat_masuk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SURAT_MASUK,
              label=u'Edit Surat Masuk', name=u'tombol_edit_surat_masuk',
              parent=self, pos=wx.Point(40, 88), size=wx.Size(168, 31),
              style=0)

        self.tombol_edit_ktp = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTP,
              label=u'Edit Pengantar KTP', name=u'tombol_edit_ktp', parent=self,
              pos=wx.Point(40, 192), size=wx.Size(168, 31), style=0)

        self.tombol_edit_skck = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SKCK,
              label=u'Edit  Pengantar SKCK', name=u'tombol_edit_skck',
              parent=self, pos=wx.Point(40, 232), size=wx.Size(168, 31),
              style=0)

        self.tombol_adm_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_ADM_LAINNYA,
              label=u'Edit Surat Lainnya', name=u'tombol_adm_lainnya',
              parent=self, pos=wx.Point(40, 272), size=wx.Size(168, 31),
              style=0)

        self.kotak_layanan_umum = wx.StaticBox(id=wxID_ADMINISTRASI_SURATKOTAK_LAYANAN_UMUM,
              label=u'Layanan Umum', name=u'kotak_layanan_umum', parent=self,
              pos=wx.Point(232, 64), size=wx.Size(216, 152), style=0)

        self.tombol_edit_ktr = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTR,
              label=u'Edit Ktr. Tidak Mampu', name=u'tombol_edit_ktr',
              parent=self, pos=wx.Point(248, 92), size=wx.Size(184, 31),
              style=0)

        self.tombol_domisili = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_DOMISILI,
              label=u'Edit Keterangan Domisili', name=u'tombol_domisili',
              parent=self, pos=wx.Point(248, 136), size=wx.Size(184, 31),
              style=0)

        self.tombol_edit_ktr_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_KTR_LAINNYA,
              label=u'Edit Keterangan Lainnya', name=u'tombol_edit_ktr_lainnya',
              parent=self, pos=wx.Point(248, 176), size=wx.Size(184, 31),
              style=0)

        self.kotak_perijinan = wx.StaticBox(id=wxID_ADMINISTRASI_SURATKOTAK_PERIJINAN,
              label=u'Perijinan', name=u'kotak_perijinan', parent=self,
              pos=wx.Point(232, 216), size=wx.Size(216, 104), style=0)

        self.tombol_edit_menebang = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_MENEBANG,
              label=u'Edit Ijin Menebang Pohon', name=u'tombol_edit_menebang',
              parent=self, pos=wx.Point(248, 240), size=wx.Size(184, 31),
              style=0)

        self.tombol_edit_ijin_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_IJIN_LAINNYA,
              label=u'Edit Ijin Lainnya', name=u'tombol_edit_ijin_lainnya',
              parent=self, pos=wx.Point(248, 280), size=wx.Size(184, 31),
              style=0)

        self.tombol_edit_surat_keluar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_EDIT_SURAT_KELUAR,
              label=u'Edit Surat Keluar', name=u'tombol_edit_surat_keluar',
              parent=self, pos=wx.Point(40, 128), size=wx.Size(168, 31),
              style=0)

        self.tombol_kembali_kemenu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADMINISTRASI_SURATTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(152, 328), size=wx.Size(184, 31),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton11Button,
              id=wxID_ADMINISTRASI_SURATTOMBOL_KEMBALI_KEMENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton11Button(self, event):
        event.Skip()
