#Boa:Frame:pembuatan_surat_keluar

import wx
import input_administrasi_surat
import sqlite3
from subprocess import call
from pyPdf import PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return pembuatan_surat_keluar(parent)

[wxID_PEMBUATAN_SURAT_KELUAR, wxID_PEMBUATAN_SURAT_KELUARAGAMA, 
 wxID_PEMBUATAN_SURAT_KELUARALAMAT, wxID_PEMBUATAN_SURAT_KELUARALAMAT_KANTOR, 
 wxID_PEMBUATAN_SURAT_KELUARBUTTON1, wxID_PEMBUATAN_SURAT_KELUARBUTTON2, 
 wxID_PEMBUATAN_SURAT_KELUARBUTTON3, wxID_PEMBUATAN_SURAT_KELUARCARI_PENDUDUK, 
 wxID_PEMBUATAN_SURAT_KELUARCOMBOBOX1, 
 wxID_PEMBUATAN_SURAT_KELUARDATEPICKERCTRL1, 
 wxID_PEMBUATAN_SURAT_KELUARDIFABELITAS, wxID_PEMBUATAN_SURAT_KELUAREMAIL, 
 wxID_PEMBUATAN_SURAT_KELUARGOL_DARAH, 
 wxID_PEMBUATAN_SURAT_KELUARJENIS_KELAMIN, 
 wxID_PEMBUATAN_SURAT_KELUARKEHAMILAN, wxID_PEMBUATAN_SURAT_KELUARKEMATIAN, 
 wxID_PEMBUATAN_SURAT_KELUARKEMISKINAN, 
 wxID_PEMBUATAN_SURAT_KELUARKONTRASEPSI, 
 wxID_PEMBUATAN_SURAT_KELUARLIST_SURAT, wxID_PEMBUATAN_SURAT_KELUARNAMA_AYAH, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_DESA, wxID_PEMBUATAN_SURAT_KELUARNAMA_DUSUN, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_IBU, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_KABUPATEN, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_KADES, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_KECAMATAN, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_LENGKAP, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_PROPINSI, 
 wxID_PEMBUATAN_SURAT_KELUARNAMA_SEKDES, 
 wxID_PEMBUATAN_SURAT_KELUARNEGARAKERJA, wxID_PEMBUATAN_SURAT_KELUARNO_KK, 
 wxID_PEMBUATAN_SURAT_KELUARNO_NIK, wxID_PEMBUATAN_SURAT_KELUARNO_SURAT, 
 wxID_PEMBUATAN_SURAT_KELUARNO_TELP, 
 wxID_PEMBUATAN_SURAT_KELUARPEKERJAAN_LAIN, 
 wxID_PEMBUATAN_SURAT_KELUARPEKERJAAN_UTAMA, 
 wxID_PEMBUATAN_SURAT_KELUARPENDIDIKAN_AKHIR, 
 wxID_PEMBUATAN_SURAT_KELUARPENDIDIKAN_SAAT_INI, 
 wxID_PEMBUATAN_SURAT_KELUARPENDUDUK, 
 wxID_PEMBUATAN_SURAT_KELUARPERUSAHAANKERJA, 
 wxID_PEMBUATAN_SURAT_KELUARPINDAHKERJA, wxID_PEMBUATAN_SURAT_KELUARRT, 
 wxID_PEMBUATAN_SURAT_KELUARRW, wxID_PEMBUATAN_SURAT_KELUARSHDK, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT1, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT2, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT3, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT4, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT5, 
 wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT6, 
 wxID_PEMBUATAN_SURAT_KELUARSTATUS_KAWIN, 
 wxID_PEMBUATAN_SURAT_KELUARSTATUS_KEPENDUDUKAN, 
 wxID_PEMBUATAN_SURAT_KELUARSTATUS_TINGGAL, 
 wxID_PEMBUATAN_SURAT_KELUARTANGGAL_LAHIR, 
 wxID_PEMBUATAN_SURAT_KELUARTEMPAT_LAHIR, 
 wxID_PEMBUATAN_SURAT_KELUARTGL_SURAT, wxID_PEMBUATAN_SURAT_KELUARWARGANEGARA, 
 wxID_PEMBUATAN_SURAT_KELUARWEBSITE, 
] = [wx.NewId() for _init_ctrls in range(58)]

