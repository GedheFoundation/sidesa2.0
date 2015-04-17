#Boa:Frame:pecah_keluarga

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
    return pecah_keluarga(parent)

[wxID_PECAH_KELUARGA, wxID_PECAH_KELUARGABUTTON1, 
 wxID_PECAH_KELUARGACEK_AKTA_CERAI, wxID_PECAH_KELUARGACEK_AKTA_KEMATIAN, 
 wxID_PECAH_KELUARGACEK_AKTA_LAHIR, wxID_PECAH_KELUARGACEK_AKTA_NIKAH, 
 wxID_PECAH_KELUARGACEK_KITAS, wxID_PECAH_KELUARGACEK_KTP, 
 wxID_PECAH_KELUARGACEK_PASPORT, wxID_PECAH_KELUARGACEK_VISA, 
 wxID_PECAH_KELUARGADAFTAR, wxID_PECAH_KELUARGADOKUMEN, 
 wxID_PECAH_KELUARGAINPUT_ALAMAT, wxID_PECAH_KELUARGAINPUT_AYAH, 
 wxID_PECAH_KELUARGAINPUT_DUSUN, wxID_PECAH_KELUARGAINPUT_IBU, 
 wxID_PECAH_KELUARGAINPUT_NAMA, wxID_PECAH_KELUARGAINPUT_NIK, 
 wxID_PECAH_KELUARGAINPUT_NO_KK, wxID_PECAH_KELUARGAINPUT_TEMPAT_LAHIR, 
 wxID_PECAH_KELUARGAKEMBALI, wxID_PECAH_KELUARGALABEL_AGAMA, 
 wxID_PECAH_KELUARGALABEL_ALAMAT, wxID_PECAH_KELUARGALABEL_DATA_PENDUDUK, 
 wxID_PECAH_KELUARGALABEL_DIFABELITAS, wxID_PECAH_KELUARGALABEL_DUSUN, 
 wxID_PECAH_KELUARGALABEL_GOLONGAN_DARAH, 
 wxID_PECAH_KELUARGALABEL_JENIS_KELAMIN, 
 wxID_PECAH_KELUARGALABEL_KEWARGANEGARAAN, 
 wxID_PECAH_KELUARGALABEL_KONTRASEPSI, wxID_PECAH_KELUARGALABEL_NAMA_AYAH, 
 wxID_PECAH_KELUARGALABEL_NAMA_IBU, wxID_PECAH_KELUARGALABEL_NAMA_LENGKAP, 
 wxID_PECAH_KELUARGALABEL_NOMOR_KK, wxID_PECAH_KELUARGALABEL_PEKERJAAN, 
 wxID_PECAH_KELUARGALABEL_PEKERJAAN_LAINNYA, 
 wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TEMPUH, 
 wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TERAKHIR, 
 wxID_PECAH_KELUARGALABEL_RESIKO_KEHAMILAN, wxID_PECAH_KELUARGALABEL_SHDK, 
 wxID_PECAH_KELUARGALABEL_STATUS_KEPENDUDUKAN, 
 wxID_PECAH_KELUARGALABEL_STATUS_PERKAWINAN, 
 wxID_PECAH_KELUARGALABEL_STATUS_TINGGAL, 
 wxID_PECAH_KELUARGALABEL_TANGGAL_LAHIR, 
 wxID_PECAH_KELUARGALABEL_TEMPAT_LAHIR, wxID_PECAH_KELUARGALEBEL_NIK, 
 wxID_PECAH_KELUARGAPHOTO, wxID_PECAH_KELUARGAPILIHAN_AGAMA, 
 wxID_PECAH_KELUARGAPILIHAN_DIFABELITAS, 
 wxID_PECAH_KELUARGAPILIHAN_GOLONGAN_DARAH, 
 wxID_PECAH_KELUARGAPILIHAN_JENIS_KELAMIN, 
 wxID_PECAH_KELUARGAPILIHAN_KEHAMILAN, wxID_PECAH_KELUARGAPILIHAN_KONTRASEPSI, 
 wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN, 
 wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR, 
 wxID_PECAH_KELUARGAPILIHAN_SHDK, wxID_PECAH_KELUARGAPILIHAN_STATUS, 
 wxID_PECAH_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_PECAH_KELUARGAPILIHAN_STATUS_TINGGAL, 
 wxID_PECAH_KELUARGAPILIHAN_WARGANEGARA, wxID_PECAH_KELUARGAPILIHPHOTO, 
 wxID_PECAH_KELUARGASTATICTEXT1, wxID_PECAH_KELUARGATANGGAL_LAHIR, 
 wxID_PECAH_KELUARGATEXTCTRL1, wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA, 
 wxID_PECAH_KELUARGATOMBOL_TAMBAH_KEMBALI, 
] = [wx.NewId() for _init_ctrls in range(68)]

