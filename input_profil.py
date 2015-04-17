#Boa:Frame:input_profil_desa

import wx
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return input_profil_desa(parent)

[wxID_INPUT_PROFIL_DESA, wxID_INPUT_PROFIL_DESAINPUT_ALAMAT, 
 wxID_INPUT_PROFIL_DESAINPUT_DESA, wxID_INPUT_PROFIL_DESAINPUT_DUSUN1, 
 wxID_INPUT_PROFIL_DESAINPUT_DUSUN2, wxID_INPUT_PROFIL_DESAINPUT_DUSUN3, 
 wxID_INPUT_PROFIL_DESAINPUT_DUSUN4, wxID_INPUT_PROFIL_DESAINPUT_DUSUN5, 
 wxID_INPUT_PROFIL_DESAINPUT_DUSUN6, wxID_INPUT_PROFIL_DESAINPUT_EMAIL, 
 wxID_INPUT_PROFIL_DESAINPUT_KABUPATEN, wxID_INPUT_PROFIL_DESAINPUT_KADES, 
 wxID_INPUT_PROFIL_DESAINPUT_KECAMATAN, wxID_INPUT_PROFIL_DESAINPUT_KODE, 
 wxID_INPUT_PROFIL_DESAINPUT_PROPINSI, wxID_INPUT_PROFIL_DESAINPUT_SEKDES, 
 wxID_INPUT_PROFIL_DESAINPUT_TELP, wxID_INPUT_PROFIL_DESAINPUT_WEB, 
 wxID_INPUT_PROFIL_DESALABEL_ALAMAT, wxID_INPUT_PROFIL_DESALABEL_DUKUH, 
 wxID_INPUT_PROFIL_DESALABEL_KADES, wxID_INPUT_PROFIL_DESALABEL_KECAMATAN, 
 wxID_INPUT_PROFIL_DESALABEL_KODE_DESA, wxID_INPUT_PROFIL_DESALABEL_NAMA_DESA, 
 wxID_INPUT_PROFIL_DESALABEL_PROPINSI, wxID_INPUT_PROFIL_DESALABEL_SEKDES, 
 wxID_INPUT_PROFIL_DESALABEL_WEB, wxID_INPUT_PROFIL_DESALABLE_KABUPATEN, 
 wxID_INPUT_PROFIL_DESALOGO, wxID_INPUT_PROFIL_DESASTATICTEXT1, 
 wxID_INPUT_PROFIL_DESASTATICTEXT2, wxID_INPUT_PROFIL_DESASTATICTEXT3, 
 wxID_INPUT_PROFIL_DESASTATICTEXT4, wxID_INPUT_PROFIL_DESASTATICTEXT5, 
 wxID_INPUT_PROFIL_DESASTATICTEXT6, wxID_INPUT_PROFIL_DESASTATICTEXT7, 
 wxID_INPUT_PROFIL_DESATELP, wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI, 
 wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN, 
] = [wx.NewId() for _init_ctrls in range(39)]

