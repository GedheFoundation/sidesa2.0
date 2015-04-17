#Boa:Frame:penduduk

import wx
import wx.lib.buttons
import data_penduduk

def create(parent):
    return penduduk(parent)

[wxID_PENDUDUK, wxID_PENDUDUKGENBITMAPTEXTBUTTON1, 
 wxID_PENDUDUKGENBITMAPTEXTBUTTON10, wxID_PENDUDUKGENBITMAPTEXTBUTTON2, 
 wxID_PENDUDUKGENBITMAPTEXTBUTTON3, wxID_PENDUDUKGENBITMAPTEXTBUTTON4, 
 wxID_PENDUDUKGENBITMAPTEXTBUTTON5, wxID_PENDUDUKGENBITMAPTEXTBUTTON6, 
 wxID_PENDUDUKGENBITMAPTEXTBUTTON7, wxID_PENDUDUKGENBITMAPTEXTBUTTON8, 
 wxID_PENDUDUKGENBITMAPTEXTBUTTON9, wxID_PENDUDUKINPUT_AGAMA, 
 wxID_PENDUDUKINPUT_GOL_DARAH, wxID_PENDUDUKINPUT_JK, 
 wxID_PENDUDUKINPUT_KEPENDUDUKAN, wxID_PENDUDUKINPUT_NAMA, 
 wxID_PENDUDUKINPUT_NIK, wxID_PENDUDUKINPUT_NO_KK, 
 wxID_PENDUDUKINPUT_PEKERJAAN, wxID_PENDUDUKINPUT_PENDIDIKAN_TERAKHIR, 
 wxID_PENDUDUKINPUT_STATUS, wxID_PENDUDUKINPUT_TEMPAT_LAHIR, 
 wxID_PENDUDUKINPUT_WARGA_NEGARA, wxID_PENDUDUKKOTAK_CATATAN, 
 wxID_PENDUDUKKOTAK_DATA_KELUARGA, wxID_PENDUDUKKOTAK_DATA_PENDUDUK, 
 wxID_PENDUDUKKOTAK_PROSES, wxID_PENDUDUKLABEL_AGAMA, 
 wxID_PENDUDUKLABEL_GOLONGAN_DARAH, wxID_PENDUDUKLABEL_JENIS_KELAMIN, 
 wxID_PENDUDUKLABEL_KEWARGANEGARAAN, wxID_PENDUDUKLABEL_NAMA_LENGKAP, 
 wxID_PENDUDUKLABEL_NAMA_PENDUDUK, wxID_PENDUDUKLABEL_PEKERJAAN, 
 wxID_PENDUDUKLABEL_PENDIDIKAN_TERAKHIR, 
 wxID_PENDUDUKLABEL_STATUS_KEPENDUDUKAN, wxID_PENDUDUKLABEL_STATUS_PERKAWINAN, 
 wxID_PENDUDUKLABEL_TANGGAL_LAHIR, wxID_PENDUDUKLABEL_TEMPAT_LAHIR, 
 wxID_PENDUDUKLEBEL_NIK, wxID_PENDUDUKLOGO, wxID_PENDUDUKPHOTO, 
 wxID_PENDUDUKPILIHPHOTO, wxID_PENDUDUKTANGGAL_LAHIR, 
 wxID_PENDUDUKTOMBOL_KEMBALI_KEMENU, wxID_PENDUDUKTOMBOL_PENCARIAN_KK, 
] = [wx.NewId() for _init_ctrls in range(46)]

class penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PENDUDUK, name=u'penduduk', parent=prnt,
              pos=wx.Point(333, 189), size=wx.Size(906, 516),
              style=wx.FRAME_NO_TASKBAR, title=u'Data Penduduk')
        self.SetClientSize(wx.Size(906, 516))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_PENDUDUKLOGO, name=u'logo',
              parent=self, pos=wx.Point(12, 4), size=wx.Size(276, 65), style=0)

        self.kotak_data_keluarga = wx.StaticBox(id=wxID_PENDUDUKKOTAK_DATA_KELUARGA,
              label=u'Data Keluarga', name=u'kotak_data_keluarga', parent=self,
              pos=wx.Point(8, 64), size=wx.Size(600, 80), style=0)

        self.label_nama_penduduk = wx.StaticText(id=wxID_PENDUDUKLABEL_NAMA_PENDUDUK,
              label=u'Nama Penduduk', name=u'label_nama_penduduk', parent=self,
              pos=wx.Point(24, 88), size=wx.Size(102, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_PENDUDUKINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(24, 104),
              size=wx.Size(240, 25), style=0, value=u'')

        self.kotak_data_penduduk = wx.StaticBox(id=wxID_PENDUDUKKOTAK_DATA_PENDUDUK,
              label=u'Data Penduduk', name=u'kotak_data_penduduk', parent=self,
              pos=wx.Point(8, 144), size=wx.Size(600, 352), style=0)

        self.photo = wx.StaticBitmap(bitmap=wx.Bitmap('png/photo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_PENDUDUKPHOTO, name=u'photo',
              parent=self, pos=wx.Point(24, 184), size=wx.Size(110, 140),
              style=0)

        self.pilihphoto = wx.FilePickerCtrl(id=wxID_PENDUDUKPILIHPHOTO,
              name=u'pilihphoto', parent=self, pos=wx.Point(18, 330),
              size=wx.Size(152, 26),
              style=wx.FLP_OPEN | wx.FLP_FILE_MUST_EXIST | wx.FLP_USE_TEXTCTRL)

        self.input_nik = wx.TextCtrl(id=wxID_PENDUDUKINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(176, 176),
              size=wx.Size(200, 25), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_PENDUDUKLEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(176, 160), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_PENDUDUKLABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(176, 208), size=wx.Size(98, 17), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_PENDUDUKINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(176, 224),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_PENDUDUKLABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(176, 256), size=wx.Size(84, 17), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_PENDUDUKINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(176, 320),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_tempat_lahir = wx.StaticText(id=wxID_PENDUDUKLABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(176, 304), size=wx.Size(83, 17), style=0)

        self.kotak_catatan = wx.StaticBox(id=wxID_PENDUDUKKOTAK_CATATAN,
              label=u'Catatan', name=u'kotak_catatan', parent=self,
              pos=wx.Point(296, 0), size=wx.Size(600, 65), style=0)

        self.tombol_kembali_kemenu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(640, 24), size=wx.Size(240, 31),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_PENDUDUKTOMBOL_KEMBALI_KEMENU)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_PENDUDUKLABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(176, 352), size=wx.Size(79, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_PENDUDUKLABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(176, 400), size=wx.Size(98, 17),
              style=0)

        self.label_agama = wx.StaticText(id=wxID_PENDUDUKLABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 160), size=wx.Size(42, 17), style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_PENDUDUKLABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 208), size=wx.Size(108, 17),
              style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_PENDUDUKLABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 256), size=wx.Size(119, 17),
              style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_PENDUDUKLABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(103, 17), style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_PENDUDUKLABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(400, 304), size=wx.Size(112, 17),
              style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_PENDUDUKLABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(400, 400), size=wx.Size(134, 17),
              style=0)

        self.tanggal_lahir = wx.DatePickerCtrl(id=wxID_PENDUDUKTANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(176, 368),
              size=wx.Size(200, 26), style=wx.DP_SHOWCENTURY)

        self.tombol_pencarian_kk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKTOMBOL_PENCARIAN_KK,
              label=u'Cari Nomo Kartu Keluarga', name=u'tombol_pencarian_kk',
              parent=self, pos=wx.Point(280, 96), size=wx.Size(200, 31),
              style=0)

        self.kotak_proses = wx.StaticBox(id=wxID_PENDUDUKKOTAK_PROSES,
              label=u'Proses Kependudukan', name=u'kotak_proses', parent=self,
              pos=wx.Point(616, 64), size=wx.Size(280, 432), style=0)

        self.input_jk = wx.TextCtrl(id=wxID_PENDUDUKINPUT_JK, name=u'input_jk',
              parent=self, pos=wx.Point(176, 272), size=wx.Size(200, 25),
              style=0, value=u'')

        self.input_agama = wx.TextCtrl(id=wxID_PENDUDUKINPUT_AGAMA,
              name=u'input_agama', parent=self, pos=wx.Point(400, 176),
              size=wx.Size(192, 25), style=0, value=u'')

        self.input_warga_negara = wx.TextCtrl(id=wxID_PENDUDUKINPUT_WARGA_NEGARA,
              name=u'input_warga_negara', parent=self, pos=wx.Point(400, 224),
              size=wx.Size(192, 25), style=0, value=u'')

        self.input_pendidikan_terakhir = wx.TextCtrl(id=wxID_PENDUDUKINPUT_PENDIDIKAN_TERAKHIR,
              name=u'input_pendidikan_terakhir', parent=self, pos=wx.Point(400,
              272), size=wx.Size(192, 25), style=0, value=u'')

        self.input_status = wx.TextCtrl(id=wxID_PENDUDUKINPUT_STATUS,
              name=u'input_status', parent=self, pos=wx.Point(400, 320),
              size=wx.Size(192, 25), style=0, value=u'')

        self.input_pekerjaan = wx.TextCtrl(id=wxID_PENDUDUKINPUT_PEKERJAAN,
              name=u'input_pekerjaan', parent=self, pos=wx.Point(400, 368),
              size=wx.Size(192, 25), style=0, value=u'')

        self.input_kependudukan = wx.TextCtrl(id=wxID_PENDUDUKINPUT_KEPENDUDUKAN,
              name=u'input_kependudukan', parent=self, pos=wx.Point(400, 416),
              size=wx.Size(192, 25), style=0, value=u'')

        self.input_gol_darah = wx.TextCtrl(id=wxID_PENDUDUKINPUT_GOL_DARAH,
              name=u'input_gol_darah', parent=self, pos=wx.Point(176, 416),
              size=wx.Size(200, 25), style=0, value=u'')

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON1, label=u'Cetak Bio Data ',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(640, 88),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON2,
              label=u'Kepemilikan Dokumen', name='genBitmapTextButton2',
              parent=self, pos=wx.Point(640, 128), size=wx.Size(240, 31),
              style=0)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON3,
              label=u'Pembuatan Surat Keterangan', name='genBitmapTextButton3',
              parent=self, pos=wx.Point(640, 168), size=wx.Size(240, 31),
              style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON4,
              label=u'Pembuatan Surat Perijinan', name='genBitmapTextButton4',
              parent=self, pos=wx.Point(640, 208), size=wx.Size(240, 31),
              style=0)

        self.genBitmapTextButton5 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON5, label=u'Pembuatan Surat ',
              name='genBitmapTextButton5', parent=self, pos=wx.Point(640, 248),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton6 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON6, label=u'Pembuatan Surat',
              name='genBitmapTextButton6', parent=self, pos=wx.Point(640, 288),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton7 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON7, label=u'Pembuatan Surat',
              name='genBitmapTextButton7', parent=self, pos=wx.Point(640, 328),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton8 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON8, label=u'Pembuatan Surat',
              name='genBitmapTextButton8', parent=self, pos=wx.Point(640, 368),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton9 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON9, label=u'Pembuatan Surat',
              name='genBitmapTextButton9', parent=self, pos=wx.Point(640, 408),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton10 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_PENDUDUKGENBITMAPTEXTBUTTON10, label=u'Pembuatan Surat',
              name='genBitmapTextButton10', parent=self, pos=wx.Point(640, 448),
              size=wx.Size(240, 31), style=0)

    def OnTombol_kembali_kemenuButton(self, event):
        event.Skip()
        
    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_kepemilikan_dokumenButton(self, event):
        event.Skip()
