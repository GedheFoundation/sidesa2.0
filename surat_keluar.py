#Boa:Frame:surat_keluar

import wx
import wx.lib.buttons

def create(parent):
    return surat_keluar(parent)

[wxID_SURAT_KELUAR, wxID_SURAT_KELUARINPUT_ISI_SURAT, 
 wxID_SURAT_KELUARINPUT_KETERANGAN, wxID_SURAT_KELUARINPUT_NOMOR_SURAT, 
 wxID_SURAT_KELUARINPUT_TANGGAL_SURAT, wxID_SURAT_KELUARINPUT_TUJUAN_SURAT, 
 wxID_SURAT_KELUARKOTAK_SURAT_KELUAR, 
 wxID_SURAT_KELUARLABEL_ISI_SINGKAT_SURAT, wxID_SURAT_KELUARLABEL_KETERANGAN, 
 wxID_SURAT_KELUARLABEL_NOMOR_SURAT_KELUAR, 
 wxID_SURAT_KELUARLABEL_TANGGAL_SURAT, wxID_SURAT_KELUARLABEL_TUJUAN_SURAT, 
 wxID_SURAT_KELUARLOGO, wxID_SURAT_KELUARTOMBOL_KE_MENU_SURAT, 
 wxID_SURAT_KELUARTOMBOL_SIMPAN, wxID_SURAT_KELUARTOMBOL_SIMPAN_CETAK, 
] = [wx.NewId() for _init_ctrls in range(16)]

class surat_keluar(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SURAT_KELUAR, name=u'surat_keluar',
              parent=prnt, pos=wx.Point(307, 214), size=wx.Size(857, 429),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Surat Keluar')
        self.SetClientSize(wx.Size(857, 429))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SURAT_KELUARLOGO, name=u'logo',
              parent=self, pos=wx.Point(24, 8), size=wx.Size(288, 65), style=0)

        self.label_nomor_surat_keluar = wx.StaticText(id=wxID_SURAT_KELUARLABEL_NOMOR_SURAT_KELUAR,
              label=u'Nomor Surat Keluar', name=u'label_nomor_surat_keluar',
              parent=self, pos=wx.Point(40, 104), size=wx.Size(120, 17),
              style=0)

        self.label_tanggal_surat = wx.StaticText(id=wxID_SURAT_KELUARLABEL_TANGGAL_SURAT,
              label=u'Tanggal Surat', name=u'label_tanggal_surat', parent=self,
              pos=wx.Point(40, 136), size=wx.Size(81, 17), style=0)

        self.label_tujuan_surat = wx.StaticText(id=wxID_SURAT_KELUARLABEL_TUJUAN_SURAT,
              label=u'Tujuan Surat', name=u'label_tujuan_surat', parent=self,
              pos=wx.Point(40, 168), size=wx.Size(76, 17), style=0)

        self.label_isi_singkat_surat = wx.StaticText(id=wxID_SURAT_KELUARLABEL_ISI_SINGKAT_SURAT,
              label=u'Isi Singkat Surat', name=u'label_isi_singkat_surat',
              parent=self, pos=wx.Point(40, 200), size=wx.Size(97, 17),
              style=0)

        self.label_keterangan = wx.StaticText(id=wxID_SURAT_KELUARLABEL_KETERANGAN,
              label=u'Keterangan', name=u'label_keterangan', parent=self,
              pos=wx.Point(48, 304), size=wx.Size(70, 17), style=0)

        self.input_nomor_surat = wx.TextCtrl(id=wxID_SURAT_KELUARINPUT_NOMOR_SURAT,
              name=u'input_nomor_surat', parent=self, pos=wx.Point(168, 104),
              size=wx.Size(312, 25), style=0, value=u'')

        self.input_tanggal_surat = wx.TextCtrl(id=wxID_SURAT_KELUARINPUT_TANGGAL_SURAT,
              name=u'input_tanggal_surat', parent=self, pos=wx.Point(168, 136),
              size=wx.Size(312, 25), style=0, value=u'')

        self.input_tujuan_surat = wx.TextCtrl(id=wxID_SURAT_KELUARINPUT_TUJUAN_SURAT,
              name=u'input_tujuan_surat', parent=self, pos=wx.Point(168, 168),
              size=wx.Size(312, 25), style=0, value=u'')

        self.input_isi_surat = wx.TextCtrl(id=wxID_SURAT_KELUARINPUT_ISI_SURAT,
              name=u'input_isi_surat', parent=self, pos=wx.Point(168, 200),
              size=wx.Size(656, 96), style=0, value=u'')

        self.input_keterangan = wx.TextCtrl(id=wxID_SURAT_KELUARINPUT_KETERANGAN,
              name=u'input_keterangan', parent=self, pos=wx.Point(168, 304),
              size=wx.Size(656, 25), style=0, value=u'')

        self.kotak_surat_keluar = wx.StaticBox(id=wxID_SURAT_KELUARKOTAK_SURAT_KELUAR,
              label=u'Surat Keluar Input', name=u'kotak_surat_keluar',
              parent=self, pos=wx.Point(8, 72), size=wx.Size(832, 304),
              style=0)

        self.tombol_simpan_cetak = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_KELUARTOMBOL_SIMPAN_CETAK, label=u'Simpan & Cetak',
              name=u'tombol_simpan_cetak', parent=self, pos=wx.Point(168, 384),
              size=wx.Size(176, 31), style=0)

        self.tombol_simpan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_KELUARTOMBOL_SIMPAN, label=u'Simpan',
              name=u'tombol_simpan', parent=self, pos=wx.Point(352, 384),
              size=wx.Size(176, 31), style=0)

        self.tombol_ke_menu_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_KELUARTOMBOL_KE_MENU_SURAT,
              label=u'Kembali Ke Menu Surat', name=u'tombol_ke_menu_surat',
              parent=self, pos=wx.Point(536, 384), size=wx.Size(168, 31),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
