#Boa:Frame:input_data_kemiskinan

import wx
import wx.lib.buttons
import frm_sideka_menu
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return input_data_kemiskinan(parent)

[wxID_INPUT_DATA_KEMISKINAN, wxID_INPUT_DATA_KEMISKINANBUTTON1, 
 wxID_INPUT_DATA_KEMISKINANBUTTON2, wxID_INPUT_DATA_KEMISKINANBUTTON3, 
 wxID_INPUT_DATA_KEMISKINANCARI_KK, wxID_INPUT_DATA_KEMISKINANCEK_BLSM, 
 wxID_INPUT_DATA_KEMISKINANCEK_BSM, wxID_INPUT_DATA_KEMISKINANCEK_JKN, 
 wxID_INPUT_DATA_KEMISKINANCEK_PKD, wxID_INPUT_DATA_KEMISKINANCEK_PKH, 
 wxID_INPUT_DATA_KEMISKINANCEK_PPD, wxID_INPUT_DATA_KEMISKINANCEK_PROLAIN, 
 wxID_INPUT_DATA_KEMISKINANCEK_RASKIN, wxID_INPUT_DATA_KEMISKINANINPUT_ALAMAT, 
 wxID_INPUT_DATA_KEMISKINANNAMA_KK, wxID_INPUT_DATA_KEMISKINANNOMOR_KK, 
 wxID_INPUT_DATA_KEMISKINANPENDUDUK, wxID_INPUT_DATA_KEMISKINANSTATICTEXT1, 
 wxID_INPUT_DATA_KEMISKINANSTATICTEXT2, wxID_INPUT_DATA_KEMISKINANSTATICTEXT3, 
 wxID_INPUT_DATA_KEMISKINANSTATICTEXT4, wxID_INPUT_DATA_KEMISKINANSTATICTEXT5, 
 wxID_INPUT_DATA_KEMISKINANSTATICTEXT6, 
 wxID_INPUT_DATA_KEMISKINANSTATUS_MISKIN, 
] = [wx.NewId() for _init_ctrls in range(24)]