class pecah_keluarga(wx.Frame):
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
        wx.Frame.__init__(self, id=wxID_PECAH_KELUARGA, name=u'pecah_keluarga',
              parent=prnt, pos=wx.Point(269, 76), size=wx.Size(888, 639),
              style=wx.FRAME_NO_TASKBAR,
              title=u'Tambah Anggota Kartu Keluarga Tetap')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)

        self.label_nomor_kk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=0, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(272, 168),
              size=wx.Size(288, 25), style=0, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(592, 168),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_alamat = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(272, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DUSUN,
              label=u'Dusun - RT - RW', name=u'label_dusun', parent=self,
              pos=wx.Point(592, 152), size=wx.Size(144, 17), style=0)

        self.photo = wx.StaticBitmap(bitmap=wx.Bitmap('/opt/sidesa/png/photo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_PECAH_KELUARGAPHOTO, name=u'photo',
              parent=self, pos=wx.Point(16, 200), size=wx.Size(110, 140),
              style=0)

        self.pilihphoto = wx.FilePickerCtrl(id=wxID_PECAH_KELUARGAPILIHPHOTO,
              name=u'pilihphoto', parent=self, pos=wx.Point(16, 344),
              size=wx.Size(170, 30),
              style=wx.FLP_OPEN | wx.FLP_FILE_MUST_EXIST | wx.FLP_USE_TEXTCTRL)

        self.input_nik = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_PECAH_KELUARGALEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['Laki-laki',
              'Perempuan'], id=wxID_PECAH_KELUARGAPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=0)

        self.label_tempat_lahir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_PECAH_KELUARGAPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=0)

        self.label_agama = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_PECAH_KELUARGAPILIHAN_AGAMA, name=u'pilihan_agama',
              parent=self, pos=wx.Point(400, 208), size=wx.Size(216, 25),
              style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_PECAH_KELUARGAPILIHAN_WARGANEGARA,
              name=u'pilihan_warganegara', parent=self, pos=wx.Point(400, 248),
              size=wx.Size(216, 25), style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak / Belum Sekolah',
              'Tidak tamat SD / sederajat', 'Tamat SD / sederajat',
              'Tamat SLTP / sederajat', 'Tamat SLTA / sederajat',
              'Tamat Diploma I / II',
              'Tamat Akademi / Diploma III / Sarjana Muda',
              'Tamat D IV / Strata I', 'Tamat Strata II', 'Tamat Strata III',
              'Pendidikan Non Formal'],
              id=wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25), style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK sederajat', 'SD  sederajat', 'SLTP  sederajat',
              'SLTA  sederajat', 'D1  sederajat', 'D2  sederajat',
              'D3  sederajat' , 'S1 sederajat' , 'S2  sederajat' ,
              'S3  sederajat' , 'Pendidikan Non Formal'],
              id=wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25), style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.ComboBox(choices=['Belum / Tidak Bekerja',
              'Mengurus Rumah Tangga', 'Pelajar / Mahasiswa', 'Pensiunan',
              'Pegawai Negeri Sipil', 'Tentara Nasional Indonesia',
              'Kepolisian RI', 'Perdagangan', 'Petani / Pekebun', 'Peternak',
              'Nelayan / Perikanan', 'Industri', 'Konstruksi', 'Transportasi',
              'Karyawan Swasta', 'Karyawan BUMN', 'Karyawan BUMD',
              'Karyawan Honorer', 'Buruh Harian Lepas',
              'Buruh Tani / Perkebunan', 'Buruh Nelayan / Perikanan',
              'Buruh Peternakan', 'Pembantu Rumah Tangga', 'Tukang Cukur',
              'Tukang Listrik', 'Tukang Batu', 'Tukang Kayu',
              'Tukang Sol Sepatu', 'Tukang Las / Pandai Besi', 'Tukang Jahit',
              'Penata Rambut', 'Penata Rias', 'Penata Busana', 'Mekanik',
              'Tukang Gigi', 'Seniman', 'Tabib', 'Paraji', 'Perancang Busana',
              'Penterjemah', 'Imam Masjid', 'Pendeta', 'Pastur', 'Wartawan',
              'Ustadz / Mubaligh', 'Juru Masak', 'Promotor Acara',
              'Anggota DPR-RI', 'Anggota DPD', 'Anggota BPK', 'Presiden',
              'Wakil Presiden', 'Anggota Mahkamah Konstitusi',
              'Anggota Kabinet / Kementerian', 'Duta Besar', 'Gubernur',
              'Wakil Gubernur', 'Bupati', 'Wakil Bupati', 'Walikota',
              'Wakil Walikota', 'Anggota DPRD Propinsi',
              'Anggota DPRD Kabupaten / Kota', 'Dosen', 'Guru', 'Pilot',
              'Pengacara', 'Notaris', 'Arsitek', 'Akuntan', 'Konsultan',
              'Dokter', 'Bidan', 'Perawat', 'Apoteker', 'Psikiater / Psikolog',
              'Penyiar Televisi', 'Penyiar Radio', 'Pelaut', 'Peneliti',
              'Sopir', 'Pialang', 'Paranormal', 'Pedagang', 'Perangkat Desa',
              'Kepala Desa', 'Biarawati', 'Wiraswasta', 'Buruh Migran'],
              id=wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 25), style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin'],
              id=wxID_PECAH_KELUARGAPILIHAN_STATUS, name=u'pilihan_status',
              parent=self, pos=wx.Point(624, 208), size=wx.Size(248, 25),
              style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah / Pindahan', 'Meninggal'],
              id=wxID_PECAH_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25), style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal di Luar Desa*', 'Tinggal di Luar Kota / Kabupaten',
              'Tinggal di Luar Propinsi', 'Tinggal di Luar Negeri'],
              id=wxID_PECAH_KELUARGAPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=0)
        self.pilihan_status_tinggal.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_status_tinggalCombobox,
              id=wxID_PECAH_KELUARGAPILIHAN_STATUS_TINGGAL)

        self.label_difabelitas = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak cacat',
              'Cacat Fisik', 'Cacat Netra / Buta', 'Cacat Rungu / Wicara',
              'Cacat Mental / Jiwa', 'Cacat Fisik / Mental', 'Cacat Lainnya'],
              id=wxID_PECAH_KELUARGAPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 328),
              size=wx.Size(248, 25), style=0)
        self.pilihan_difabelitas.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_difabelitasCombobox,
              id=wxID_PECAH_KELUARGAPILIHAN_DIFABELITAS)

        self.label_kontrasepsi = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'],
              id=wxID_PECAH_KELUARGAPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=0)
        self.pilihan_kontrasepsi.Bind(wx.EVT_COMBOBOX,
              self.OnPilihan_kontrasepsiCombobox,
              id=wxID_PECAH_KELUARGAPILIHAN_KONTRASEPSI)

        self.label_shdk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.ComboBox(choices=['Kepala Keluarga', 'Anak',
              'Istri', 'Suami', 'Mertua', 'Menantu', 'Famili lain', 'Lainnya'],
              id=wxID_PECAH_KELUARGAPILIHAN_SHDK, name=u'pilihan_shdk',
              parent=self, pos=wx.Point(24, 560), size=wx.Size(304, 25),
              style=0)

        self.label_nama_ayah = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_PECAH_KELUARGAPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'], id=wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=0)

        self.tanggal_lahir = wx.DatePickerCtrl(id=wxID_PECAH_KELUARGATANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=wx.DP_SHOWCENTURY)

        self.tombol_tambah_data = wx.Button(id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(128, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA)

        self.tombol_tambah_kembali = wx.Button(id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_KEMBALI,
              label=u'Tambah Dan Keluar', name=u'tombol_tambah_kembali',
              parent=self, pos=wx.Point(344, 600), size=wx.Size(224, 32),
              style=0)
        self.tombol_tambah_kembali.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_kembaliButton,
              id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_KEMBALI)

        self.kembali = wx.Button(id=wxID_PECAH_KELUARGAKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(584, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_PECAH_KELUARGAKEMBALI)

        self.cek_akta_lahir = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_AKTA_LAHIR,
              label=u'Akta Kelahiran', name=u'cek_akta_lahir', parent=self,
              pos=wx.Point(16, 456), size=wx.Size(208, 24), style=0)
        self.cek_akta_lahir.SetValue(False)

        self.dokumen = wx.StaticText(id=wxID_PECAH_KELUARGADOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.cek_akta_nikah = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_AKTA_NIKAH,
              label=u'Akta Nikah', name=u'cek_akta_nikah', parent=self,
              pos=wx.Point(16, 472), size=wx.Size(160, 40), style=0)
        self.cek_akta_nikah.SetValue(False)

        self.cek_akta_cerai = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_AKTA_CERAI,
              label=u'Akta Cerai', name=u'cek_akta_cerai', parent=self,
              pos=wx.Point(16, 496), size=wx.Size(200, 32), style=0)
        self.cek_akta_cerai.SetValue(False)

        self.cek_akta_kematian = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_AKTA_KEMATIAN,
              label=u'Akta Kematian', name=u'cek_akta_kematian', parent=self,
              pos=wx.Point(152, 456), size=wx.Size(184, 24), style=0)
        self.cek_akta_kematian.SetValue(False)

        self.cek_ktp = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_KTP,
              label=u'KTP Sementara', name=u'cek_ktp', parent=self,
              pos=wx.Point(152, 480), size=wx.Size(128, 24), style=0)
        self.cek_ktp.SetValue(False)

        self.cek_kitas = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_KITAS,
              label=u'KITAS', name=u'cek_kitas', parent=self, pos=wx.Point(152,
              496), size=wx.Size(144, 32), style=0)
        self.cek_kitas.SetValue(False)

        self.cek_visa = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_VISA,
              label=u'Visa', name=u'cek_visa', parent=self, pos=wx.Point(288,
              448), size=wx.Size(200, 40), style=0)
        self.cek_visa.SetValue(False)

        self.cek_pasport = wx.CheckBox(id=wxID_PECAH_KELUARGACEK_PASPORT,
              label=u'Pasport', name=u'cek_pasport', parent=self,
              pos=wx.Point(288, 472), size=wx.Size(267, 40), style=0)
        self.cek_pasport.SetValue(False)

        self.label_data_penduduk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DATA_PENDUDUK,
              label=u'FORM DATA PENDUDUK', name=u'label_data_penduduk',
              parent=self, pos=wx.Point(336, 0), size=wx.Size(216, 17),
              style=0)

        self.daftar = wx.ListCtrl(id=wxID_PECAH_KELUARGADAFTAR, name=u'daftar',
              parent=self, pos=wx.Point(16, 16), size=wx.Size(856, 104),
              style=wx.LC_REPORT)
        self._init_coll_daftar_Columns(self.daftar)

        self.staticText1 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT1,
              label=u'Nomor Kartu Keluarga', name='staticText1', parent=self,
              pos=wx.Point(400, 128), size=wx.Size(145, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_PECAH_KELUARGATEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(552, 128),
              size=wx.Size(224, 24), style=0, value='')

        self.button1 = wx.Button(id=wxID_PECAH_KELUARGABUTTON1, label=u'Cari',
              name='button1', parent=self, pos=wx.Point(784, 128),
              size=wx.Size(85, 24), style=0)

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
