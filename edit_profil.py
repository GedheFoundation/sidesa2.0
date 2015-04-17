#Boa:Frame:edit_profil

import wx
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return edit_profil(parent)

[wxID_EDIT_PROFIL, wxID_EDIT_PROFILINPUT_ALAMAT, wxID_EDIT_PROFILINPUT_DESA, 
 wxID_EDIT_PROFILINPUT_DUSUN1, wxID_EDIT_PROFILINPUT_DUSUN2, 
 wxID_EDIT_PROFILINPUT_DUSUN3, wxID_EDIT_PROFILINPUT_DUSUN4, 
 wxID_EDIT_PROFILINPUT_DUSUN5, wxID_EDIT_PROFILINPUT_DUSUN6, 
 wxID_EDIT_PROFILINPUT_EMAIL, wxID_EDIT_PROFILINPUT_KABUPATEN, 
 wxID_EDIT_PROFILINPUT_KADES, wxID_EDIT_PROFILINPUT_KECAMATAN, 
 wxID_EDIT_PROFILINPUT_KODE, wxID_EDIT_PROFILINPUT_PROPINSI, 
 wxID_EDIT_PROFILINPUT_SEKDES, wxID_EDIT_PROFILINPUT_TELP, 
 wxID_EDIT_PROFILINPUT_WEB, wxID_EDIT_PROFILLABEL_ALAMAT, 
 wxID_EDIT_PROFILLABEL_DUKUH, wxID_EDIT_PROFILLABEL_KADES, 
 wxID_EDIT_PROFILLABEL_KECAMATAN, wxID_EDIT_PROFILLABEL_KODE_DESA, 
 wxID_EDIT_PROFILLABEL_NAMA_DESA, wxID_EDIT_PROFILLABEL_PROPINSI, 
 wxID_EDIT_PROFILLABEL_SEKDES, wxID_EDIT_PROFILLABEL_WEB, 
 wxID_EDIT_PROFILLABLE_KABUPATEN, wxID_EDIT_PROFILLOGO, 
 wxID_EDIT_PROFILSTATICTEXT1, wxID_EDIT_PROFILSTATICTEXT2, 
 wxID_EDIT_PROFILSTATICTEXT3, wxID_EDIT_PROFILSTATICTEXT4, 
 wxID_EDIT_PROFILSTATICTEXT5, wxID_EDIT_PROFILSTATICTEXT6, 
 wxID_EDIT_PROFILSTATICTEXT7, wxID_EDIT_PROFILTELP, 
 wxID_EDIT_PROFILTOMBOL_KEMBALI, wxID_EDIT_PROFILTOMBOL_SIMPAN, 
] = [wx.NewId() for _init_ctrls in range(39)]

