#Boa:Frame:sidesa

import wx
import wx.lib.buttons
import bantuan
import login_input_penduduk
import login_edit_kemiskinan
import login_edit_penduduk
import login_edit_profil
import login_edit_surat
import login_ekonomi
import login_indikator_kemiskinan
import login_input_kemiskinan
import login_input_profil
import login_input_surat
import login_inventaris_desa
import login_lahan
import login_pariwisata
import login_pecah_keluarga
import login_tambak
import cari_penduduk
import laporan_penduduk
import cari_kemiskinan
import laporan_kemiskinan
import cari_administrasi
import laporan_administrasi
import laporan_potensi
import laporan_profil
import laporan_statistik
import statistik_penduduk
import statistik_kemiskinan
import statistik_potensi
import statistik_administrasi
import sinkron_data
import kunci

def create(parent):
    return sidesa(parent)

[wxID_SIDESA, wxID_SIDESAGARIS_PROFIL, wxID_SIDESAKOTAK_ADMINISTRASI, 
 wxID_SIDESAKOTAK_KEMISKINAN, wxID_SIDESAKOTAK_MENU_UTAMA, 
 wxID_SIDESAKOTAK_POTENSI, wxID_SIDESAKOTAK_STATISTIK, 
 wxID_SIDESAKOTA_PENDUDUK, wxID_SIDESALABEL_PRAKARSA, wxID_SIDESALABEL_PROFIL, 
 wxID_SIDESALABEL_SIDEKA_ONLINE, wxID_SIDESASTATICBITMAP1, 
 wxID_SIDESATOMBOL_BANTUAN, wxID_SIDESATOMBOL_CARI_ADMINISTRASI, 
 wxID_SIDESATOMBOL_CARI_PENDUDUK, wxID_SIDESATOMBOL_EDIT_DATA_KEMISKINAN, 
 wxID_SIDESATOMBOL_EDIT_PENDUDUK, wxID_SIDESATOMBOL_EDIT_PROFIL, 
 wxID_SIDESATOMBOL_EDIT_SURAT, wxID_SIDESATOMBOL_EKONOMI, 
 wxID_SIDESATOMBOL_INPUT_PROFIL, wxID_SIDESATOMBOL_INVENTARIS_DESA, 
 wxID_SIDESATOMBOL_KELUAR, wxID_SIDESATOMBOL_KEPENDUDUKAN, 
 wxID_SIDESATOMBOL_LAHAN, wxID_SIDESATOMBOL_LAPORAN_ADMINISTRASI, 
 wxID_SIDESATOMBOL_LAPORAN_KEMISKINAN, wxID_SIDESATOMBOL_LAPORAN_PENDUDUK, 
 wxID_SIDESATOMBOL_LAPORAN_POTENSI, wxID_SIDESATOMBOL_LAPORAN_PROFIL, 
 wxID_SIDESATOMBOL_LAPORAN_STATISTIK, wxID_SIDESATOMBOL_PARIWISATA, 
 wxID_SIDESATOMBOL_PASSWORD, wxID_SIDESATOMBOL_PENCARIAN_KEMISKINAN, 
 wxID_SIDESATOMBOL_SINKRON, wxID_SIDESATOMBOL_STATISTIK_ADMINISTRASI, 
 wxID_SIDESATOMBOL_STATISTIK_KEMISKINAN, wxID_SIDESATOMBOL_STATISTIK_PENDUDUK, 
 wxID_SIDESATOMBOL_STATISTIK_POTENSI, wxID_SIDESATOMBOL_SURAT_MASUK, 
 wxID_SIDESATOMBOL_TAMBAH_DATA_KEMISKINAN, wxID_SIDESATOMBOL_TAMBAK, 
 wxID_SIDESATOMOBOL_INDIKATOR_KEMISKINAN, 
] = [wx.NewId() for _init_ctrls in range(43)]

