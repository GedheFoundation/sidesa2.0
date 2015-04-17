#Boa:Frame:frm_cari_adm

import wx

def create(parent):
    return frm_cari_adm(parent)

[wxID_FRM_CARI_ADM, wxID_FRM_CARI_ADMBUTTON1, wxID_FRM_CARI_ADMBUTTON2, 
 wxID_FRM_CARI_ADMBUTTON3, wxID_FRM_CARI_ADMDATEPICKERCTRL1, 
 wxID_FRM_CARI_ADMDATEPICKERCTRL2, wxID_FRM_CARI_ADMLISTCTRL1, 
 wxID_FRM_CARI_ADMSTATICTEXT1, wxID_FRM_CARI_ADMSTATICTEXT2, 
 wxID_FRM_CARI_ADMSTATICTEXT3, wxID_FRM_CARI_ADMSTATICTEXT4, 
 wxID_FRM_CARI_ADMSTATICTEXT5, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frm_cari_adm(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRM_CARI_ADM, name=u'frm_cari_adm',
              parent=prnt, pos=wx.Point(483, 268), size=wx.Size(732, 278),
              style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Pencarian Data Administrasi')
        self.SetClientSize(wx.Size(732, 278))
        self.Center(wx.BOTH)

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRM_CARI_ADMLISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(712, 144), style=wx.LC_REPORT)

        self.staticText1 = wx.StaticText(id=wxID_FRM_CARI_ADMSTATICTEXT1,
              label=u'Surat Masuk', name='staticText1', parent=self,
              pos=wx.Point(16, 168), size=wx.Size(81, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRM_CARI_ADMSTATICTEXT2,
              label=u'Surat Keluar', name='staticText2', parent=self,
              pos=wx.Point(368, 168), size=wx.Size(79, 15), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRM_CARI_ADMSTATICTEXT3,
              label=u'Tanggal Surat Masuk', name='staticText3', parent=self,
              pos=wx.Point(16, 200), size=wx.Size(133, 15), style=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_FRM_CARI_ADMDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self, pos=wx.Point(168, 200),
              size=wx.Size(96, 26), style=wx.DP_SHOWCENTURY)

        self.button1 = wx.Button(id=wxID_FRM_CARI_ADMBUTTON1, label=u'Cari',
              name='button1', parent=self, pos=wx.Point(272, 200),
              size=wx.Size(85, 24), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRM_CARI_ADMSTATICTEXT4,
              label=u'Tanggal Surat Keluar', name='staticText4', parent=self,
              pos=wx.Point(368, 200), size=wx.Size(131, 15), style=0)

        self.datePickerCtrl2 = wx.DatePickerCtrl(id=wxID_FRM_CARI_ADMDATEPICKERCTRL2,
              name='datePickerCtrl2', parent=self, pos=wx.Point(504, 200),
              size=wx.Size(101, 26), style=wx.DP_SHOWCENTURY)

        self.button2 = wx.Button(id=wxID_FRM_CARI_ADMBUTTON2, label=u'Cari',
              name='button2', parent=self, pos=wx.Point(616, 200),
              size=wx.Size(85, 24), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRM_CARI_ADMSTATICTEXT5,
              label=u'', name='staticText5', parent=self, pos=wx.Point(16, 248),
              size=wx.Size(1, 15), style=0)

        self.button3 = wx.Button(id=wxID_FRM_CARI_ADMBUTTON3,
              label=u'Kembali Ke Menu', name='button3', parent=self,
              pos=wx.Point(288, 240), size=wx.Size(208, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRM_CARI_ADMBUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton3Button(self, event):
        self.Close()
