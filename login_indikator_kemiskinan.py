#Boa:Dialog:otentifikasi_indikator_kemiskinan

import wx
import peringatan
import input_indikator_kemiskinan
import sqlite3

def connect():
    db = sqlite3.connect('/opt/sidesa/sidesa')
    return db
    db.close()



def create(parent):
    return otentifikasi_indikator_kemiskinan(parent)

[wxID_OTENTIFIKASI_INDIKATOR_KEMISKINAN, 
 wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANINPUT_PASSWORD, 
 wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANLABEL_MASUKAN_PASSWORD, 
 wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANLABEL_PASSWORD, 
 wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_KEMBALI_KEMENU, 
 wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_LANJUTKAN, 
] = [wx.NewId() for _init_ctrls in range(6)]

class otentifikasi_indikator_kemiskinan(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINAN,
              name=u'otentifikasi_indikator_kemiskinan', parent=prnt,
              pos=wx.Point(482, 327), size=wx.Size(402, 140), style=wx.CAPTION,
              title=u'Otentifikasi Input Indikator Kemiskinan')
        self.SetClientSize(wx.Size(402, 140))
        self.Center(wx.BOTH)

        self.label_password = wx.StaticText(id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANLABEL_PASSWORD,
              label=u'Password', name=u'label_password', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(64, 24), style=0)

        self.input_password = wx.TextCtrl(id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANINPUT_PASSWORD,
              name=u'input_password', parent=self, pos=wx.Point(96, 56),
              size=wx.Size(296, 25), style=wx.TE_PASSWORD, value='')

        self.label_masukan_password = wx.StaticText(id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANLABEL_MASUKAN_PASSWORD,
              label=u'MASUKAN PASSWORD DAHULU', name=u'label_masukan_password',
              parent=self, pos=wx.Point(104, 16), size=wx.Size(203, 17),
              style=0)

        self.tombol_lanjutkan = wx.Button(id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_LANJUTKAN,
              label=u'Lanjutkan', name=u'tombol_lanjutkan', parent=self,
              pos=wx.Point(208, 96), size=wx.Size(184, 30), style=0)
        self.tombol_lanjutkan.Bind(wx.EVT_BUTTON, self.OnTombol_lanjutkanButton,
              id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_LANJUTKAN)

        self.tombol_kembali_kemenu = wx.Button(id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(16, 96), size=wx.Size(184, 30),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_OTENTIFIKASI_INDIKATOR_KEMISKINANTOMBOL_KEMBALI_KEMENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_lanjutkanButton(self, event):
        user_password=str(self.input_password.GetValue())
        db = connect()
        cursor = db.cursor()
        isinya = "SELECT * FROM password WHERE nama='admin'"
        cursor.execute(isinya)
        kunci = cursor.fetchone()[1]
        if kunci == user_password :
            
            self.main=input_indikator_kemiskinan.create(None)
            self.main.Show()
            self.Close()
         
       
        else:
            self.Close()
            self.main=peringatan.create(None)
            self.main.Show()

    def OnTombol_kembali_kemenuButton(self, event):
        self.Close()