class sidesa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SIDESA, name=u'sidesa', parent=prnt,
              pos=wx.Point(711, 69), size=wx.Size(647, 616),
              style=wx.FRAME_NO_TASKBAR, title=u'SIDESA 2.0 Versi 1.0')
        self.SetClientSize(wx.Size(647, 616))
        self.Center(wx.BOTH)

        self.kotak_menu_utama = wx.StaticBox(id=wxID_SIDESAKOTAK_MENU_UTAMA,
              label=u'MENU UTAMA', name=u'kotak_menu_utama', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(200, 235), style=0)

        self.kota_penduduk = wx.StaticBox(id=wxID_SIDESAKOTA_PENDUDUK,
              label=u'PENDUDUK', name=u'kota_penduduk', parent=self,
              pos=wx.Point(224, 88), size=wx.Size(200, 235), style=0)

        self.kotak_kemiskinan = wx.StaticBox(id=wxID_SIDESAKOTAK_KEMISKINAN,
              label=u'KEMISKINAN', name=u'kotak_kemiskinan', parent=self,
              pos=wx.Point(432, 88), size=wx.Size(200, 235), style=0)

        self.kotak_administrasi = wx.StaticBox(id=wxID_SIDESAKOTAK_ADMINISTRASI,
              label=u'ADMINISTRASI', name=u'kotak_administrasi', parent=self,
              pos=wx.Point(16, 328), size=wx.Size(200, 235), style=0)

        self.kotak_potensi = wx.StaticBox(id=wxID_SIDESAKOTAK_POTENSI,
              label=u'POTENSI DESA', name=u'kotak_potensi', parent=self,
              pos=wx.Point(224, 328), size=wx.Size(200, 235), style=0)

        self.tombol_kependudukan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/tambahdata.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_KEPENDUDUKAN,
              label=u'  Kependudukan', name=u'tombol_kependudukan', parent=self,
              pos=wx.Point(240, 112), size=wx.Size(168, 32), style=0)
        self.tombol_kependudukan.Bind(wx.EVT_BUTTON,
              self.OnTombol_kependudukanButton,
              id=wxID_SIDESATOMBOL_KEPENDUDUKAN)

        self.tombol_edit_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_EDIT_PENDUDUK,
              label=u' Edit Penduduk', name=u'tombol_edit_penduduk',
              parent=self, pos=wx.Point(240, 152), size=wx.Size(168, 32),
              style=0)
        self.tombol_edit_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_pendudukButton,
              id=wxID_SIDESATOMBOL_EDIT_PENDUDUK)

        self.tombol_cari_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_CARI_PENDUDUK,
              label=u'Lihat Data Penduduk', name=u'tombol_cari_penduduk',
              parent=self, pos=wx.Point(240, 192), size=wx.Size(168, 32),
              style=0)
        self.tombol_cari_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_cari_pendudukButton,
              id=wxID_SIDESATOMBOL_CARI_PENDUDUK)

        self.tombol_laporan_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_PENDUDUK,
              label=u' Laporan Penduduk', name=u'tombol_laporan_penduduk',
              parent=self, pos=wx.Point(240, 232), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_pendudukButton,
              id=wxID_SIDESATOMBOL_LAPORAN_PENDUDUK)

        self.tombol_tambah_data_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_TAMBAH_DATA_KEMISKINAN,
              label=u'  Tambah Data', name=u'tombol_tambah_data_kemiskinan',
              parent=self, pos=wx.Point(448, 112), size=wx.Size(168, 32),
              style=0)
        self.tombol_tambah_data_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_data_kemiskinanButton,
              id=wxID_SIDESATOMBOL_TAMBAH_DATA_KEMISKINAN)

        self.tomobol_indikator_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMOBOL_INDIKATOR_KEMISKINAN,
              label=u'  Indikator', name=u'tomobol_indikator_kemiskinan',
              parent=self, pos=wx.Point(448, 152), size=wx.Size(168, 32),
              style=0)
        self.tomobol_indikator_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTomobol_indikator_kemiskinanButton,
              id=wxID_SIDESATOMOBOL_INDIKATOR_KEMISKINAN)

        self.kotak_statistik = wx.StaticBox(id=wxID_SIDESAKOTAK_STATISTIK,
              label=u'STATISTIK', name=u'kotak_statistik', parent=self,
              pos=wx.Point(432, 328), size=wx.Size(200, 235), style=0)

        self.tombol_input_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/tambah_profil.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_INPUT_PROFIL,
              label=u'  Input Profil', name=u'tombol_input_profil', parent=self,
              pos=wx.Point(32, 192), size=wx.Size(168, 32), style=0)
        self.tombol_input_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_input_profilButton,
              id=wxID_SIDESATOMBOL_INPUT_PROFIL)

        self.tombol_edit_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_EDIT_PROFIL,
              label=u'  Edit Profil', name=u'tombol_edit_profil', parent=self,
              pos=wx.Point(32, 232), size=wx.Size(168, 32), style=0)
        self.tombol_edit_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_profilButton,
              id=wxID_SIDESATOMBOL_EDIT_PROFIL)

        self.tombol_sinkron = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/exportimport.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_SINKRON,
              label=u'Sinkron Data', name=u'tombol_sinkron', parent=self,
              pos=wx.Point(296, 40), size=wx.Size(168, 32), style=0)
        self.tombol_sinkron.Bind(wx.EVT_BUTTON, self.OnTombol_sinkronButton,
              id=wxID_SIDESATOMBOL_SINKRON)

        self.tombol_bantuan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/bantuan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_BANTUAN,
              label=u'  Bantuan', name=u'tombol_bantuan', parent=self,
              pos=wx.Point(472, 40), size=wx.Size(168, 32), style=0)
        self.tombol_bantuan.Bind(wx.EVT_BUTTON, self.OnTombol_bantuanButton,
              id=wxID_SIDESATOMBOL_BANTUAN)

        self.tombol_edit_data_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_EDIT_DATA_KEMISKINAN,
              label=u' Edit Data Kemiskinan',
              name=u'tombol_edit_data_kemiskinan', parent=self,
              pos=wx.Point(448, 192), size=wx.Size(168, 32), style=0)
        self.tombol_edit_data_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_data_kemiskinanButton,
              id=wxID_SIDESATOMBOL_EDIT_DATA_KEMISKINAN)

        self.tombol_pencarian_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_PENCARIAN_KEMISKINAN,
              label=u'Lihat Data Kemiskinan',
              name=u'tombol_pencarian_kemiskinan', parent=self,
              pos=wx.Point(448, 232), size=wx.Size(168, 32), style=0)
        self.tombol_pencarian_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_pencarian_kemiskinanButton,
              id=wxID_SIDESATOMBOL_PENCARIAN_KEMISKINAN)

        self.tombol_laporan_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_KEMISKINAN,
              label=u' Laporan Kemiskinan', name=u'tombol_laporan_kemiskinan',
              parent=self, pos=wx.Point(448, 272), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_kemiskinanButton,
              id=wxID_SIDESATOMBOL_LAPORAN_KEMISKINAN)

        self.tombol_surat_masuk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_SURAT_MASUK,
              label=u' Surat Masuk/Keluar', name=u'tombol_surat_masuk',
              parent=self, pos=wx.Point(32, 352), size=wx.Size(168, 32),
              style=0)
        self.tombol_surat_masuk.Bind(wx.EVT_BUTTON,
              self.OnTombol_surat_masukButton,
              id=wxID_SIDESATOMBOL_SURAT_MASUK)

        self.tombol_edit_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_EDIT_SURAT,
              label=u' Edit Data Surat', name=u'tombol_edit_surat', parent=self,
              pos=wx.Point(32, 392), size=wx.Size(168, 32), style=0)
        self.tombol_edit_surat.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_suratButton, id=wxID_SIDESATOMBOL_EDIT_SURAT)

        self.tombol_inventaris_desa = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_INVENTARIS_DESA,
              label=u' Inventaris Desa', name=u'tombol_inventaris_desa',
              parent=self, pos=wx.Point(32, 432), size=wx.Size(168, 32),
              style=0)
        self.tombol_inventaris_desa.Bind(wx.EVT_BUTTON,
              self.OnTombol_inventaris_desaButton,
              id=wxID_SIDESATOMBOL_INVENTARIS_DESA)

        self.tombol_cari_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_CARI_ADMINISTRASI,
              label=u'Lihat Data Adm', name=u'tombol_cari_administrasi',
              parent=self, pos=wx.Point(32, 472), size=wx.Size(168, 32),
              style=0)
        self.tombol_cari_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_cari_administrasiButton,
              id=wxID_SIDESATOMBOL_CARI_ADMINISTRASI)

        self.tombol_laporan_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_ADMINISTRASI,
              label=u'Laporan Administrasi',
              name=u'tombol_laporan_administrasi', parent=self, pos=wx.Point(32,
              512), size=wx.Size(168, 32), style=0)
        self.tombol_laporan_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_administrasiButton,
              id=wxID_SIDESATOMBOL_LAPORAN_ADMINISTRASI)

        self.label_sideka_online = wx.StaticText(id=wxID_SIDESALABEL_SIDEKA_ONLINE,
              label=u' SIDESA ONLINE :', name=u'label_sideka_online',
              parent=self, pos=wx.Point(304, 16), size=wx.Size(113, 17),
              style=0)

        self.tombol_password = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/security1.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_PASSWORD,
              label=u'  Password', name=u'tombol_password', parent=self,
              pos=wx.Point(32, 112), size=wx.Size(168, 32), style=0)
        self.tombol_password.Bind(wx.EVT_BUTTON, self.OnTombol_passwordButton,
              id=wxID_SIDESATOMBOL_PASSWORD)

        self.label_profil = wx.StaticText(id=wxID_SIDESALABEL_PROFIL,
              label=u'PROFIL DESA', name=u'label_profil', parent=self,
              pos=wx.Point(72, 168), size=wx.Size(84, 17), style=0)

        self.tombol_laporan_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_PROFIL,
              label=u' Laporan Profil', name=u'tombol_laporan_profil',
              parent=self, pos=wx.Point(32, 272), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_profilButton,
              id=wxID_SIDESATOMBOL_LAPORAN_PROFIL)

        self.tombol_ekonomi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/bantuan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_EKONOMI,
              label=u' Ekonomi SosBud', name=u'tombol_ekonomi', parent=self,
              pos=wx.Point(240, 352), size=wx.Size(168, 32), style=0)
        self.tombol_ekonomi.Bind(wx.EVT_BUTTON, self.OnTombol_ekonomiButton,
              id=wxID_SIDESATOMBOL_EKONOMI)

        self.garis_profil = wx.StaticLine(id=wxID_SIDESAGARIS_PROFIL,
              name=u'garis_profil', parent=self, pos=wx.Point(24, 152),
              size=wx.Size(184, 2), style=0)

        self.label_prakarsa = wx.StaticText(id=wxID_SIDESALABEL_PRAKARSA,
              label=u'Gerakan Desa Membangun', name=u'label_prakarsa',
              parent=self, pos=wx.Point(464, 592), size=wx.Size(192, 17),
              style=0)

        self.tombol_keluar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/keluar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_KELUAR,
              label=u'  Keluar Dari SIDESA 2.0', name=u'tombol_keluar',
              parent=self, pos=wx.Point(208, 576), size=wx.Size(240, 31),
              style=0)
        self.tombol_keluar.Bind(wx.EVT_BUTTON, self.OnTombol_keluarButton,
              id=wxID_SIDESATOMBOL_KELUAR)

        self.tombol_statistik_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/pen.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_STATISTIK_PENDUDUK,
              label=u' Statistik Penduduk', name=u'tombol_statistik_penduduk',
              parent=self, pos=wx.Point(448, 352), size=wx.Size(168, 31),
              style=0)
        self.tombol_statistik_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_pendudukButton,
              id=wxID_SIDESATOMBOL_STATISTIK_PENDUDUK)

        self.tombol_statistik_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/statistikmiskin.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_STATISTIK_KEMISKINAN,
              label=u' Statistik Kemiskinan',
              name=u'tombol_statistik_kemiskinan', parent=self,
              pos=wx.Point(448, 392), size=wx.Size(168, 31), style=0)
        self.tombol_statistik_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_kemiskinanButton,
              id=wxID_SIDESATOMBOL_STATISTIK_KEMISKINAN)

        self.tombol_statistik_potensi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/potensi.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_STATISTIK_POTENSI,
              label=u' Statistik Potensi', name=u'tombol_statistik_potensi',
              parent=self, pos=wx.Point(448, 432), size=wx.Size(168, 31),
              style=0)
        self.tombol_statistik_potensi.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_potensiButton,
              id=wxID_SIDESATOMBOL_STATISTIK_POTENSI)

        self.tombol_statistik_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/adm2.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_STATISTIK_ADMINISTRASI,
              label=u' Statistik Administrasi',
              name=u'tombol_statistik_administrasi', parent=self,
              pos=wx.Point(448, 472), size=wx.Size(168, 31), style=0)
        self.tombol_statistik_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_administrasiButton,
              id=wxID_SIDESATOMBOL_STATISTIK_ADMINISTRASI)

        self.tombol_laporan_statistik = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_STATISTIK,
              label=u'  Laporan', name=u'tombol_laporan_statistik', parent=self,
              pos=wx.Point(448, 512), size=wx.Size(168, 31), style=0)
        self.tombol_laporan_statistik.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_statistikButton,
              id=wxID_SIDESATOMBOL_LAPORAN_STATISTIK)

        self.tombol_lahan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/lahan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAHAN,
              label=u' Lahan & Sumber Air', name=u'tombol_lahan', parent=self,
              pos=wx.Point(240, 392), size=wx.Size(168, 31), style=0)
        self.tombol_lahan.Bind(wx.EVT_BUTTON, self.OnTombol_lahanButton,
              id=wxID_SIDESATOMBOL_LAHAN)

        self.tombol_tambak = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/tambak.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_TAMBAK,
              label=u' Tambak / Kolam Ikan', name=u'tombol_tambak', parent=self,
              pos=wx.Point(240, 432), size=wx.Size(168, 31), style=0)
        self.tombol_tambak.Bind(wx.EVT_BUTTON, self.OnTombol_tambakButton,
              id=wxID_SIDESATOMBOL_TAMBAK)

        self.tombol_pariwisata = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/pariwisata.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_PARIWISATA,
              label=u' Pariwisata', name=u'tombol_pariwisata', parent=self,
              pos=wx.Point(240, 472), size=wx.Size(168, 31), style=0)
        self.tombol_pariwisata.Bind(wx.EVT_BUTTON,
              self.OnTombol_pariwisataButton, id=wxID_SIDESATOMBOL_PARIWISATA)

        self.tombol_laporan_potensi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('/opt/sidesa/png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESATOMBOL_LAPORAN_POTENSI,
              label=u' Laporan Potensi', name=u'tombol_laporan_potensi',
              parent=self, pos=wx.Point(240, 512), size=wx.Size(168, 31),
              style=0)
        self.tombol_laporan_potensi.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_potensiButton,
              id=wxID_SIDESATOMBOL_LAPORAN_POTENSI)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('/opt/sidesa/png/logo3.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDESASTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(584, 392), style=0)
        self.staticBitmap1.SetAutoLayout(False)

    def __init__(self, parent):
                self._init_ctrls(parent)
                
    def OnTombol_bantuanButton(self, event):
        self.main=bantuan.create(None)
        self.main.Show()

    def OnTombol_input_profilButton(self, event):
        self.main=login_input_profil.create(None)
        self.main.Show()
        
    def OnTombol_edit_profilButton(self, event):
        self.main=login_edit_profil.create(None)
        self.main.Show()
        
    def OnTombol_laporan_profilButton(self, event):
        self.main=laporan_profil.create(None)
        self.main.Show()
        
    def OnTombol_kependudukanButton(self, event):
        self.main=login_input_penduduk.create(None)
        self.main.Show()
        
    def OnTombol_pecah_keluargaButton(self, event):
        self.main=login_pecah_keluarga.create(None)
        self.main.Show()
        
    def OnTombol_edit_pendudukButton(self, event):
        self.main=login_edit_penduduk.create(None)
        self.main.Show()
        
    def OnTombol_cari_pendudukButton(self, event):
        self.main=cari_penduduk.create(None)
        self.main.Show()
        
    def OnTombol_laporan_pendudukButton(self, event):
        self.main=laporan_penduduk.create(None)
        self.main.Show()
        
    def OnTombol_tambah_data_kemiskinanButton(self, event):
        self.main=login_input_kemiskinan.create(None)
        self.main.Show()
        
    def OnTomobol_indikator_kemiskinanButton(self, event):
        self.main=login_indikator_kemiskinan.create(None)
        self.main.Show()
        
    def OnTombol_edit_data_kemiskinanButton(self, event):
        self.main=login_edit_kemiskinan.create(None)
        self.main.Show()
        
    def OnTombol_pencarian_kemiskinanButton(self, event):
        self.main=cari_kemiskinan.create(None)
        self.main.Show()
        
    def OnTombol_laporan_kemiskinanButton(self, event):
        self.main=laporan_kemiskinan.create(None)
        self.main.Show()
        
    def OnTombol_surat_masukButton(self, event):
        self.main=login_input_surat.create(None)
        self.main.Show()
        
    def OnTombol_edit_suratButton(self, event):
        self.main=login_edit_surat.create(None)
        self.main.Show()
        
    def OnTombol_inventaris_desaButton(self, event):
        self.main=login_inventaris_desa.create(None)
        self.main.Show()
        
    def OnTombol_cari_administrasiButton(self, event):
        self.main=cari_administrasi.create(None)
        self.main.Show()
        
    def OnTombol_laporan_administrasiButton(self, event):
        self.main=laporan_administrasi.create(None)
        self.main.Show()
        
    def OnTombol_ekonomiButton(self, event):
        self.main=login_ekonomi.create(None)
        self.main.Show()
        
    def OnTombol_lahanButton(self, event):
        self.main=login_lahan.create(None)
        self.main.Show()
        
    def OnTombol_tambakButton(self, event):
        self.main=login_tambak.create(None)
        self.main.Show()
        
    def OnTombol_pariwisataButton(self, event):
        self.main=login_pariwisata.create(None)
        self.main.Show()
        
    def OnTombol_laporan_potensiButton(self, event):
        self.main=laporan_potensi.create(None)
        self.main.Show()
        
    def OnTombol_statistik_pendudukButton(self, event):
        self.main=statistik_penduduk.create(None)
        self.main.Show()
        
    def OnTombol_statistik_kemiskinanButton(self, event):
        self.main=statistik_kemiskinan.create(None)
        self.main.Show()
        
    def OnTombol_statistik_potensiButton(self, event):
        self.main=statistik_potensi.create(None)
        self.main.Show()
        
    def OnTombol_statistik_administrasiButton(self, event):
        self.main=statistik_administrasi.create(None)
        self.main.Show()
        
    def OnTombol_laporan_statistikButton(self, event):
        self.main=laporan_statistik.create(None)
        self.main.Show()
        
    def OnTombol_keluarButton(self, event):
        self.Close()
        self.Destroy()  

    def OnTombol_sinkronButton(self, event):
        self.main=sinkron_data.create(None)
        self.main.Show()

    def OnTombol_passwordButton(self, event):
        self.main=kunci.create(None)
        self.main.Show()
        