class pembuatan_surat_keluar(wx.Frame):
    def _init_coll_list_surat_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='No',
              width=35)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor Surat', width=200)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Perihal Surat', width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Tanggal Surat', width=260)

    def _init_coll_penduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Penduduk', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=160)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=290)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_PEMBUATAN_SURAT_KELUAR,
              name=u'pembuatan_surat_keluar', parent=prnt, pos=wx.Point(450,
              199), size=wx.Size(826, 435), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Pembuatan Surat Keluar')
        self.SetClientSize(wx.Size(826, 435))
        self.Center(wx.BOTH)

        self.penduduk = wx.ListCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPENDUDUK,
              name=u'penduduk', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(800, 100), style=wx.LC_REPORT)
        self._init_coll_penduduk_Columns(self.penduduk)
        self.penduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnList_pendudukListItemSelected,
              id=wxID_PEMBUATAN_SURAT_KELUARPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT1,
              label=u'Nama Penduduk', name='staticText1', parent=self,
              pos=wx.Point(288, 128), size=wx.Size(107, 24), style=0)

        self.cari_penduduk = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARCARI_PENDUDUK,
              name=u'cari_penduduk', parent=self, pos=wx.Point(408, 120),
              size=wx.Size(304, 32), style=0, value='')

        self.button1 = wx.Button(id=wxID_PEMBUATAN_SURAT_KELUARBUTTON1,
              label=u'Cari', name='button1', parent=self, pos=wx.Point(720,
              120), size=wx.Size(85, 30), style=0)

        self.staticText2 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT2,
              label=u'Nama Penduduk', name='staticText2', parent=self,
              pos=wx.Point(8, 344), size=wx.Size(107, 17), style=0)

        self.nama_lengkap = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_LENGKAP,
              name='nama_lengkap', parent=self, pos=wx.Point(127, 335),
              size=wx.Size(217, 25), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT3,
              label=u'PEMBUATAN SURAT / GENERATE SURAT OTOMATIS',
              name='staticText3', parent=self, pos=wx.Point(8, 280),
              size=wx.Size(317, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT4,
              label=u'NIK', name='staticText4', parent=self, pos=wx.Point(352,
              344), size=wx.Size(22, 17), style=0)

        self.no_nik = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNO_NIK,
              name='no_nik', parent=self, pos=wx.Point(383, 335),
              size=wx.Size(177, 25), style=0, value='')

        self.comboBox1 = wx.ComboBox(choices=['Surat Keterangan Pengantar',
              'Surat Keterangan Moyang', 'Surat Keterangan Wali Nikah',
              'Surat Keterangan Jalan', 'Surat Keterangan Kelahiran',
              'Keterangan Kematian', 'Pengentar Pindah Antar Kabupaten',
              'Keterangan Untuk Menikah', 'Keterangan Asal Usul',
              'Persetujuan Mempelai', 'Keterangan Tentang Orang Tua',
              'Ijin Orang Tua'], id=wxID_PEMBUATAN_SURAT_KELUARCOMBOBOX1,
              name='comboBox1', parent=self, pos=wx.Point(568, 336),
              size=wx.Size(240, 27), style=0, value='')

        self.list_surat = wx.ListCtrl(id=wxID_PEMBUATAN_SURAT_KELUARLIST_SURAT,
              name=u'list_surat', parent=self, pos=wx.Point(8, 176),
              size=wx.Size(800, 100), style=wx.LC_REPORT)
        self._init_coll_list_surat_Columns(self.list_surat)

        self.staticText5 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT5,
              label=u'Nomor Surat Terakhir', name='staticText5', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(137, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARSTATICTEXT6,
              label=u'Masukan Nomor Surat', name='staticText6', parent=self,
              pos=wx.Point(8, 312), size=wx.Size(145, 17), style=0)

        self.no_surat = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNO_SURAT,
              name=u'no_surat', parent=self, pos=wx.Point(160, 304),
              size=wx.Size(296, 27), style=0, value='')

        self.button2 = wx.Button(id=wxID_PEMBUATAN_SURAT_KELUARBUTTON2,
              label=u'Buat Surat Otomatis', name='button2', parent=self,
              pos=wx.Point(200, 384), size=wx.Size(240, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_PEMBUATAN_SURAT_KELUARBUTTON2)

        self.button3 = wx.Button(id=wxID_PEMBUATAN_SURAT_KELUARBUTTON3,
              label=u'Kembali Ke Menu', name='button3', parent=self,
              pos=wx.Point(448, 384), size=wx.Size(216, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_PEMBUATAN_SURAT_KELUARBUTTON3)

        self.tgl_surat = wx.StaticText(id=wxID_PEMBUATAN_SURAT_KELUARTGL_SURAT,
              label=u'Tanggal', name=u'tgl_surat', parent=self,
              pos=wx.Point(464, 312), size=wx.Size(49, 15), style=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_PEMBUATAN_SURAT_KELUARDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(536, 304),
              size=wx.Size(272, 26), style=wx.DP_SHOWCENTURY)

        self.perusahaankerja = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPERUSAHAANKERJA,
              name='perusahaankerja', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.negarakerja = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNEGARAKERJA,
              name='negarakerja', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pindahkerja = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPINDAHKERJA,
              name='pindahkerja', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.kematian = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARKEMATIAN,
              name='kematian', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.kemiskinan = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARKEMISKINAN,
              name='kemiskinan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.rw = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARRW, name='rw',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(80, 25),
              style=wx.TE_NOHIDESEL, value='')

        self.rt = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARRT, name='rt',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(80, 25),
              style=wx.TE_NOHIDESEL, value='')

        self.nama_dusun = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_DUSUN,
              name='nama_dusun', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.alamat = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARALAMAT,
              name='alamat', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_ibu = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_IBU,
              name='nama_ibu', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_ayah = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_AYAH,
              name='nama_ayah', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pindahkerja = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPINDAHKERJA,
              name='pindahkerja', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.shdk = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARSHDK, name='shdk',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(80, 25),
              style=wx.TE_NOHIDESEL, value='')

        self.kehamilan = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARKEHAMILAN,
              name='kehamilan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.kontrasepsi = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARKONTRASEPSI,
              name='kontrasepsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.difabelitas = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARDIFABELITAS,
              name='difabelitas', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.status_tinggal = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARSTATUS_TINGGAL,
              name='status_tinggal', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.status_kependudukan = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARSTATUS_KEPENDUDUKAN,
              name='status_kependudukan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.status_kawin = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARSTATUS_KAWIN,
              name='status_kawin', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pekerjaan_lain = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPEKERJAAN_LAIN,
              name='pekerjaan_lain', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pekerjaan_utama = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPEKERJAAN_UTAMA,
              name='pekerjaan_utama', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pendidikan_saat_ini = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPENDIDIKAN_SAAT_INI,
              name='pendidikan_saat_ini', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.pendidikan_akhir = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARPENDIDIKAN_AKHIR,
              name='pendidikan_akhir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.warganegara = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARWARGANEGARA,
              name='warganegara', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.agama = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARAGAMA,
              name='agama', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.gol_darah = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARGOL_DARAH,
              name='gol_darah', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.tanggal_lahir = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARTANGGAL_LAHIR,
              name='tanggal_lahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.tempat_lahir = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARTEMPAT_LAHIR,
              name='tempat_lahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.jenis_kelamin = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARJENIS_KELAMIN,
              name='jenis_kelamin', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_lengkap = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_LENGKAP,
              name='nama_lengkap', parent=self, pos=wx.Point(127, 335),
              size=wx.Size(217, 25), style=0, value='')

        self.no_nik = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNO_NIK,
              name='no_nik', parent=self, pos=wx.Point(383, 335),
              size=wx.Size(177, 25), style=0, value='')

        self.no_kk = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNO_KK,
              name='no_kk', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_desa = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_DESA,
              name='nama_desa', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_kecamatan = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_KECAMATAN,
              name='nama_kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_kabupaten = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_KABUPATEN,
              name='nama_kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_propinsi = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_PROPINSI,
              name='nama_propinsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.alamat_kantor = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARALAMAT_KANTOR,
              name='alamat_kantor', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.website = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARWEBSITE,
              name='website', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.email = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUAREMAIL,
              name='email', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

        self.no_telp = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNO_TELP,
              name='no_telp', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(217, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_kades = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_KADES,
              name='nama_kades', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(177, 25), style=wx.TE_NOHIDESEL, value='')

        self.nama_sekdes = wx.TextCtrl(id=wxID_PEMBUATAN_SURAT_KELUARNAMA_SEKDES,
              name='nama_sekdes', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(80, 25), style=wx.TE_NOHIDESEL, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.IsiList()
        self.IsiList1()
        
        
    def IsiList(self):    
        sql = "SELECT * FROM penduduk"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.penduduk.GetItemCount() 
        for i in hasil : 
            self.penduduk.InsertStringItem(nokk, "%s"%i[45]) 
            self.penduduk.SetStringItem(nokk,1,"%s"%i[44]) 
            self.penduduk.SetStringItem(nokk,2,"%s"%i[16]) 
            nokk = nokk + 1  
    
    def IsiList1(self):    
        sql = "SELECT * FROM suratkeluar"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.list_surat.GetItemCount() 
        for i in hasil : 
            self.list_surat.InsertStringItem(nokk, "%s"%i[0]) 
            self.list_surat.SetStringItem(nokk,1,"%s"%i[1]) 
            self.list_surat.SetStringItem(nokk,2,"%s"%i[2])
            self.list_surat.SetStringItem(nokk,2,"%s"%i[3]) 
            nokk = nokk + 1  
            
    def Isi_Object(self) : 
        caripenduduk=str(self.cari_penduduk.GetValue())
        sql="SELECT * FROM penduduk WHERE nama_lengkap='%s'"%(caripenduduk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.perusahaankerja.SetValue(str(hasil[1]))
            self.negarakerja.SetValue(str(hasil[2]))
            self.pindahkerja.SetValue(str(hasil[3]))
            self.kematian.SetValue(str(hasil[4]))
            
            self.kemiskinan.SetValue(str(hasil[13]))
            self.rw.SetValue(str(hasil[14]))
            self.rt.SetValue(str(hasil[15]))
            self.nama_dusun.SetValue(str(hasil[16]))
            self.alamat.SetValue(str(hasil[17]))
            self.nama_ibu.SetValue(str(hasil[18]))
            self.nama_ayah.SetValue(str(hasil[19]))
            self.shdk.SetValue(str(hasil[20]))
            
            self.kehamilan.SetValue(str(hasil[29]))
            self.kontrasepsi.SetValue(str(hasil[30]))
            self.difabelitas.SetValue(str(hasil[31]))
            self.status_tinggal.SetValue(str(hasil[32]))
            self.status_kependudukan.SetValue(str(hasil[33]))
            self.status_kawin.SetValue(str(hasil[34]))
            self.pekerjaan_lain.SetValue(str(hasil[35]))
            self.pekerjaan_utama.SetValue(str(hasil[36]))
            self.pendidikan_saat_ini.SetValue(str(hasil[37]))
            self.pendidikan_akhir.SetValue(str(hasil[38]))
            self.warganegara.SetValue(str(hasil[39]))
            self.agama.SetValue(str(hasil[40]))
            self.gol_darah.SetValue(str(hasil[41]))
            self.tanggal_lahir.SetValue(str(hasil[42]))
            self.tempat_lahir.SetValue(str(hasil[43]))
            self.jenis_kelamin.SetValue(str(hasil[44]))
            self.nama_lengkap.SetValue(str(hasil[45]))
            self.no_nik.SetValue(str(hasil[46]))
            self.no_kk.SetValue(str(hasil[47]))            
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_penduduk.Clear()
            self.cari_penduduk.SetFocus()   

    
    def create_pdf0(self):
        nosurat=str(self.no_surat.GetValue())
        aa=str(self.perusahaankerja.GetValue())
        ab=str(self.negarakerja.GetValue())
        ac=str(self.pindahkerja.GetValue())
        ad=str(self.kematian.GetValue())
        am=str(self.kemiskinan.GetValue())
        ao=str(self.rw.GetValue())
        ap=str(self.rt.GetValue())
        aq=str(self.nama_dusun.GetValue())
        ar=str(self.alamat.GetValue())
        at=str(self.nama_ibu.GetValue())
        au=str(self.nama_ayah.GetValue())
        av=str(self.shdk.GetValue())
        be=str(self.kehamilan.GetValue())
        bf=str(self.kontrasepsi.GetValue())
        bg=str(self.difabelitas.GetValue())
        bh=str(self.status_tinggal.GetValue())
        bi=str(self.status_kependudukan.GetValue())
        bj=str(self.status_kawin.GetValue())
        bk=str(self.pekerjaan_lain.GetValue())
        bl=str(self.pekerjaan_utama.GetValue())
        bm=str(self.pendidikan_saat_ini.GetValue())
        bn=str(self.pendidikan_akhir.GetValue())
        bo=str(self.warganegara.GetValue())
        bp=str(self.agama.GetValue())
        bq=str(self.gol_darah.GetValue())
        br=str(self.tanggal_lahir.GetValue())
        bs=str(self.tempat_lahir.GetValue())
        bt=str(self.jenis_kelamin.GetValue())
        bu=str(self.nama_lengkap.GetValue())
        bv=str(self.no_nik.GetValue())
        bw=str(self.no_kk.GetValue())             
        
        c = canvas.Canvas(""+bu+"+"+bv+".pdf", pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 12)
 
        c.drawString(30,750,'PEMERINTAH KABUPATEN')
        c.drawString(30,736,'KECAMATAN')
        c.drawString(30,722,'DESA')
        c.drawString(30,690,'Alamat :')
        c.line(30,676,580,676)
        c.drawString(30,662,'Nomor Kode Kelurahan :')
        c.drawString(30,648,'SURAT KETERANGAN')
        c.drawString(30,634,'Nomor :')
        c.drawString(30,620,'Yang bertanda tangan dibawah ini, menerangkan bahwa:')
        c.drawString(30,606,'1. Nama                     :')
        c.drawString(30,592,'2. Tempat & Tanggal Lahir   :')
        c.drawString(30,578,'3. Kewarnegaraan & Agama    :')
        c.drawString(30,564,'4. Pekerjaan                :')
        c.drawString(30,564,'5. Tempat Tinggal           :')
        c.drawString(30,564,'   Kabupaten                :')
        c.drawString(30,564,'6. Surat Bukti Diri                :')
        c.drawString(30,564,'7. Keperluan                :')
        c.drawString(30,564,'8. Berlaku Mulai            :')
        c.drawString(30,564,'9. Keterangan Lain-lain*)   :')
        c.save()
        call(["xpdf", ""+bu+"+"+bv+".pdf"])
        
    def create_pdf1(self):
             
        c = canvas.Canvas("form.pdf", pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 10)
 
        c.drawString(30,750,'Surat Keterangan Moyang')
        c.drawString(30,740,'KECAMATAN')
        c.drawString(30,730,'DESA')
        c.drawString(30,720,'Alamat :')
        c.line(30,730,580,730)
        c.drawString(30,710,'Nomor Kode Kelurahan :')
        c.drawString(30,700,'Surat Keterangan')
        c.drawString(30,690,'Nomor :')
        c.save()
        call(["xpdf", "(nosurat).pdf"])
    
    def create_pdf2(self):
             
        c = canvas.Canvas("form.pdf", pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 10)
 
        c.drawString(30,750,'Surat Keterangan Wali Nikah')
        c.drawString(30,740,'KECAMATAN')
        c.drawString(30,730,'DESA')
        c.drawString(30,720,'Alamat :')
        c.line(30,730,580,730)
        c.drawString(30,710,'Nomor Kode Kelurahan :')
        c.drawString(30,700,'Surat Keterangan')
        c.drawString(30,690,'Nomor :')
        c.save()
        call(["xpdf", "form.pdf"])
    
    def create_pdf3(self):
             
        c = canvas.Canvas("form.pdf", pagesize=letter)
        c.setLineWidth(.3)
        c.setFont('Helvetica', 10)
 
        c.drawString(30,750,'Surat Keterangan Jalan')
        c.drawString(30,740,'KECAMATAN')
        c.drawString(30,730,'DESA')
        c.drawString(30,720,'Alamat :')
        c.line(30,730,580,730)
        c.drawString(30,710,'Nomor Kode Kelurahan :')
        c.drawString(30,700,'Surat Keterangan')
        c.drawString(30,690,'Nomor :')
        c.save()
        call(["xpdf", "form.pdf"])        
    

    def OnButton3Button(self, event):
        
        
            self.main=input_administrasi_surat.create(None)
            self.main.Show()
            self.Close()

    def OnList_pendudukListItemSelected(self, event):
        self.currentItem = event.m_itemIndex # mengambil no index baris yang dipilih 
        b=self.penduduk.GetItem(self.currentItem).GetText() # no index baris dikonversi ke text/ string 
        self.cari_penduduk.SetValue(b) 
        self.Isi_Object() 
        event.Skip()    

    def OnButton2Button(self, event):
        pilihan = str(self.comboBox1.GetValue())
        if pilihan == 'Surat Keterangan Pengantar':
           self.create_pdf0()
        elif pilihan == 'Surat Keterangan Moyang':
           self.create_pdf1()
        elif pilihan == 'Surat Keterangan Wali Nikah':
           self.create_pdf2()
        elif pilihan == 'Surat Keterangan Jalan':
           self.create_pdf3()
        else:         
            event.Skip()

