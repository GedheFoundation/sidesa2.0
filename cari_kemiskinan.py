#Boa:Frame:cari_kemiskinan

import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return cari_kemiskinan(parent)

[wxID_CARI_KEMISKINAN, wxID_CARI_KEMISKINANBUTTON1, 
 wxID_CARI_KEMISKINANBUTTON3, wxID_CARI_KEMISKINANCHECKBOX1, 
 wxID_CARI_KEMISKINANCHECKBOX2, wxID_CARI_KEMISKINANCHECKBOX3, 
 wxID_CARI_KEMISKINANCHECKBOX4, wxID_CARI_KEMISKINANCHECKBOX5, 
 wxID_CARI_KEMISKINANCHECKBOX6, wxID_CARI_KEMISKINANCHECKBOX7, 
 wxID_CARI_KEMISKINANCHECKBOX8, wxID_CARI_KEMISKINANCOMBOBOX1, 
 wxID_CARI_KEMISKINANDATA_KK, wxID_CARI_KEMISKINANSTATICTEXT1, 
 wxID_CARI_KEMISKINANSTATICTEXT2, wxID_CARI_KEMISKINANSTATICTEXT3, 
 wxID_CARI_KEMISKINANSTATICTEXT4, wxID_CARI_KEMISKINANSTATICTEXT5, 
 wxID_CARI_KEMISKINANSTATICTEXT6, wxID_CARI_KEMISKINANTEXTCTRL1, 
 wxID_CARI_KEMISKINANTEXTCTRL2, wxID_CARI_KEMISKINANTEXTCTRL3, 
 wxID_CARI_KEMISKINANTEXTCTRL4, 
] = [wx.NewId() for _init_ctrls in range(23)]

class cari_kemiskinan(wx.Frame):
    def _init_coll_data_kk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama KK', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=160)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_CARI_KEMISKINAN,
              name=u'cari_kemiskinan', parent=prnt, pos=wx.Point(428, 180),
              size=wx.Size(843, 453), style=wx.FRAME_NO_TASKBAR,
              title=u'Pencarian Data Kemiskinan')
        self.SetClientSize(wx.Size(843, 453))
        self.Center(wx.BOTH)

        self.data_kk = wx.ListCtrl(id=wxID_CARI_KEMISKINANDATA_KK,
              name=u'data_kk', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(808, 184), style=wx.LC_REPORT)
        self._init_coll_data_kk_Columns(self.data_kk)

        self.staticText1 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT1,
              label=u'Nomor Kartu Keluarga', name='staticText1', parent=self,
              pos=wx.Point(408, 200), size=wx.Size(145, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_CARI_KEMISKINANTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(560, 200),
              size=wx.Size(168, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_CARI_KEMISKINANBUTTON1, label=u'Cari',
              name='button1', parent=self, pos=wx.Point(744, 200),
              size=wx.Size(80, 24), style=0)

        self.staticText2 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT2,
              label=u'Nomor KK', name='staticText2', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(65, 15), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_CARI_KEMISKINANTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(96, 232),
              size=wx.Size(312, 25), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self,
              pos=wx.Point(416, 232), size=wx.Size(47, 15), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_CARI_KEMISKINANTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(472, 232),
              size=wx.Size(352, 25), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT4,
              label=u'Nama KK', name='staticText4', parent=self,
              pos=wx.Point(16, 264), size=wx.Size(60, 15), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_CARI_KEMISKINANTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(96, 264),
              size=wx.Size(312, 25), style=0, value='')

        self.staticText5 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT5,
              label=u'Status Kemiskinan', name='staticText5', parent=self,
              pos=wx.Point(416, 264), size=wx.Size(119, 15), style=0)

        self.comboBox1 = wx.ComboBox(choices=['Miskin', 'Tidak Miskin'],
              id=wxID_CARI_KEMISKINANCOMBOBOX1, name='comboBox1', parent=self,
              pos=wx.Point(552, 264), size=wx.Size(272, 25), style=0, value='')

        self.staticText6 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT6,
              label=u'Program Perlindungan Sosial', name='staticText6',
              parent=self, pos=wx.Point(16, 296), size=wx.Size(185, 15),
              style=0)

        self.checkBox1 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX1,
              label=u'Raskin', name='checkBox1', parent=self, pos=wx.Point(16,
              320), size=wx.Size(89, 18), style=0)
        self.checkBox1.SetValue(False)

        self.checkBox2 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX2,
              label=u'JKN', name='checkBox2', parent=self, pos=wx.Point(16,
              344), size=wx.Size(89, 18), style=0)
        self.checkBox2.SetValue(False)

        self.checkBox3 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX3,
              label=u'BLSM', name='checkBox3', parent=self, pos=wx.Point(16,
              368), size=wx.Size(89, 18), style=0)
        self.checkBox3.SetValue(False)

        self.checkBox4 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX4,
              label=u'BSM', name='checkBox4', parent=self, pos=wx.Point(192,
              320), size=wx.Size(89, 18), style=0)
        self.checkBox4.SetValue(False)

        self.checkBox5 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX5,
              label=u'PKH', name='checkBox5', parent=self, pos=wx.Point(192,
              344), size=wx.Size(89, 18), style=0)
        self.checkBox5.SetValue(False)

        self.checkBox6 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX6,
              label=u'Program Kesehatan Daerah', name='checkBox6', parent=self,
              pos=wx.Point(192, 368), size=wx.Size(208, 18), style=0)
        self.checkBox6.SetValue(False)

        self.checkBox7 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX7,
              label=u'Program Pendidikan Daerah', name='checkBox7', parent=self,
              pos=wx.Point(416, 320), size=wx.Size(208, 18), style=0)
        self.checkBox7.SetValue(False)

        self.checkBox8 = wx.CheckBox(id=wxID_CARI_KEMISKINANCHECKBOX8,
              label=u'Program Lain', name='checkBox8', parent=self,
              pos=wx.Point(416, 344), size=wx.Size(200, 18), style=0)
        self.checkBox8.SetValue(False)

        self.button3 = wx.Button(id=wxID_CARI_KEMISKINANBUTTON3,
              label=u'Kembali Ke Menu', name='button3', parent=self,
              pos=wx.Point(320, 408), size=wx.Size(184, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_CARI_KEMISKINANBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton3Button(self, event):
        self.Close()