class input_profil_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_INPUT_PROFIL_DESA,
              name=u'input_profil_desa', parent=prnt, pos=wx.Point(393, 235),
              size=wx.Size(911, 325), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Input Profil Desa')
        self.SetClientSize(wx.Size(911, 325))
        self.Center(wx.BOTH)

        self.logo = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_INPUT_PROFIL_DESALOGO, name=u'logo', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(152, 144), style=0)

        self.label_nama_desa = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(73, 17), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 80), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(192, 112), size=wx.Size(51, 17), style=0)

        self.input_desa = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DESA,
              name=u'input_desa', parent=self, pos=wx.Point(280, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kabupaten = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_KABUPATEN,
              name=u'input_kabupaten', parent=self, pos=wx.Point(280, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_propinsi = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_PROPINSI,
              name=u'input_propinsi', parent=self, pos=wx.Point(280, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.input_web = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_WEB,
              name=u'input_web', parent=self, pos=wx.Point(656, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kode = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_KODE,
              name=u'input_kode', parent=self, pos=wx.Point(656, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kades = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_KADES,
              name=u'input_kades', parent=self, pos=wx.Point(656, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_sekdes = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_SEKDES,
              name=u'input_sekdes', parent=self, pos=wx.Point(656, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.label_web = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(544, 16), size=wx.Size(104, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(544, 48), size=wx.Size(91, 17), style=0)

        self.label_kades = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KADES,
              label=u'Nama KADES', name=u'label_kades', parent=self,
              pos=wx.Point(544, 80), size=wx.Size(88, 17), style=0)

        self.label_sekdes = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_SEKDES,
              label=u'Nama SEKDES', name=u'label_sekdes', parent=self,
              pos=wx.Point(544, 112), size=wx.Size(96, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 144), size=wx.Size(47, 17), style=0)

        self.label_dukuh = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_DUKUH,
              label=u'Daftar Nama Dusun / Dukuh', name=u'label_dukuh',
              parent=self, pos=wx.Point(24, 184), size=wx.Size(576, 17),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(16,
              208), size=wx.Size(13, 17), style=0)

        self.input_dusun1 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN1,
              name=u'input_dusun1', parent=self, pos=wx.Point(40, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun2 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN2,
              name=u'input_dusun2', parent=self, pos=wx.Point(40, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun3 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN3,
              name=u'input_dusun3', parent=self, pos=wx.Point(336, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun4 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN4,
              name=u'input_dusun4', parent=self, pos=wx.Point(336, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun5 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN5,
              name=u'input_dusun5', parent=self, pos=wx.Point(640, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun6 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_DUSUN6,
              name=u'input_dusun6', parent=self, pos=wx.Point(640, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_alamat = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(280, 144),
              size=wx.Size(280, 24), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT3,
              label=u'2.', name='staticText3', parent=self, pos=wx.Point(16,
              240), size=wx.Size(13, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT4,
              label=u'3.', name='staticText4', parent=self, pos=wx.Point(312,
              208), size=wx.Size(13, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT5,
              label=u'4.', name='staticText5', parent=self, pos=wx.Point(312,
              240), size=wx.Size(13, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT6,
              label=u'5.', name='staticText6', parent=self, pos=wx.Point(616,
              208), size=wx.Size(13, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT7,
              label=u'6.', name='staticText7', parent=self, pos=wx.Point(616,
              240), size=wx.Size(13, 17), style=0)

        self.input_kecamatan = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_KECAMATAN,
              name=u'input_kecamatan', parent=self, pos=wx.Point(280, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.tombol_simpan = wx.Button(id=wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN,
              label=u'Simpan Data', name=u'tombol_simpan', parent=self,
              pos=wx.Point(280, 280), size=wx.Size(192, 30), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN)

        self.tombol_kembali = wx.Button(id=wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(480, 280), size=wx.Size(184, 30), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI)

        self.telp = wx.StaticText(id=wxID_INPUT_PROFIL_DESATELP, label=u'Telp',
              name=u'telp', parent=self, pos=wx.Point(568, 144),
              size=wx.Size(25, 15), style=0)

        self.input_telp = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_TELP,
              name=u'input_telp', parent=self, pos=wx.Point(608, 144),
              size=wx.Size(128, 25), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT2,
              label=u'Email', name='staticText2', parent=self, pos=wx.Point(744,
              144), size=wx.Size(36, 15), style=0)

        self.input_email = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAINPUT_EMAIL,
              name=u'input_email', parent=self, pos=wx.Point(792, 144),
              size=wx.Size(104, 25), style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.cekisi()
        
    def cekisi(self):   
        namadesa=str(self.input_desa.GetValue())
        if namadesa == '' :
            self.tombol_simpan.Enable=True
        else:
            self.tombol_simpan.Enable=False
            self.pesan = wx.MessageDialog(self,"Data Telah Terisi \n Silahkan Diedit","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
     
    def OnTombol_kembaliButton(self, event):
        self.Close()
        self.Destroy()

    def OnTombol_simpanButton(self, event):
        inputdesa = str(self.input_desa.GetValue())
        inputkecamatan = str(self.input_kecamatan.GetValue())
        inputkabupaten = str(self.input_kabupaten.GetValue())
        inputpropinsi = str(self.input_propinsi.GetValue())
        inputalamat = str(self.input_alamat.GetValue())
        inputweb = str(self.input_web.GetValue())
        inputkodedesa = str(self.input_kode.GetValue())
        inputkades = str(self.input_kades.GetValue())
        inputsekdes = str(self.input_sekdes.GetValue())
        inputdusun1 = str(self.input_dusun1.GetValue())
        inputdusun2 = str(self.input_dusun2.GetValue())
        inputdusun3 = str(self.input_dusun3.GetValue())
        inputdusun4 = str(self.input_dusun4.GetValue())
        inputdusun5 = str(self.input_dusun5.GetValue())
        inputdusun6 = str(self.input_dusun6.GetValue())
        inputtelp = str(self.input_telp.GetValue())
        inputemail = str(self.input_email.GetValue())
        add_identitas="INSERT INTO identitas (dusun6, dusun5, dusun4, dusun3, dusun2, dusun1, nama_desa, nama_kecamatan, nama_kabupaten, nama_propinsi, alamat_kantor, website, email, no_telp, nama_kades, nama_sekdes) VALUES('"+(inputdusun6)+"', '"+(inputdusun5)+"', '"+(inputdusun4)+"', '"+(inputdusun3)+"', '"+(inputdusun2)+"', '"+(inputdusun1)+"', '"+(inputdesa)+"', '"+(inputkecamatan)+"', '"+(inputkabupaten)+"', '"+(inputpropinsi)+"', '"+(inputalamat)+"', '"+(inputweb)+"', '"+(inputemail)+"', '"+(inputtelp)+"', '"+(inputkades)+"', '"+(inputsekdes)+"')"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Identitas Desa Tersimpan ","Konfirmasi",wx.OK) 
        self.pesan.ShowModal() 
        self.Close()
        self.Destroy()
