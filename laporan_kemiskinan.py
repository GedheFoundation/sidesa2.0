#Boa:Frame:laporan_kemiskinan

import wx
import wx.lib.buttons

def create(parent):
    return laporan_kemiskinan(parent)

[wxID_LAPORAN_KEMISKINAN, wxID_LAPORAN_KEMISKINANBUTTON1, 
 wxID_LAPORAN_KEMISKINANBUTTON2, wxID_LAPORAN_KEMISKINANGENBUTTON1, 
 wxID_LAPORAN_KEMISKINANGENBUTTON10, wxID_LAPORAN_KEMISKINANGENBUTTON11, 
 wxID_LAPORAN_KEMISKINANGENBUTTON12, wxID_LAPORAN_KEMISKINANGENBUTTON13, 
 wxID_LAPORAN_KEMISKINANGENBUTTON14, wxID_LAPORAN_KEMISKINANGENBUTTON15, 
 wxID_LAPORAN_KEMISKINANGENBUTTON16, wxID_LAPORAN_KEMISKINANGENBUTTON17, 
 wxID_LAPORAN_KEMISKINANGENBUTTON18, wxID_LAPORAN_KEMISKINANGENBUTTON19, 
 wxID_LAPORAN_KEMISKINANGENBUTTON2, wxID_LAPORAN_KEMISKINANGENBUTTON20, 
 wxID_LAPORAN_KEMISKINANGENBUTTON3, wxID_LAPORAN_KEMISKINANGENBUTTON4, 
 wxID_LAPORAN_KEMISKINANGENBUTTON5, wxID_LAPORAN_KEMISKINANGENBUTTON6, 
 wxID_LAPORAN_KEMISKINANGENBUTTON7, wxID_LAPORAN_KEMISKINANGENBUTTON8, 
 wxID_LAPORAN_KEMISKINANGENBUTTON9, wxID_LAPORAN_KEMISKINANLAPORAN, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT1, wxID_LAPORAN_KEMISKINANSTATICTEXT10, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT11, wxID_LAPORAN_KEMISKINANSTATICTEXT2, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT3, wxID_LAPORAN_KEMISKINANSTATICTEXT4, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT5, wxID_LAPORAN_KEMISKINANSTATICTEXT6, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT7, wxID_LAPORAN_KEMISKINANSTATICTEXT8, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT9, wxID_LAPORAN_KEMISKINANTEXTCTRL1, 
 wxID_LAPORAN_KEMISKINANTEXTCTRL10, wxID_LAPORAN_KEMISKINANTEXTCTRL2, 
 wxID_LAPORAN_KEMISKINANTEXTCTRL3, wxID_LAPORAN_KEMISKINANTEXTCTRL4, 
 wxID_LAPORAN_KEMISKINANTEXTCTRL5, wxID_LAPORAN_KEMISKINANTEXTCTRL6, 
 wxID_LAPORAN_KEMISKINANTEXTCTRL7, wxID_LAPORAN_KEMISKINANTEXTCTRL8, 
 wxID_LAPORAN_KEMISKINANTEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(45)]