class input_data_kemiskinan(wx.Frame):
    def _init_coll_penduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama KK', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=160)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_INPUT_DATA_KEMISKINAN,
              name=u'input_data_kemiskinan', parent=prnt, pos=wx.Point(427,
              180), size=wx.Size(843, 453), style=wx.FRAME_NO_TASKBAR,
              title=u'Input Data Kemiskinan')
        self.SetClientSize(wx.Size(843, 453))
        self.Center(wx.BOTH)

        self.penduduk = wx.ListCtrl(id=wxID_INPUT_DATA_KEMISKINANPENDUDUK,
              name=u'penduduk', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(808, 184), style=wx.LC_REPORT)
        self._init_coll_penduduk_Columns(self.penduduk)
        self.penduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_INPUT_DATA_KEMISKINANPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT1,
              label=u'Nomor Kartu Keluarga', name='staticText1', parent=self,
              pos=wx.Point(408, 200), size=wx.Size(145, 15), style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_INPUT_DATA_KEMISKINANCARI_KK,
              name=u'cari_kk', parent=self, pos=wx.Point(560, 200),
              size=wx.Size(168, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_INPUT_DATA_KEMISKINANBUTTON1,
              label=u'Cari', name='button1', parent=self, pos=wx.Point(744,
              200), size=wx.Size(80, 24), style=0)

        self.staticText2 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT2,
              label=u'Nomor KK', name='staticText2', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(65, 15), style=0)

        self.nomor_kk = wx.TextCtrl(id=wxID_INPUT_DATA_KEMISKINANNOMOR_KK,
              name=u'nomor_kk', parent=self, pos=wx.Point(96, 232),
              size=wx.Size(312, 25), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self,
              pos=wx.Point(416, 232), size=wx.Size(47, 15), style=0)

        self.input_alamat = wx.TextCtrl(id=wxID_INPUT_DATA_KEMISKINANINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(472, 232),
              size=wx.Size(352, 25), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT4,
              label=u'Nama KK', name='staticText4', parent=self,
              pos=wx.Point(16, 264), size=wx.Size(60, 15), style=0)

        self.nama_kk = wx.TextCtrl(id=wxID_INPUT_DATA_KEMISKINANNAMA_KK,
              name=u'nama_kk', parent=self, pos=wx.Point(96, 264),
              size=wx.Size(312, 25), style=0, value='')

        self.staticText5 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT5,
              label=u'Status Kemiskinan', name='staticText5', parent=self,
              pos=wx.Point(416, 264), size=wx.Size(119, 15), style=0)

        self.status_miskin = wx.ComboBox(choices=['Miskin', 'Tidak Miskin'],
              id=wxID_INPUT_DATA_KEMISKINANSTATUS_MISKIN, name=u'status_miskin',
              parent=self, pos=wx.Point(552, 264), size=wx.Size(272, 25),
              style=0, value='')

        self.staticText6 = wx.StaticText(id=wxID_INPUT_DATA_KEMISKINANSTATICTEXT6,
              label=u'Program Perlindungan Sosial', name='staticText6',
              parent=self, pos=wx.Point(16, 296), size=wx.Size(185, 15),
              style=0)

        self.cek_raskin = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_RASKIN,
              label=u'Raskin', name=u'cek_raskin', parent=self, pos=wx.Point(16,
              320), size=wx.Size(89, 18), style=0)
        self.cek_raskin.SetValue(False)

        self.cek_jkn = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_JKN,
              label=u'JKN', name=u'cek_jkn', parent=self, pos=wx.Point(16, 344),
              size=wx.Size(89, 18), style=0)
        self.cek_jkn.SetValue(False)

        self.cek_blsm = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_BLSM,
              label=u'BLSM', name=u'cek_blsm', parent=self, pos=wx.Point(16,
              368), size=wx.Size(89, 18), style=0)
        self.cek_blsm.SetValue(False)

        self.cek_bsm = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_BSM,
              label=u'BSM', name=u'cek_bsm', parent=self, pos=wx.Point(192,
              320), size=wx.Size(89, 18), style=0)
        self.cek_bsm.SetValue(False)

        self.cek_pkh = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_PKH,
              label=u'PKH', name=u'cek_pkh', parent=self, pos=wx.Point(192,
              344), size=wx.Size(89, 18), style=0)
        self.cek_pkh.SetValue(False)

        self.cek_pkd = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_PKD,
              label=u'Program Kesehatan Daerah', name=u'cek_pkd', parent=self,
              pos=wx.Point(192, 368), size=wx.Size(208, 18), style=0)
        self.cek_pkd.SetValue(False)

        self.cek_ppd = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_PPD,
              label=u'Program Pendidikan Daerah', name=u'cek_ppd', parent=self,
              pos=wx.Point(416, 320), size=wx.Size(208, 18), style=0)
        self.cek_ppd.SetValue(False)

        self.cek_prolain = wx.CheckBox(id=wxID_INPUT_DATA_KEMISKINANCEK_PROLAIN,
              label=u'Program Lain', name=u'cek_prolain', parent=self,
              pos=wx.Point(416, 344), size=wx.Size(200, 18), style=0)
        self.cek_prolain.SetValue(False)

        self.button2 = wx.Button(id=wxID_INPUT_DATA_KEMISKINANBUTTON2,
              label=u'Simpan Data', name='button2', parent=self,
              pos=wx.Point(232, 400), size=wx.Size(192, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_INPUT_DATA_KEMISKINANBUTTON2)

        self.button3 = wx.Button(id=wxID_INPUT_DATA_KEMISKINANBUTTON3,
              label=u'Kembali Ke Menu', name='button3', parent=self,
              pos=wx.Point(440, 400), size=wx.Size(184, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_INPUT_DATA_KEMISKINANBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.IsiList()
        
    def IsiList(self):    
        sql = "SELECT * FROM penduduk WHERE shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.penduduk.GetItemCount() 
        for i in hasil : 
            self.penduduk.InsertStringItem(nokk, "%s"%i[46]) 
            self.penduduk.SetStringItem(nokk,1,"%s"%i[44]) 
            self.penduduk.SetStringItem(nokk,2,"%s"%i[16]) 
            nokk = nokk + 1 
    
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE no_kk='%s'"%(carikk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.nomor_kk.SetValue(str(hasil[46]))
            self.nama_kk.SetValue(str(hasil[44])) 
            self.input_alamat.SetValue(str(hasil[16]))
            self.status_miskin.SetValue(str(hasil[12])) 
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()   

    def OnButton3Button(self, event):
        self.Close()
    
    def OnIsipendudukListItemSelected(self, event):
        self.currentItem = event.m_itemIndex # mengambil no index baris yang dipilih 
        b=self.penduduk.GetItem(self.currentItem).GetText() # no index baris dikonversi ke text/ string 
        self.cari_kk.SetValue(b) 
        self.Isi_Object()
        event.Skip()    

    def OnButton2Button(self, event):
        miskin = str(self.status_miskin.GetValue())
        nomorkk = str(self.nomor_kk.GetValue())
        cekraskin = str(self.cek_raskin.GetValue())
        cekjkn = str(self.cek_jkn.GetValue())
        cekblsm = str(self.cek_blsm.GetValue())
        cekbsm = str(self.cek_bsm.GetValue())
        cekpkh = str(self.cek_pkh.GetValue())
        cekpkd = str(self.cek_pkd.GetValue())
        cekppd = str(self.cek_ppd.GetValue())
        cekprolain = str(self.cek_prolain.GetValue())
        sql = "UPDATE penduduk SET kemiskinan = '"+miskin+"', raskin = '"+cekraskin+"', jkn = '"+cekjkn+"', blsm = '"+cekblsm+"', bsm ='"+cekbsm+"', pkh = '"+cekpkh+"', progkesda = '"+cekpkd+"', propeda = '"+cekppd+"', proglain = '"+cekprolain+"'   WHERE no_kk = '"+nomorkk+"'"
        cur.execute(sql)
        db.commit()
        self.nomor_kk.Clear()
        self.nama_kk.Clear() 
        self.input_alamat.Clear()
        self.status_miskin.SetValue('')
        self.cari_kk.Clear()
        self.cek_raskin.SetValue(False)
        self.cek_jkn.SetValue(False)
        self.cek_blsm.SetValue(False)
        self.cek_bsm.SetValue(False)
        self.cek_pkh.SetValue(False)
        self.cek_pkd.SetValue(False)
        self.cek_ppd.SetValue(False)
        self.cek_prolain.SetValue(False)
        self.pesan = wx.MessageDialog(self,"Data Kemiskinan Telah Disimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal() 
        event.Skip()
        
