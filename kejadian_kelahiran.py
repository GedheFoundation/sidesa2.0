#Boa:Frame:kejadian_kelahiran


import os
import wx
import wx.lib.buttons
import data_penduduk
import sqlite3
import string
import gettext

def connect():
    db = sqlite3.connect('sidesa')
    return db
    db.close()

def create(parent):
    return kejadian_kelahiran(parent)

[wxID_KEJADIAN_KELAHIRAN, wxID_KEJADIAN_KELAHIRANBUTTON1, 
 wxID_KEJADIAN_KELAHIRANCEK_AKTA_CERAI, 
 wxID_KEJADIAN_KELAHIRANCEK_AKTA_KEMATIAN, 
 wxID_KEJADIAN_KELAHIRANCEK_AKTA_LAHIR, wxID_KEJADIAN_KELAHIRANCEK_AKTA_NIKAH, 
 wxID_KEJADIAN_KELAHIRANCEK_KITAS, wxID_KEJADIAN_KELAHIRANCEK_KTP, 
 wxID_KEJADIAN_KELAHIRANCEK_PASPORT, wxID_KEJADIAN_KELAHIRANCEK_VISA, 
 wxID_KEJADIAN_KELAHIRANDAFTAR, wxID_KEJADIAN_KELAHIRANDATEPICKERCTRL1, 
 wxID_KEJADIAN_KELAHIRANDOKUMEN, wxID_KEJADIAN_KELAHIRANINPUT_ALAMAT, 
 wxID_KEJADIAN_KELAHIRANINPUT_AYAH, wxID_KEJADIAN_KELAHIRANINPUT_DUSUN, 
 wxID_KEJADIAN_KELAHIRANINPUT_IBU, wxID_KEJADIAN_KELAHIRANINPUT_NAMA, 
 wxID_KEJADIAN_KELAHIRANINPUT_NIK, wxID_KEJADIAN_KELAHIRANINPUT_NO_KK, 
 wxID_KEJADIAN_KELAHIRANINPUT_TEMPAT_LAHIR, 
 wxID_KEJADIAN_KELAHIRANKEJADIAN_KELAHIRAN, wxID_KEJADIAN_KELAHIRANKEMBALI, 
 wxID_KEJADIAN_KELAHIRANLABEL_AGAMA, wxID_KEJADIAN_KELAHIRANLABEL_ALAMAT, 
 wxID_KEJADIAN_KELAHIRANLABEL_DATA_PENDUDUK, 
 wxID_KEJADIAN_KELAHIRANLABEL_DIFABELITAS, wxID_KEJADIAN_KELAHIRANLABEL_DUSUN, 
 wxID_KEJADIAN_KELAHIRANLABEL_GOLONGAN_DARAH, 
 wxID_KEJADIAN_KELAHIRANLABEL_JENIS_KELAMIN, 
 wxID_KEJADIAN_KELAHIRANLABEL_KEWARGANEGARAAN, 
 wxID_KEJADIAN_KELAHIRANLABEL_KONTRASEPSI, 
 wxID_KEJADIAN_KELAHIRANLABEL_NAMA_AYAH, 
 wxID_KEJADIAN_KELAHIRANLABEL_NAMA_IBU, 
 wxID_KEJADIAN_KELAHIRANLABEL_NAMA_LENGKAP, 
 wxID_KEJADIAN_KELAHIRANLABEL_NOMOR_KK, 
 wxID_KEJADIAN_KELAHIRANLABEL_PEKERJAAN, 
 wxID_KEJADIAN_KELAHIRANLABEL_PEKERJAAN_LAINNYA, 
 wxID_KEJADIAN_KELAHIRANLABEL_PENDIDIKAN_TEMPUH, 
 wxID_KEJADIAN_KELAHIRANLABEL_PENDIDIKAN_TERAKHIR, 
 wxID_KEJADIAN_KELAHIRANLABEL_RESIKO_KEHAMILAN, 
 wxID_KEJADIAN_KELAHIRANLABEL_SHDK, 
 wxID_KEJADIAN_KELAHIRANLABEL_STATUS_KEPENDUDUKAN, 
 wxID_KEJADIAN_KELAHIRANLABEL_STATUS_PERKAWINAN, 
 wxID_KEJADIAN_KELAHIRANLABEL_STATUS_TINGGAL, 
 wxID_KEJADIAN_KELAHIRANLABEL_TANGGAL_LAHIR, 
 wxID_KEJADIAN_KELAHIRANLABEL_TEMPAT_LAHIR, wxID_KEJADIAN_KELAHIRANLEBEL_NIK, 
 wxID_KEJADIAN_KELAHIRANPETUGAS_KEMATIAN, wxID_KEJADIAN_KELAHIRANPHOTO, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_AGAMA, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_DIFABELITAS, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_GOLONGAN_DARAH, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_JENIS_KELAMIN, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_KEHAMILAN, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_KONTRASEPSI, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_PEKERJAAN, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_PENDIDIKAN_TERAKHIR, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_SHDK, wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS_TINGGAL, 
 wxID_KEJADIAN_KELAHIRANPILIHAN_WARGANEGARA, 
 wxID_KEJADIAN_KELAHIRANPILIHPHOTO, wxID_KEJADIAN_KELAHIRANSTATICTEXT1, 
 wxID_KEJADIAN_KELAHIRANSTATICTEXT2, wxID_KEJADIAN_KELAHIRANSTATICTEXT3, 
 wxID_KEJADIAN_KELAHIRANSTATICTEXT4, wxID_KEJADIAN_KELAHIRANTANGGAL_LAHIR, 
 wxID_KEJADIAN_KELAHIRANTEXTCTRL1, wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_DATA, 
 wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_KEMBALI, 
] = [wx.NewId() for _init_ctrls in range(74)]