class edit_profil(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_PROFIL, name=u'edit_profil',
              parent=prnt, pos=wx.Point(445, 203), size=wx.Size(911, 325),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Input Profil Desa')
        self.SetClientSize(wx.Size(911, 325))
        self.Center(wx.BOTH)

        self.logo = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PROFILLOGO, name=u'logo', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(152, 144), style=0)

        self.label_nama_desa = wx.StaticText(id=wxID_EDIT_PROFILLABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(73, 17), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_EDIT_PROFILLABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 80), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_EDIT_PROFILLABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(192, 112), size=wx.Size(51, 17), style=0)

        self.input_desa = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DESA,
              name=u'input_desa', parent=self, pos=wx.Point(280, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kabupaten = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_KABUPATEN,
              name=u'input_kabupaten', parent=self, pos=wx.Point(280, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_propinsi = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_PROPINSI,
              name=u'input_propinsi', parent=self, pos=wx.Point(280, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.input_web = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_WEB,
              name=u'input_web', parent=self, pos=wx.Point(656, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kode = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_KODE,
              name=u'input_kode', parent=self, pos=wx.Point(656, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.input_kades = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_KADES,
              name=u'input_kades', parent=self, pos=wx.Point(656, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.input_sekdes = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_SEKDES,
              name=u'input_sekdes', parent=self, pos=wx.Point(656, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.label_web = wx.StaticText(id=wxID_EDIT_PROFILLABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(544, 16), size=wx.Size(104, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(544, 48), size=wx.Size(91, 17), style=0)

        self.label_kades = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KADES,
              label=u'Nama KADES', name=u'label_kades', parent=self,
              pos=wx.Point(544, 80), size=wx.Size(88, 17), style=0)

        self.label_sekdes = wx.StaticText(id=wxID_EDIT_PROFILLABEL_SEKDES,
              label=u'Nama SEKDES', name=u'label_sekdes', parent=self,
              pos=wx.Point(544, 112), size=wx.Size(96, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_EDIT_PROFILLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 144), size=wx.Size(47, 17), style=0)

        self.label_dukuh = wx.StaticText(id=wxID_EDIT_PROFILLABEL_DUKUH,
              label=u'Daftar Nama Dusun / Dukuh', name=u'label_dukuh',
              parent=self, pos=wx.Point(24, 184), size=wx.Size(576, 17),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(16,
              208), size=wx.Size(13, 17), style=0)

        self.input_dusun1 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN1,
              name=u'input_dusun1', parent=self, pos=wx.Point(40, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun2 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN2,
              name=u'input_dusun2', parent=self, pos=wx.Point(40, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun3 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN3,
              name=u'input_dusun3', parent=self, pos=wx.Point(336, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun4 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN4,
              name=u'input_dusun4', parent=self, pos=wx.Point(336, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun5 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN5,
              name=u'input_dusun5', parent=self, pos=wx.Point(640, 208),
              size=wx.Size(256, 24), style=0, value='')

        self.input_dusun6 = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_DUSUN6,
              name=u'input_dusun6', parent=self, pos=wx.Point(640, 240),
              size=wx.Size(256, 24), style=0, value='')

        self.input_alamat = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(280, 144),
              size=wx.Size(280, 24), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT3,
              label=u'2.', name='staticText3', parent=self, pos=wx.Point(16,
              240), size=wx.Size(13, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT4,
              label=u'3.', name='staticText4', parent=self, pos=wx.Point(312,
              208), size=wx.Size(13, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT5,
              label=u'4.', name='staticText5', parent=self, pos=wx.Point(312,
              240), size=wx.Size(13, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT6,
              label=u'5.', name='staticText6', parent=self, pos=wx.Point(616,
              208), size=wx.Size(13, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT7,
              label=u'6.', name='staticText7', parent=self, pos=wx.Point(616,
              240), size=wx.Size(13, 17), style=0)

        self.input_kecamatan = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_KECAMATAN,
              name=u'input_kecamatan', parent=self, pos=wx.Point(280, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.tombol_simpan = wx.Button(id=wxID_EDIT_PROFILTOMBOL_SIMPAN,
              label=u'Simpan Data', name=u'tombol_simpan', parent=self,
              pos=wx.Point(280, 280), size=wx.Size(192, 30), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_EDIT_PROFILTOMBOL_SIMPAN)

        self.tombol_kembali = wx.Button(id=wxID_EDIT_PROFILTOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(480, 280), size=wx.Size(184, 30), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_EDIT_PROFILTOMBOL_KEMBALI)

        self.telp = wx.StaticText(id=wxID_EDIT_PROFILTELP, label=u'Telp',
              name=u'telp', parent=self, pos=wx.Point(568, 144),
              size=wx.Size(25, 15), style=0)

        self.input_telp = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_TELP,
              name=u'input_telp', parent=self, pos=wx.Point(608, 144),
              size=wx.Size(128, 25), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT2,
              label=u'Email', name='staticText2', parent=self, pos=wx.Point(744,
              144), size=wx.Size(36, 15), style=0)

        self.input_email = wx.TextCtrl(id=wxID_EDIT_PROFILINPUT_EMAIL,
              name=u'input_email', parent=self, pos=wx.Point(792, 144),
              size=wx.Size(104, 25), style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        sql = "SELECT *  FROM identitas"
        cur.execute(sql)
        for row in cur:
            self.input_desa.SetValue(str(row[6]))
            self.input_kecamatan.SetValue(str(row[7]))
            self.input_kabupaten.SetValue(str(row[8]))
            self.input_propinsi.SetValue(str(row[9]))
            self.input_alamat.SetValue(str(row[10]))
            self.input_web.SetValue(str(row[11]))
            self.input_kode.SetValue(str(row[16]))
            self.input_kades.SetValue(str(row[14]))
            self.input_sekdes.SetValue(str(row[15]))
            self.input_dusun1.SetValue(str(row[5]))
            self.input_dusun2.SetValue(str(row[4]))
            self.input_dusun3.SetValue(str(row[3]))
            self.input_dusun4.SetValue(str(row[2]))
            self.input_dusun5.SetValue(str(row[1]))
            self.input_dusun6.SetValue(str(row[0]))
            self.input_telp.SetValue(str(row[13]))
            self.input_email.SetValue(str(row[12]))
        
    
     
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
        add_identitas="UPDATE identitas SET dusun6='%s', dusun5'%s', dusun4'%s', dusun3'%s', dusun2'%s', dusun1'%s', nama_desa'%s', nama_kecamatan'%s', nama_kabupaten'%s', nama_propinsi'%s', alamat_kantor'%s', website'%s', email'%s', no_telp'%s', nama_kades'%s', nama_sekdes'%s' VALUES('"+(inputdusun6)+"', '"+(inputdusun5)+"', '"+(inputdusun4)+"', '"+(inputdusun3)+"', '"+(inputdusun2)+"', '"+(inputdusun1)+"', '"+(inputdesa)+"', '"+(inputkecamatan)+"', '"+(inputkabupaten)+"', '"+(inputpropinsi)+"', '"+(inputalamat)+"', '"+(inputweb)+"', '"+(inputemail)+"', '"+(inputtelp)+"', '"+(inputkades)+"', '"+(inputsekdes)+"')"
        cur.execute(add_identitas)
        db.commit()
        self.pesan = wx.MessageDialog(self,"Data Identitas Desa Terupdate ","Konfirmasi",wx.OK) 
        self.pesan.ShowModal() 
        self.Close()
        self.Destroy()
