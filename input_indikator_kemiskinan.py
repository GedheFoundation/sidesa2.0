#Boa:Frame:indikator

import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return indikator(parent)

[wxID_INDIKATOR, wxID_INDIKATORGENBITMAPTEXTBUTTON1, 
 wxID_INDIKATORINPUT_INDIKATOR1, wxID_INDIKATORINPUT_INDIKATOR2, 
 wxID_INDIKATORINPUT_INDIKATOR3, wxID_INDIKATORINPUT_INDIKATOR4, 
 wxID_INDIKATORINPUT_INDIKATOR5, wxID_INDIKATORINPUT_INDIKATOR6, 
 wxID_INDIKATORINPUT_INDIKATOR7, wxID_INDIKATORINPUT_INDIKATOR8, 
 wxID_INDIKATORINPUT_INDIKATOR9, wxID_INDIKATORSTATICTEXT1, 
 wxID_INDIKATORSTATICTEXT10, wxID_INDIKATORSTATICTEXT11, 
 wxID_INDIKATORSTATICTEXT12, wxID_INDIKATORSTATICTEXT2, 
 wxID_INDIKATORSTATICTEXT3, wxID_INDIKATORSTATICTEXT4, 
 wxID_INDIKATORSTATICTEXT5, wxID_INDIKATORSTATICTEXT6, 
 wxID_INDIKATORSTATICTEXT7, wxID_INDIKATORSTATICTEXT8, 
 wxID_INDIKATORSTATICTEXT9, wxID_INDIKATORTEXTCTRL1, wxID_INDIKATORTEXTCTRL2, 
 wxID_INDIKATORTEXTCTRL3, wxID_INDIKATORTOMBOL_KEMBALI_KEMENU, 
 wxID_INDIKATORTOMBOL_SIMPAN_DATA, 
] = [wx.NewId() for _init_ctrls in range(28)]

class indikator(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_INDIKATOR, name=u'indikator',
              parent=prnt, pos=wx.Point(321, 270), size=wx.Size(927, 445),
              style=wx.FRAME_NO_TASKBAR, title=u'Input Indikator Kemiskinan')
        self.SetClientSize(wx.Size(927, 445))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(32,
              16), size=wx.Size(12, 17), style=0)

        self.input_indikator1 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR1,
              name=u'input_indikator1', parent=self, pos=wx.Point(56, 16),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT2,
              label=u'2.', name='staticText2', parent=self, pos=wx.Point(32,
              48), size=wx.Size(12, 17), style=0)

        self.input_indikator2 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR2,
              name=u'input_indikator2', parent=self, pos=wx.Point(56, 48),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT3,
              label=u'3.', name='staticText3', parent=self, pos=wx.Point(32,
              80), size=wx.Size(12, 17), style=0)

        self.input_indikator3 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR3,
              name=u'input_indikator3', parent=self, pos=wx.Point(56, 80),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT4,
              label=u'4.', name='staticText4', parent=self, pos=wx.Point(32,
              112), size=wx.Size(12, 17), style=0)

        self.input_indikator4 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR4,
              name=u'input_indikator4', parent=self, pos=wx.Point(56, 112),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT5,
              label=u'5.', name='staticText5', parent=self, pos=wx.Point(32,
              144), size=wx.Size(12, 17), style=0)

        self.input_indikator5 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR5,
              name=u'input_indikator5', parent=self, pos=wx.Point(56, 144),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT6,
              label=u'6.', name='staticText6', parent=self, pos=wx.Point(32,
              176), size=wx.Size(12, 17), style=0)

        self.input_indikator6 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR6,
              name=u'input_indikator6', parent=self, pos=wx.Point(56, 176),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT7,
              label=u'7.', name='staticText7', parent=self, pos=wx.Point(32,
              208), size=wx.Size(12, 17), style=0)

        self.input_indikator7 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR7,
              name=u'input_indikator7', parent=self, pos=wx.Point(56, 208),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText8 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT8,
              label=u'8.', name='staticText8', parent=self, pos=wx.Point(32,
              240), size=wx.Size(12, 17), style=0)

        self.input_indikator8 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR8,
              name=u'input_indikator8', parent=self, pos=wx.Point(56, 240),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText9 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT9,
              label=u'9.', name='staticText9', parent=self, pos=wx.Point(32,
              272), size=wx.Size(12, 17), style=0)

        self.input_indikator9 = wx.TextCtrl(id=wxID_INDIKATORINPUT_INDIKATOR9,
              name=u'input_indikator9', parent=self, pos=wx.Point(56, 272),
              size=wx.Size(840, 25), style=0, value=u'')

        self.tombol_simpan_data = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_INDIKATORTOMBOL_SIMPAN_DATA, label=u'Update',
              name=u'tombol_simpan_data', parent=self, pos=wx.Point(328, 408),
              size=wx.Size(184, 31), style=0)
        self.tombol_simpan_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_simpan_dataButton,
              id=wxID_INDIKATORTOMBOL_SIMPAN_DATA)

        self.tombol_kembali_kemenu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_INDIKATORTOMBOL_KEMBALI_KEMENU, label=u'Kembali Ke Menu',
              name=u'tombol_kembali_kemenu', parent=self, pos=wx.Point(528,
              408), size=wx.Size(176, 31), style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_INDIKATORTOMBOL_KEMBALI_KEMENU)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_INDIKATORGENBITMAPTEXTBUTTON1, label=u'Simpan',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(176, 408),
              size=wx.Size(144, 31), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_INDIKATORTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(56, 304),
              size=wx.Size(840, 25), style=0, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_INDIKATORTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(56, 336),
              size=wx.Size(840, 25), style=0, value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_INDIKATORTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(56, 368),
              size=wx.Size(840, 25), style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT10,
              label=u'10.', name='staticText10', parent=self, pos=wx.Point(24,
              304), size=wx.Size(21, 15), style=0)

        self.staticText11 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT11,
              label=u'11.', name='staticText11', parent=self, pos=wx.Point(24,
              336), size=wx.Size(21, 15), style=0)

        self.staticText12 = wx.StaticText(id=wxID_INDIKATORSTATICTEXT12,
              label=u'12.', name='staticText12', parent=self, pos=wx.Point(24,
              368), size=wx.Size(21, 15), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_simpan_dataButton(self, event):
        event.Skip()

    def OnTombol_kembali_kemenuButton(self, event):
        self.Close()