class kejadian_kelahiran(wx.Frame):
    def _init_coll_daftar_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Kepala Keluarga', width=160)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_KEJADIAN_KELAHIRAN,
              name=u'kejadian_kelahiran', parent=prnt, pos=wx.Point(300, 64),
              size=wx.Size(888, 639), style=wx.FRAME_NO_TASKBAR,
              title=u'Peristiwa Kelahiran Penduduk')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)

        self.label_nomor_kk = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=0, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(272, 168),
              size=wx.Size(288, 25), style=0, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(592, 168),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_alamat = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(272, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_DUSUN,
              label=u'Dusun - RT - RW', name=u'label_dusun', parent=self,
              pos=wx.Point(592, 152), size=wx.Size(144, 17), style=0)

        self.photo = wx.StaticBitmap(bitmap=wx.Bitmap('/opt/sidesa/png/photo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_KEJADIAN_KELAHIRANPHOTO,
              name=u'photo', parent=self, pos=wx.Point(16, 200),
              size=wx.Size(110, 140), style=0)

        self.pilihphoto = wx.FilePickerCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHPHOTO,
              name=u'pilihphoto', parent=self, pos=wx.Point(16, 344),
              size=wx.Size(170, 30),
              style=wx.FLP_OPEN | wx.FLP_FILE_MUST_EXIST | wx.FLP_USE_TEXTCTRL)

        self.input_nik = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.pilihan_jenis_kelamin = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=0, value=u'')

        self.label_tempat_lahir = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.pilihan_golongan_darah = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=0, value=u'')

        self.label_agama = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.pilihan_agama = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_AGAMA,
              name=u'pilihan_agama', parent=self, pos=wx.Point(400, 208),
              size=wx.Size(216, 25), style=0, value=u'')

        self.label_kewarganegaraan = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_WARGANEGARA,
              name=u'pilihan_warganegara', parent=self, pos=wx.Point(400, 248),
              size=wx.Size(216, 25), style=0, value=u'')

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25), style=0,
              value=u'')

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25), style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 25), style=0, value=u'')

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 208),
              size=wx.Size(248, 25), style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25), style=0,
              value=u'')

        self.label_status_tinggal = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=0, value=u'')
        self.pilihan_status_tinggal.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_status_tinggalCombobox,
              id=wxID_KEJADIAN_KELAHIRANPILIHAN_STATUS_TINGGAL)

        self.label_difabelitas = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 328),
              size=wx.Size(248, 25), style=0, value=u'')
        self.pilihan_difabelitas.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_difabelitasCombobox,
              id=wxID_KEJADIAN_KELAHIRANPILIHAN_DIFABELITAS)

        self.label_kontrasepsi = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=0, value=u'')
        self.pilihan_kontrasepsi.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_kontrasepsiCombobox,
              id=wxID_KEJADIAN_KELAHIRANPILIHAN_KONTRASEPSI)

        self.label_shdk = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_SHDK,
              name=u'pilihan_shdk', parent=self, pos=wx.Point(24, 560),
              size=wx.Size(304, 25), style=0, value=u'')

        self.label_nama_ayah = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.pilihan_kehamilan = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=0, value=u'')

        self.pilihan_pekerjaan_lainnya = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=0, value=u'')

        self.tanggal_lahir = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANTANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=0, value=u'')

        self.tombol_tambah_data = wx.Button(id=wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(128, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_DATA)

        self.tombol_tambah_kembali = wx.Button(id=wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_KEMBALI,
              label=u'Tambah Dan Keluar', name=u'tombol_tambah_kembali',
              parent=self, pos=wx.Point(344, 600), size=wx.Size(224, 32),
              style=0)
        self.tombol_tambah_kembali.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_kembaliButton,
              id=wxID_KEJADIAN_KELAHIRANTOMBOL_TAMBAH_KEMBALI)

        self.kembali = wx.Button(id=wxID_KEJADIAN_KELAHIRANKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(584, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_KEJADIAN_KELAHIRANKEMBALI)

        self.cek_akta_lahir = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_AKTA_LAHIR,
              label=u'Akta Kelahiran', name=u'cek_akta_lahir', parent=self,
              pos=wx.Point(16, 456), size=wx.Size(208, 24), style=0)
        self.cek_akta_lahir.SetValue(False)

        self.dokumen = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANDOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.cek_akta_nikah = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_AKTA_NIKAH,
              label=u'Akta Nikah', name=u'cek_akta_nikah', parent=self,
              pos=wx.Point(16, 472), size=wx.Size(160, 40), style=0)
        self.cek_akta_nikah.SetValue(False)

        self.cek_akta_cerai = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_AKTA_CERAI,
              label=u'Akta Cerai', name=u'cek_akta_cerai', parent=self,
              pos=wx.Point(16, 496), size=wx.Size(200, 32), style=0)
        self.cek_akta_cerai.SetValue(False)

        self.cek_akta_kematian = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_AKTA_KEMATIAN,
              label=u'Akta Kematian', name=u'cek_akta_kematian', parent=self,
              pos=wx.Point(152, 456), size=wx.Size(184, 24), style=0)
        self.cek_akta_kematian.SetValue(False)

        self.cek_ktp = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_KTP,
              label=u'KTP Sementara', name=u'cek_ktp', parent=self,
              pos=wx.Point(152, 480), size=wx.Size(128, 24), style=0)
        self.cek_ktp.SetValue(False)

        self.cek_kitas = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_KITAS,
              label=u'KITAS', name=u'cek_kitas', parent=self, pos=wx.Point(152,
              496), size=wx.Size(144, 32), style=0)
        self.cek_kitas.SetValue(False)

        self.cek_visa = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_VISA,
              label=u'Visa', name=u'cek_visa', parent=self, pos=wx.Point(288,
              448), size=wx.Size(100, 40), style=0)
        self.cek_visa.SetValue(False)

        self.cek_pasport = wx.CheckBox(id=wxID_KEJADIAN_KELAHIRANCEK_PASPORT,
              label=u'Pasport', name=u'cek_pasport', parent=self,
              pos=wx.Point(288, 472), size=wx.Size(100, 40), style=0)
        self.cek_pasport.SetValue(False)

        self.label_data_penduduk = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANLABEL_DATA_PENDUDUK,
              label=u'FORM DATA PERISTIWA KELAHIRAN PENDUDUK',
              name=u'label_data_penduduk', parent=self, pos=wx.Point(288, 0),
              size=wx.Size(307, 17), style=0)

        self.daftar = wx.ListCtrl(id=wxID_KEJADIAN_KELAHIRANDAFTAR,
              name=u'daftar', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 104), style=wx.LC_REPORT)
        self._init_coll_daftar_Columns(self.daftar)

        self.staticText1 = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANSTATICTEXT1,
              label=u'Nama Kepala Keluarga', name='staticText1', parent=self,
              pos=wx.Point(400, 128), size=wx.Size(149, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(552, 128),
              size=wx.Size(224, 24), style=0, value='')

        self.button1 = wx.Button(id=wxID_KEJADIAN_KELAHIRANBUTTON1,
              label=u'Cari', name='button1', parent=self, pos=wx.Point(784,
              128), size=wx.Size(85, 24), style=0)

        self.staticText2 = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANSTATICTEXT2,
              label=u'Tanggal Kelahiran', name='staticText2', parent=self,
              pos=wx.Point(400, 448), size=wx.Size(117, 15), style=0)

        self.staticText3 = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANSTATICTEXT3,
              label=u'Petugas Kelahiran', name='staticText3', parent=self,
              pos=wx.Point(400, 472), size=wx.Size(208, 15), style=0)

        self.staticText4 = wx.StaticText(id=wxID_KEJADIAN_KELAHIRANSTATICTEXT4,
              label=u'Catatan Kelahiran', name='staticText4', parent=self,
              pos=wx.Point(400, 504), size=wx.Size(123, 15), style=0)

        self.petugas_kematian = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANPETUGAS_KEMATIAN,
              name=u'petugas_kematian', parent=self, pos=wx.Point(592, 472),
              size=wx.Size(264, 24), style=0, value='')

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_KEJADIAN_KELAHIRANDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(592, 440),
              size=wx.Size(264, 24), style=wx.DP_SHOWCENTURY)

        self.kejadian_kelahiran = wx.TextCtrl(id=wxID_KEJADIAN_KELAHIRANKEJADIAN_KELAHIRAN,
              name=u'kejadian_kelahiran', parent=self, pos=wx.Point(592, 504),
              size=wx.Size(264, 24), style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
      
        
    def OnTombol_kembali_kemenuButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_kepemilikan_dokumenButton(self, event):
        event.Skip()
  
    def OnTombol_tambah_dataButton(self, event):
        inputnokk = str(self.input_no_kk.GetValue())
        inputnik = str(self.input_nik.GetValue())
        inputnama = str(self.input_nama.GetValue())
        inputtempatlahir = str(self.input_tempat_lahir.GetValue())
        pilihanjeniskelamin = str(self.pilihan_jenis_kelamin.GetValue())
        tanggallahir = str(self.tanggal_lahir.GetValue())
        pilihangolongandarah = str(self.pilihan_golongan_darah.GetValue())
        pilihanagama = str(self.pilihan_agama.GetValue())
        pilihanwarganegara = str(self.pilihan_warganegara.GetValue())
        pilihanpendidikanterakhir = str(self.pilihan_pendidikan_terakhir.GetValue())
        pilihanpendidikanditempuh = str(self.pilihan_pendidikan_ditempuh.GetValue())
        pilihanpekerjaan = str(self.pilihan_pekerjaan.GetValue())
        pilihanpekerjaanlainnya = str(self.pilihan_pekerjaan_lainnya.GetValue())
        pilihanstatus = str(self.pilihan_status.GetValue())
        pilihanstatuskependudukan = str(self.pilihan_status_kependudukan.GetValue())
        pilihanstatustinggal = str(self.pilihan_status_tinggal.GetValue())
        pilihandifabelitas = str(self.pilihan_difabelitas.GetValue())
        pilihankontrasepsi = str(self.pilihan_kontrasepsi.GetValue())
        pilihanshdk = str(self.pilihan_shdk.GetValue())
        inputayah = str(self.input_ayah.GetValue())
        inputibu = str(self.input_ibu.GetValue())
        pilihankehamilan = str(self.pilihan_kehamilan.GetValue())
        inputalamat = str(self.input_alamat.GetValue())
        inputdusun = str(self.input_dusun.GetValue())
        db = connect()
        cursor = db.cursor()
        add_keluarga="INSERT INTO penduduk (no_kk, no_nik, nama_lengkap, jenis_kelamin, tempat_lahir, tanggal_lahir, gol_darah, agama, warganegara, pendidikan_akhir, pendidikan_saat_ini, pekerjaan_utama, pekerjaan_lain, status_kawin, status_kependudukan, status_tinggal, difabelitas, kontrasepsi, kehamilan, shdk, nama_ayah, nama_ibu, alamat, nama_dusun) VALUES('"+(inputnokk)+"', '"+(inputnik)+"', '"+(inputnama)+"', '"+(pilihanjeniskelamin)+"', '"+(inputtempatlahir)+"', '"+(tanggallahir)+"', '"+(pilihangolongandarah)+"', '"+(pilihanagama)+"', '"+(pilihanwarganegara)+"', '"+(pilihanpendidikanterakhir)+"', '"+(pilihanpendidikanditempuh)+"', '"+(pilihanpekerjaan)+"', '"+(pilihanpekerjaanlainnya)+"', '"+(pilihanstatus)+"', '"+(pilihanstatuskependudukan)+"', '"+(pilihanstatustinggal)+"', '"+(pilihandifabelitas)+"', '"+(pilihankontrasepsi)+"', '"+(pilihankehamilan)+"', '"+(pilihanshdk)+"', '"+(inputayah)+"', '"+(inputibu)+"', '"+(inputalamat)+"', '"+(inputdusun)+"')"
        cursor.execute(add_keluarga)
        db.commit()
        self.input_no_kk.Clear()
        self.input_alamat.Clear()
        self.input_dusun.Clear()
        self.input_nik.Clear()
        self.input_nama.Clear()
        self.pilihan_jenis_kelamin.Bind(wx.EVT_COMBOBOX, on_select)
        self.input_tempat_lahir.Clear()
        #self.tanggal_lahir.Clear()
        self.pilihan_golongan_darah()
        self.pilihan_agama()
        self.pilihan_warganegara.Clear()
        self.pilihan_pendidikan_terakhir.Clear()
        self.pilihan_pendidikan_ditempuh.Clear()
        self.pilihan_pekerjaan.Clear()
        self.pilihan_pekerjaan_lainnya.Clear()
        self.pilihan_status.Clear()
        self.pilihan_status_kependudukan.Clear()
        self.pilihan_status_tinggal.Clear()
        self.pilihan_difabelitas.Clear()
        self.pilihan_kontrasepsi.Clear()
        self.pilihan_kehamilan.Clear()
        self.pilihan_shdk.Clear()
        self.input_ayah.Clear()
        self.input_ibu.Clear()
        
        
       
        
        db.close()
        
    def OnTombol_tambah_kembaliButton(self, event):
        inputnokk = str(self.input_no_kk.GetValue())
        inputalamat = str(self.input_alamat.GetValue())
        inputdusun = str(self.input_dusun.GetValue())
        inputnik = str(self.input_nik.GetValue())
        inputnama = str(self.input_nama.GetValue())
        inputtempatlahir = str(self.input_tempat_lahir.GetValue())
        pilihanjeniskelamin = str(self.pilihan_jenis_kelamin.GetCurrentSelection())
        tanggallahir = str(self.tanggal_lahir.GetValue())
        pilihangolongandarah = str(self.pilihan_golongan_darah.GetCurrentSelection())
        pilihanagama = str(self.pilihan_agama.GetCurrentSelection())
        pilihanwarganegara = str(self.pilihan_warganegara.GetCurrentSelection())
        pilihanpendidikanterakhir = str(self.pilihan_pendidikan_terakhir.GetCurrentSelection())
        pilihanpendidikanditempuh = str(self.pilihan_pendidikan_ditempuh.GetCurrentSelection())
        pilihanpekerjaan = str(self.pilihan_pekerjaan.GetCurrentSelection())
        pilihanpekerjaanlainnya = str(self.pilihan_pekerjaan_lainnya.GetCurrentSelection())
        pilihanstatus = str(self.pilihan_status.GetCurrentSelection())
        pilihanstatuskependudukan = str(self.pilihan_status_kependudukan.GetCurrentSelection())
        pilihanstatustinggal = str(self.pilihan_status_tinggal.GetCurrentSelection())
        pilihandifabelitas = str(self.pilihan_difabelitas.GetCurrentSelection())
        pilihankontrasepsi = str(self.pilihan_kontrasepsi.GetCurrentSelection())
        pilihanshdk = str(self.pilihan_shdk.GetCurrentSelection())
        inputayah = str(self.input_ayah.GetValue())
        inputibu = str(self.input_ibu.GetValue())
        pilihankehamilan = str(self.pilihan_kehamilan.GetCurrentSelection())
        db = connect()
        cursor = db.cursor()
        add_keluarga="INSERT INTO penduduk (no_kk, no_nik, nama_lengkap, jenis_kelamin, tempat_lahir, tanggal_lahir, gol_darah, agama, warganegara, pendidikan_akhir, pendidikan_saat_ini, pekerjaan_utama, pekerjaan_lain, status_kawin, status_kependudukan, status_tinggal, difabelitas, kontrasepsi, kehamilan, shdk, nama_ayah, nama_ibu, alamat, nama_dusun) VALUES('"+(inputnokk)+"', '"+(inputnik)+"', '"+(inputnama)+"', '"+(pilihanjeniskelamin)+"', '"+(inputtempatlahir)+"', '"+(tanggallahir)+"', '"+(pilihangolongandarah)+"', '"+(pilihanagama)+"', '"+(pilihanwarganegara)+"', '"+(pilihanpendidikanterakhir)+"', '"+(pilihanpendidikanditempuh)+"', '"+(pilihanpekerjaan)+"', '"+(pilihanpekerjaanlainnya)+"', '"+(pilihanstatus)+"', '"+(pilihanstatuskependudukan)+"', '"+(pilihanstatustinggal)+"', '"+(pilihandifabelitas)+"', '"+(pilihankontrasepsi)+"', '"+(pilihankehamilan)+"', '"+(pilihanshdk)+"', '"+(inputayah)+"', '"+(inputibu)+"', '"+(inputalamat)+"', '"+(inputdusun)+"')"
        cursor.execute(add_keluarga)
        db.commit()
        self.Close()

    def OnKembaliButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnPilihan_status_tinggalCombobox(self, event):
        event.Skip()

    def OnPilihan_difabelitasCombobox(self, event):
        event.Skip()

    def OnPilihan_kontrasepsiCombobox(self, event):
        event.Skip()