class laporan_kemiskinan(wx.Frame):
    def _init_coll_laporan_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama KK', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=160)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Status Kemiskinan', width=160)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_KEMISKINAN,
              name=u'laporan_kemiskinan', parent=prnt, pos=wx.Point(393, 134),
              size=wx.Size(911, 545), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Data Kemiskinan')
        self.SetClientSize(wx.Size(911, 545))
        self.Center(wx.BOTH)

        self.laporan = wx.ListCtrl(id=wxID_LAPORAN_KEMISKINANLAPORAN,
              name=u'laporan', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(896, 256), style=wx.LC_REPORT)
        self._init_coll_laporan_Columns(self.laporan)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT1,
              label=u'Jumlah Keluarga Miskin ', name='staticText1', parent=self,
              pos=wx.Point(8, 280), size=wx.Size(150, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT2,
              label=u'Jumlah Keluarga Tidak Miskin', name='staticText2',
              parent=self, pos=wx.Point(8, 312), size=wx.Size(183, 15),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT3,
              label=u'Program Perlindungan Sosial', name='staticText3',
              parent=self, pos=wx.Point(8, 344), size=wx.Size(185, 15),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(296, 280),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(296, 312),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(136, 368),
              size=wx.Size(80, 25), style=0, value='')

        self.genButton1 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON1,
              label=u'Lihat Laporan', name='genButton1', parent=self,
              pos=wx.Point(392, 280), size=wx.Size(136, 24), style=0)

        self.genButton2 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON2,
              label=u'Lihat Laporan', name='genButton2', parent=self,
              pos=wx.Point(392, 312), size=wx.Size(136, 24), style=0)

        self.genButton3 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON3,
              label=u'Cetak Laporan', name='genButton3', parent=self,
              pos=wx.Point(544, 280), size=wx.Size(136, 24), style=0)

        self.genButton4 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON4,
              label=u'Lihat Laporan', name='genButton4', parent=self,
              pos=wx.Point(544, 312), size=wx.Size(136, 24), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(136, 400),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl5 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(136, 432),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl6 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(136, 464),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl7 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL7,
              name='textCtrl7', parent=self, pos=wx.Point(600, 368),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl8 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL8,
              name='textCtrl8', parent=self, pos=wx.Point(600, 400),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl9 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL9,
              name='textCtrl9', parent=self, pos=wx.Point(600, 432),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl10 = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(600, 464),
              size=wx.Size(80, 25), style=0, value='')

        self.genButton5 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON5,
              label=u'Lihat Laporan', name='genButton5', parent=self,
              pos=wx.Point(224, 368), size=wx.Size(136, 24), style=0)

        self.genButton6 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON6,
              label=u'Lihat Laporan', name='genButton6', parent=self,
              pos=wx.Point(224, 400), size=wx.Size(136, 24), style=0)

        self.genButton7 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON7,
              label=u'Lihat Laporan', name='genButton7', parent=self,
              pos=wx.Point(224, 432), size=wx.Size(136, 24), style=0)

        self.genButton8 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON8,
              label=u'Lihat Laporan', name='genButton8', parent=self,
              pos=wx.Point(224, 464), size=wx.Size(136, 24), style=0)

        self.genButton9 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON9,
              label=u'Lihat Laporan', name='genButton9', parent=self,
              pos=wx.Point(688, 368), size=wx.Size(136, 24), style=0)

        self.genButton10 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON10,
              label=u'Lihat Laporan', name='genButton10', parent=self,
              pos=wx.Point(688, 400), size=wx.Size(136, 24), style=0)

        self.genButton11 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON11,
              label=u'Lihat Laporan', name='genButton11', parent=self,
              pos=wx.Point(688, 432), size=wx.Size(136, 24), style=0)

        self.genButton12 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON12,
              label=u'Lihat Laporan', name='genButton12', parent=self,
              pos=wx.Point(688, 464), size=wx.Size(136, 24), style=0)

        self.genButton13 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON13,
              label=u'Cetak', name='genButton13', parent=self, pos=wx.Point(368,
              368), size=wx.Size(50, 24), style=0)

        self.genButton14 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON14,
              label=u'Cetak', name='genButton14', parent=self, pos=wx.Point(368,
              400), size=wx.Size(50, 24), style=0)

        self.genButton15 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON15,
              label=u'Cetak', name='genButton15', parent=self, pos=wx.Point(368,
              432), size=wx.Size(50, 24), style=0)

        self.genButton16 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON16,
              label=u'Cetak', name='genButton16', parent=self, pos=wx.Point(368,
              464), size=wx.Size(50, 24), style=0)

        self.genButton17 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON17,
              label=u'Cetak', name='genButton17', parent=self, pos=wx.Point(832,
              368), size=wx.Size(50, 24), style=0)

        self.genButton18 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON18,
              label=u'Cetak', name='genButton18', parent=self, pos=wx.Point(832,
              400), size=wx.Size(50, 24), style=0)

        self.genButton19 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON19,
              label=u'Cetak', name='genButton19', parent=self, pos=wx.Point(832,
              432), size=wx.Size(50, 24), style=0)

        self.genButton20 = wx.lib.buttons.GenButton(id=wxID_LAPORAN_KEMISKINANGENBUTTON20,
              label=u'Cetak', name='genButton20', parent=self, pos=wx.Point(832,
              464), size=wx.Size(50, 24), style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT4,
              label=u'1.  Raskin', name='staticText4', parent=self,
              pos=wx.Point(8, 368), size=wx.Size(62, 15), style=0)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT5,
              label=u'2.  JKN', name='staticText5', parent=self, pos=wx.Point(8,
              400), size=wx.Size(42, 15), style=0)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT6,
              label=u'3.  BLSM', name='staticText6', parent=self,
              pos=wx.Point(8, 432), size=wx.Size(57, 15), style=0)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT7,
              label=u'4.  BSM', name='staticText7', parent=self, pos=wx.Point(8,
              464), size=wx.Size(50, 15), style=0)

        self.staticText8 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT8,
              label=u'5.  PKH', name='staticText8', parent=self,
              pos=wx.Point(432, 368), size=wx.Size(47, 15), style=0)

        self.staticText9 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT9,
              label=u'6.  Prog Kes Daerah', name='staticText9', parent=self,
              pos=wx.Point(432, 400), size=wx.Size(127, 15), style=0)

        self.staticText10 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT10,
              label=u'7. Prog Pend Daerah', name='staticText10', parent=self,
              pos=wx.Point(432, 432), size=wx.Size(133, 15), style=0)

        self.staticText11 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT11,
              label=u'8.  Program Lain', name='staticText11', parent=self,
              pos=wx.Point(432, 464), size=wx.Size(106, 15), style=0)

        self.button1 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON1,
              label=u'Cetak Laporan Keseluruhan', name='button1', parent=self,
              pos=wx.Point(280, 504), size=wx.Size(184, 30), style=0)

        self.button2 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON2,
              label=u'Kembali Ke Menu', name='button2', parent=self,
              pos=wx.Point(480, 504), size=wx.Size(200, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        self.Close()
