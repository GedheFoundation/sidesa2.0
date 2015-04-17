#Boa:Frame:profil_desa

import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return profil_desa(parent)

[wxID_PROFIL_DESA, wxID_PROFIL_DESAINPUT_DUSUN, 
 wxID_PROFIL_DESAINPUT_KABUPATEN, wxID_PROFIL_DESAINPUT_KANTOR, 
 wxID_PROFIL_DESAINPUT_KECAMATAN, wxID_PROFIL_DESAINPUT_KODEPOS, 
 wxID_PROFIL_DESAINPUT_RT, wxID_PROFIL_DESAINPUT_RW, 
 wxID_PROFIL_DESAINPUT_TELP, wxID_PROFIL_DESAKOTAK_DUSUN, 
 wxID_PROFIL_DESAKOTAK_INFORMASI, wxID_PROFIL_DESAKOTAK_RT, 
 wxID_PROFIL_DESAKOTAK_RW, wxID_PROFIL_DESALABEL_ALAMAT_KANTOR, 
 wxID_PROFIL_DESALABEL_KABUPATEN, wxID_PROFIL_DESALABEL_KECAMATAN, 
 wxID_PROFIL_DESALABEL_KODE_POS, wxID_PROFIL_DESALABEL_NO_TELP, 
 wxID_PROFIL_DESALABEL_PROPINSI, wxID_PROFIL_DESALOGO, 
 wxID_PROFIL_DESATEXT_PROPINSI, wxID_PROFIL_DESATOMBOL_KE_MENU_UTAMA, 
 wxID_PROFIL_DESATOMBOL_SIMPAN_DATA, wxID_PROFIL_DESATOMBOL_TAMBAH_DUSUN, 
 wxID_PROFIL_DESATOMBOL_TAMBAH_RT, wxID_PROFIL_DESATOMBOL_TAMBAH_RW, 
] = [wx.NewId() for _init_ctrls in range(26)]

