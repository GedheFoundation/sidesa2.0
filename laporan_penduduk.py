#Boa:Frame:laporan_penduduk

import wx

def create(parent):
    return laporan_penduduk(parent)

[wxID_LAPORAN_PENDUDUK, wxID_LAPORAN_PENDUDUKBUTTON1, 
 wxID_LAPORAN_PENDUDUKBUTTON10, wxID_LAPORAN_PENDUDUKBUTTON11, 
 wxID_LAPORAN_PENDUDUKBUTTON12, wxID_LAPORAN_PENDUDUKBUTTON13, 
 wxID_LAPORAN_PENDUDUKBUTTON14, wxID_LAPORAN_PENDUDUKBUTTON15, 
 wxID_LAPORAN_PENDUDUKBUTTON2, wxID_LAPORAN_PENDUDUKBUTTON3, 
 wxID_LAPORAN_PENDUDUKBUTTON4, wxID_LAPORAN_PENDUDUKBUTTON5, 
 wxID_LAPORAN_PENDUDUKBUTTON6, wxID_LAPORAN_PENDUDUKBUTTON7, 
 wxID_LAPORAN_PENDUDUKBUTTON8, wxID_LAPORAN_PENDUDUKBUTTON9, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX1, wxID_LAPORAN_PENDUDUKCOMBOBOX2, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX3, wxID_LAPORAN_PENDUDUKCOMBOBOX4, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX5, wxID_LAPORAN_PENDUDUKCOMBOBOX6, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX7, wxID_LAPORAN_PENDUDUKCOMBOBOX8, 
 wxID_LAPORAN_PENDUDUKPENDUDUK, wxID_LAPORAN_PENDUDUKSTATICTEXT1, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT10, wxID_LAPORAN_PENDUDUKSTATICTEXT11, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT12, wxID_LAPORAN_PENDUDUKSTATICTEXT13, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT14, wxID_LAPORAN_PENDUDUKSTATICTEXT2, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT3, wxID_LAPORAN_PENDUDUKSTATICTEXT4, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT5, wxID_LAPORAN_PENDUDUKSTATICTEXT6, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT7, wxID_LAPORAN_PENDUDUKSTATICTEXT8, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT9, wxID_LAPORAN_PENDUDUKTEXTCTRL1, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL10, wxID_LAPORAN_PENDUDUKTEXTCTRL11, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL12, wxID_LAPORAN_PENDUDUKTEXTCTRL13, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL14, wxID_LAPORAN_PENDUDUKTEXTCTRL2, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL3, wxID_LAPORAN_PENDUDUKTEXTCTRL4, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL5, wxID_LAPORAN_PENDUDUKTEXTCTRL6, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL7, wxID_LAPORAN_PENDUDUKTEXTCTRL8, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(53)]

