#Boa:Frame:surat_masuk

import wx
import wx.richtext
import wx.lib.buttons
import input_administrasi_surat

def create(parent):
    return surat_masuk(parent)

[wxID_SURAT_MASUK, wxID_SURAT_MASUKDARI, wxID_SURAT_MASUKDATEPICKERCTRL1, 
 wxID_SURAT_MASUKINPUT_KETERANGAN, wxID_SURAT_MASUKINPUT_NOMOR_SURAT, 
 wxID_SURAT_MASUKKOTAK_SURAT_MASUK, wxID_SURAT_MASUKLABEL_ISI_SINGKAT_SURAT, 
 wxID_SURAT_MASUKLABEL_KETERANGAN, wxID_SURAT_MASUKLABEL_NOMOR_SURAT_MASUK, 
 wxID_SURAT_MASUKLABEL_TANGGAL_SURAT, wxID_SURAT_MASUKLABEL_TUJUAN_SURAT, 
 wxID_SURAT_MASUKPERIHAL, wxID_SURAT_MASUKRICHTEXTCTRL1, 
 wxID_SURAT_MASUKTEXTCTRL1, wxID_SURAT_MASUKTEXTCTRL2, 
 wxID_SURAT_MASUKTOMBOL_KE_MENU_SURAT, wxID_SURAT_MASUKTOMBOL_SIMPAN, 
 wxID_SURAT_MASUKTUJUAN, 
] = [wx.NewId() for _init_ctrls in range(18)]

class surat_masuk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SURAT_MASUK, name=u'surat_masuk',
              parent=prnt, pos=wx.Point(438, 232), size=wx.Size(850, 370),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Surat Masuk')
        self.SetClientSize(wx.Size(850, 370))
        self.Center(wx.BOTH)

        self.label_nomor_surat_masuk = wx.StaticText(id=wxID_SURAT_MASUKLABEL_NOMOR_SURAT_MASUK,
              label=u'Nomor Surat Masuk', name=u'label_nomor_surat_masuk',
              parent=self, pos=wx.Point(40, 48), size=wx.Size(122, 17),
              style=0)

        self.label_tanggal_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_TANGGAL_SURAT,
              label=u'Tanggal Surat', name=u'label_tanggal_surat', parent=self,
              pos=wx.Point(40, 80), size=wx.Size(81, 17), style=0)

        self.label_tujuan_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_TUJUAN_SURAT,
              label=u'Dari', name=u'label_tujuan_surat', parent=self,
              pos=wx.Point(40, 112), size=wx.Size(76, 17), style=0)

        self.label_isi_singkat_surat = wx.StaticText(id=wxID_SURAT_MASUKLABEL_ISI_SINGKAT_SURAT,
              label=u'Isi Singkat Surat', name=u'label_isi_singkat_surat',
              parent=self, pos=wx.Point(40, 144), size=wx.Size(97, 17),
              style=0)

        self.label_keterangan = wx.StaticText(id=wxID_SURAT_MASUKLABEL_KETERANGAN,
              label=u'Disposisi', name=u'label_keterangan', parent=self,
              pos=wx.Point(40, 280), size=wx.Size(88, 17), style=0)

        self.input_nomor_surat = wx.TextCtrl(id=wxID_SURAT_MASUKINPUT_NOMOR_SURAT,
              name=u'input_nomor_surat', parent=self, pos=wx.Point(168, 40),
              size=wx.Size(312, 25), style=0, value=u'')

        self.dari = wx.TextCtrl(id=wxID_SURAT_MASUKDARI, name=u'dari',
              parent=self, pos=wx.Point(168, 104), size=wx.Size(312, 25),
              style=0, value=u'')

        self.input_keterangan = wx.TextCtrl(id=wxID_SURAT_MASUKINPUT_KETERANGAN,
              name=u'input_keterangan', parent=self, pos=wx.Point(168, 280),
              size=wx.Size(656, 25), style=0, value=u'')

        self.kotak_surat_masuk = wx.StaticBox(id=wxID_SURAT_MASUKKOTAK_SURAT_MASUK,
              label=u'Surat masuk Input', name=u'kotak_surat_masuk',
              parent=self, pos=wx.Point(8, 16), size=wx.Size(832, 304),
              style=0)

        self.tombol_simpan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_MASUKTOMBOL_SIMPAN, label=u'Simpan',
              name=u'tombol_simpan', parent=self, pos=wx.Point(280, 328),
              size=wx.Size(176, 31), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_SURAT_MASUKTOMBOL_SIMPAN)

        self.tombol_ke_menu_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SURAT_MASUKTOMBOL_KE_MENU_SURAT,
              label=u'Kembali Ke Menu Surat', name=u'tombol_ke_menu_surat',
              parent=self, pos=wx.Point(464, 328), size=wx.Size(200, 31),
              style=0)
        self.tombol_ke_menu_surat.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_suratButton,
              id=wxID_SURAT_MASUKTOMBOL_KE_MENU_SURAT)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_SURAT_MASUKDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(168, 72),
              size=wx.Size(168, 26), style=wx.DP_SHOWCENTURY)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_SURAT_MASUKRICHTEXTCTRL1,
              parent=self, pos=wx.Point(168, 144), size=wx.Size(656, 128),
              style=wx.richtext.RE_MULTILINE, value='')

        self.tujuan = wx.StaticText(id=wxID_SURAT_MASUKTUJUAN, label=u'Kepada',
              name=u'tujuan', parent=self, pos=wx.Point(488, 112),
              size=wx.Size(48, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_SURAT_MASUKTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(552, 104),
              size=wx.Size(272, 25), style=0, value='')

        self.perihal = wx.StaticText(id=wxID_SURAT_MASUKPERIHAL,
              label=u'Perihal', name=u'perihal', parent=self, pos=wx.Point(488,
              48), size=wx.Size(44, 15), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_SURAT_MASUKTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(552, 40),
              size=wx.Size(272, 25), style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_ke_menu_suratButton(self, event):
        self.main=input_administrasi_surat.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_simpanButton(self, event):
        inputsuratmasuk = str(self.input_tambak.GetValue())
        inputjumlah = str(self.input_jumlah.GetValue())
        inputpemilik = str(self.input_pemilik.GetValue())
        inputketerangan = str(self.richTextCtrl1.GetValue())
        add_tambak="INSERT INTO potensipariwisata (namapotensi, jumlah, pemilik, keterangan) VALUES('"+(inputtambak)+"', '"+(inputjumlah)+"', '"+(inputpemilik)+"', '"+(inputketerangan)+"')"
        cur.execute(add_tambak)
        db.commit()
        self.input_tambak.SetValue('')
        self.input_jumlah.Clear()
        self.input_pemilik.Clear()
        self.richTextCtrl1.Clear()
        self.pesan = wx.MessageDialog(self,"Data Baru Tambak Disimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