class profil_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PROFIL_DESA, name=u'profil_desa',
              parent=prnt, pos=wx.Point(313, 276), size=wx.Size(911, 374),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Input Profil Desa')
        self.SetClientSize(wx.Size(911, 374))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_PROFIL_DESALOGO, name=u'logo',
              parent=self, pos=wx.Point(24, 0), size=wx.Size(288, 72), style=0)

        self.kotak_informasi = wx.StaticBox(id=wxID_PROFIL_DESAKOTAK_INFORMASI,
              label=u'Informasi Umum', name=u'kotak_informasi', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(872, 160), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_PROFIL_DESALABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(32, 80), size=wx.Size(50, 17), style=0)

        self.text_propinsi = wx.TextCtrl(id=wxID_PROFIL_DESATEXT_PROPINSI,
              name=u'text_propinsi', parent=self, pos=wx.Point(32, 96),
              size=wx.Size(256, 25), style=0, value=u'')

        self.label_kabupaten = wx.StaticText(id=wxID_PROFIL_DESALABEL_KABUPATEN,
              label=u'Kabupaten', name=u'label_kabupaten', parent=self,
              pos=wx.Point(304, 80), size=wx.Size(67, 17), style=0)

        self.input_kabupaten = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_KABUPATEN,
              name=u'input_kabupaten', parent=self, pos=wx.Point(304, 96),
              size=wx.Size(264, 25), style=0, value=u'')

        self.label_kecamatan = wx.StaticText(id=wxID_PROFIL_DESALABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(584, 80), size=wx.Size(68, 17), style=0)

        self.input_kecamatan = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_KECAMATAN,
              name=u'input_kecamatan', parent=self, pos=wx.Point(584, 96),
              size=wx.Size(288, 25), style=0, value=u'')

        self.label_alamat_kantor = wx.StaticText(id=wxID_PROFIL_DESALABEL_ALAMAT_KANTOR,
              label=u'Alamat Kantor', name=u'label_alamat_kantor', parent=self,
              pos=wx.Point(32, 128), size=wx.Size(87, 17), style=0)

        self.input_kantor = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_KANTOR,
              name=u'input_kantor', parent=self, pos=wx.Point(32, 144),
              size=wx.Size(536, 25), style=0, value=u'')

        self.label_kode_pos = wx.StaticText(id=wxID_PROFIL_DESALABEL_KODE_POS,
              label=u'Kode Pos', name=u'label_kode_pos', parent=self,
              pos=wx.Point(584, 128), size=wx.Size(57, 17), style=0)

        self.input_kodepos = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_KODEPOS,
              name=u'input_kodepos', parent=self, pos=wx.Point(584, 144),
              size=wx.Size(136, 25), style=0, value=u'')

        self.label_no_telp = wx.StaticText(id=wxID_PROFIL_DESALABEL_NO_TELP,
              label=u'No. Telp', name=u'label_no_telp', parent=self,
              pos=wx.Point(736, 128), size=wx.Size(50, 17), style=0)

        self.input_telp = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_TELP,
              name=u'input_telp', parent=self, pos=wx.Point(736, 144),
              size=wx.Size(136, 25), style=0, value=u'')

        self.tombol_simpan_data = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PROFIL_DESATOMBOL_SIMPAN_DATA, label=u'Simpan Data',
              name=u'tombol_simpan_data', parent=self, pos=wx.Point(704, 176),
              size=wx.Size(168, 31), style=0)

        self.kotak_dusun = wx.StaticBox(id=wxID_PROFIL_DESAKOTAK_DUSUN,
              label=u'Dusun', name=u'kotak_dusun', parent=self, pos=wx.Point(16,
              216), size=wx.Size(592, 100), style=0)

        self.kotak_rw = wx.StaticBox(id=wxID_PROFIL_DESAKOTAK_RW, label=u'RW',
              name=u'kotak_rw', parent=self, pos=wx.Point(616, 216),
              size=wx.Size(130, 100), style=0)

        self.kotak_rt = wx.StaticBox(id=wxID_PROFIL_DESAKOTAK_RT, label=u'RT',
              name=u'kotak_rt', parent=self, pos=wx.Point(760, 216),
              size=wx.Size(130, 100), style=0)

        self.input_dusun = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(24, 240),
              size=wx.Size(576, 25), style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(632, 240),
              size=wx.Size(100, 25), style=0, value=u'')

        self.tombol_tambah_dusun = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PROFIL_DESATOMBOL_TAMBAH_DUSUN, label=u'Tambah',
              name=u'tombol_tambah_dusun', parent=self, pos=wx.Point(512, 272),
              size=wx.Size(86, 31), style=0)

        self.tombol_tambah_rw = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PROFIL_DESATOMBOL_TAMBAH_RW, label=u'Tambah',
              name=u'tombol_tambah_rw', parent=self, pos=wx.Point(640, 272),
              size=wx.Size(86, 31), style=0)

        self.tombol_tambah_rt = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PROFIL_DESATOMBOL_TAMBAH_RT, label=u'Tambah',
              name=u'tombol_tambah_rt', parent=self, pos=wx.Point(784, 272),
              size=wx.Size(86, 31), style=0)

        self.input_rt = wx.TextCtrl(id=wxID_PROFIL_DESAINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(776, 240),
              size=wx.Size(96, 25), style=0, value=u'')

        self.tombol_ke_menu_utama = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PROFIL_DESATOMBOL_KE_MENU_UTAMA,
              label=u'Kembali Ke Menu Utama', name=u'tombol_ke_menu_utama',
              parent=self, pos=wx.Point(368, 328), size=wx.Size(224, 31),
              style=0)
        self.tombol_ke_menu_utama.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_utamaButton,
              id=wxID_PROFIL_DESATOMBOL_KE_MENU_UTAMA)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_ke_menu_utamaButton(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()