class laporan_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_PENDUDUK,
              name=u'laporan_penduduk', parent=prnt, pos=wx.Point(313, 177),
              size=wx.Size(928, 491), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Penduduk')
        self.SetClientSize(wx.Size(928, 491))
        self.Center(wx.BOTH)

        self.penduduk = wx.ListCtrl(id=wxID_LAPORAN_PENDUDUKPENDUDUK,
              name=u'penduduk', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(912, 160), style=wx.LC_ICON)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT1,
              label=u'Jumlah Keluarga KK Sementara', name='staticText1',
              parent=self, pos=wx.Point(16, 192), size=wx.Size(199, 15),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT2,
              label=u'Jumlah Keluarga KK Tetap', name='staticText2',
              parent=self, pos=wx.Point(16, 224), size=wx.Size(161, 15),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT3,
              label=u'Jumlah Penduduk Laki - Laki', name='staticText3',
              parent=self, pos=wx.Point(16, 256), size=wx.Size(178, 15),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT4,
              label=u'Jumlah Penduduk Perempuan', name='staticText4',
              parent=self, pos=wx.Point(16, 288), size=wx.Size(189, 15),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(248, 184),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(248, 216),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(248, 248),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl4 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(248, 280),
              size=wx.Size(80, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON1,
              label=u'Lihat Data', name='button1', parent=self,
              pos=wx.Point(336, 216), size=wx.Size(96, 24), style=0)

        self.button2 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON2,
              label=u'Lihat Data', name='button2', parent=self,
              pos=wx.Point(336, 248), size=wx.Size(96, 24), style=0)

        self.button3 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON3,
              label=u'Lihat Data', name='button3', parent=self,
              pos=wx.Point(816, 312), size=wx.Size(96, 24), style=0)

        self.button4 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON4,
              label=u'Lihat Data', name='button4', parent=self,
              pos=wx.Point(816, 184), size=wx.Size(96, 24), style=0)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT5,
              label=u'Jumlah Pend. Perempuan Produktif', name='staticText5',
              parent=self, pos=wx.Point(16, 352), size=wx.Size(222, 15),
              style=0)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT6,
              label=u'Jumlah Pend. Laki-laki Produktif', name='staticText6',
              parent=self, pos=wx.Point(16, 320), size=wx.Size(208, 15),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT7,
              label=u'Jumlah Pendidikan Akhir', name='staticText7', parent=self,
              pos=wx.Point(448, 192), size=wx.Size(153, 15), style=0)

        self.comboBox1 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX1, name='comboBox1', parent=self,
              pos=wx.Point(624, 184), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl5 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(728, 184),
              size=wx.Size(80, 25), style=0, value='')

        self.staticText8 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT8,
              label=u'Jumlah Saat Ini Pendidikan', name='staticText8',
              parent=self, pos=wx.Point(448, 224), size=wx.Size(169, 15),
              style=0)

        self.comboBox2 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX2, name='comboBox2', parent=self,
              pos=wx.Point(624, 216), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl6 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(728, 216),
              size=wx.Size(80, 25), style=0, value='')

        self.staticText9 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT9,
              label=u'Status Perkawinan', name='staticText9', parent=self,
              pos=wx.Point(448, 288), size=wx.Size(119, 15), style=0)

        self.comboBox3 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX3, name='comboBox3', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(96, 25), style=0, value='')

        self.button5 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON5,
              label=u'Lihat Data', name='button5', parent=self,
              pos=wx.Point(816, 216), size=wx.Size(96, 24), style=0)

        self.button6 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON6,
              label=u'Lihat Data', name='button6', parent=self,
              pos=wx.Point(336, 184), size=wx.Size(96, 24), style=0)

        self.staticText10 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT10,
              label=u'Difabelitas', name='staticText10', parent=self,
              pos=wx.Point(448, 320), size=wx.Size(68, 15), style=0)

        self.comboBox4 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX4, name='comboBox4', parent=self,
              pos=wx.Point(624, 280), size=wx.Size(96, 25), style=0, value='')

        self.staticText11 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT11,
              label=u'Status Tinggal', name='staticText11', parent=self,
              pos=wx.Point(448, 352), size=wx.Size(92, 15), style=0)

        self.comboBox5 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX5, name='comboBox5', parent=self,
              pos=wx.Point(624, 312), size=wx.Size(96, 25), style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT12,
              label=u'Pekerjaan', name='staticText12', parent=self,
              pos=wx.Point(448, 256), size=wx.Size(64, 15), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL7,
              name='textCtrl7', parent=self, pos=wx.Point(248, 312),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl8 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL8,
              name='textCtrl8', parent=self, pos=wx.Point(248, 344),
              size=wx.Size(80, 25), style=0, value='')

        self.staticText13 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT13,
              label=u'Status Penduduk', name='staticText13', parent=self,
              pos=wx.Point(448, 384), size=wx.Size(110, 15), style=0)

        self.comboBox6 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX6, name='comboBox6', parent=self,
              pos=wx.Point(624, 344), size=wx.Size(96, 25), style=0, value='')

        self.comboBox7 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX7, name='comboBox7', parent=self,
              pos=wx.Point(624, 376), size=wx.Size(96, 25), style=0, value='')

        self.staticText14 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT14,
              label=u'Resiko Kehamilan', name='staticText14', parent=self,
              pos=wx.Point(448, 416), size=wx.Size(111, 15), style=0)

        self.comboBox8 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX8, name='comboBox8', parent=self,
              pos=wx.Point(624, 408), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl9 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL9,
              name='textCtrl9', parent=self, pos=wx.Point(728, 248),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl10 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(728, 280),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl11 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL11,
              name='textCtrl11', parent=self, pos=wx.Point(728, 312),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl12 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL12,
              name='textCtrl12', parent=self, pos=wx.Point(728, 344),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl13 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL13,
              name='textCtrl13', parent=self, pos=wx.Point(728, 376),
              size=wx.Size(80, 25), style=0, value='')

        self.textCtrl14 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL14,
              name='textCtrl14', parent=self, pos=wx.Point(728, 408),
              size=wx.Size(80, 25), style=0, value='')

        self.button7 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON7,
              label=u'Lihat Data', name='button7', parent=self,
              pos=wx.Point(336, 344), size=wx.Size(96, 24), style=0)

        self.button8 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON8,
              label=u'Lihat Data', name='button8', parent=self,
              pos=wx.Point(816, 248), size=wx.Size(96, 24), style=0)

        self.button9 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON9,
              label=u'Lihat Data', name='button9', parent=self,
              pos=wx.Point(816, 280), size=wx.Size(96, 24), style=0)

        self.button10 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON10,
              label=u'Lihat Data', name='button10', parent=self,
              pos=wx.Point(336, 312), size=wx.Size(96, 24), style=0)

        self.button11 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON11,
              label=u'Lihat Data', name='button11', parent=self,
              pos=wx.Point(816, 344), size=wx.Size(96, 24), style=0)

        self.button12 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON12,
              label=u'Lihat Data', name='button12', parent=self,
              pos=wx.Point(816, 376), size=wx.Size(96, 24), style=0)

        self.button13 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON13,
              label=u'Lihat Data', name='button13', parent=self,
              pos=wx.Point(816, 408), size=wx.Size(96, 24), style=0)

        self.button14 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON14,
              label=u'Lihat Data', name='button14', parent=self,
              pos=wx.Point(336, 280), size=wx.Size(96, 24), style=0)

        self.button15 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON15,
              label=u'Kembali Ke Menu', name='button15', parent=self,
              pos=wx.Point(360, 448), size=wx.Size(224, 30), style=0)
        self.button15.Bind(wx.EVT_BUTTON, self.OnButton15Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON15)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton15Button(self, event):
        self.Close()
