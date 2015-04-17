#Boa:Frame:Frame1

import wx
import wx.grid
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CHOICE1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1GENBITMAPTEXTBUTTON3, 
 wxID_FRAME1GENBITMAPTEXTBUTTON4, wxID_FRAME1GENBITMAPTEXTBUTTON5, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICLINE1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL10, wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, 
 wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, 
 wxID_FRAME1TEXTCTRL7, wxID_FRAME1TEXTCTRL8, wxID_FRAME1TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(31)]

class Frame1(wx.Frame):

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(255, 191), size=wx.Size(975, 439),
              style=wx.FRAME_NO_TASKBAR, title='Tambh Penduduk')
        self.SetClientSize(wx.Size(975, 439))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Memiliki KK ?', name='staticText1', parent=self,
              pos=wx.Point(24, 16), size=wx.Size(83, 17), style=0)

        self.choice1 = wx.Choice(choices=['Ya', 'Tidak'], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self, pos=wx.Point(132, 16),
              size=wx.Size(100, 27), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Jika "Tidak" Masukan No KK Sementara', name='staticText2',
              parent=self, pos=wx.Point(240, 16), size=wx.Size(248, 17),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(512, 16), size=wx.Size(208, 24),
              style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Jika "Ya" Masukan No KK Disini', name='staticText3',
              parent=self, pos=wx.Point(240, 40), size=wx.Size(190, 17),
              style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(512, 48), size=wx.Size(208, 24),
              style=0, value=u'')

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Cari No KK Sementara',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(744, 8),
              size=wx.Size(176, 32), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Hasil Pencarian KK Sementara', name='staticBox1',
              parent=self, pos=wx.Point(24, 88), size=wx.Size(920, 150),
              style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Hasil Pencarian KK Tetap', name='staticBox2', parent=self,
              pos=wx.Point(24, 240), size=wx.Size(920, 150), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Nomor Kartu Keluarga', name='staticText4', parent=self,
              pos=wx.Point(56, 264), size=wx.Size(142, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Alamat', name='staticText5', parent=self, pos=wx.Point(56,
              296), size=wx.Size(47, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'RT - RW - DUSUN', name='staticText6', parent=self,
              pos=wx.Point(504, 264), size=wx.Size(108, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Nama Kepala Keluarga', name='staticText7', parent=self,
              pos=wx.Point(504, 296), size=wx.Size(145, 17), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(224, 112), size=wx.Size(264, 24),
              style=0, value=u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(224, 144), size=wx.Size(264, 25),
              style=0, value=u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(672, 112), size=wx.Size(256, 25),
              style=0, value=u'')

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(672, 144), size=wx.Size(256, 24),
              style=0, value=u'')

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2,
              label=u'Tambah Anggota Keluarga', name='genBitmapTextButton2',
              parent=self, pos=wx.Point(664, 184), size=wx.Size(264, 31),
              style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(224, 264), size=wx.Size(264, 24),
              style=0, value=u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(224, 296), size=wx.Size(264, 24),
              style=0, value=u'')

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(672, 264), size=wx.Size(256, 25),
              style=0, value='textCtrl5')

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(672, 296),
              size=wx.Size(256, 25), style=0, value='textCtrl5')

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3,
              label=u'Tambah Anggota Keluarga', name='genBitmapTextButton3',
              parent=self, pos=wx.Point(664, 336), size=wx.Size(264, 31),
              style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Nomor KK Sementara', name='staticText8', parent=self,
              pos=wx.Point(64, 112), size=wx.Size(141, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Alamat', name='staticText9', parent=self, pos=wx.Point(64,
              144), size=wx.Size(47, 17), style=0)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'RT - RW - DUSUN', name='staticText10', parent=self,
              pos=wx.Point(504, 112), size=wx.Size(108, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Nama Kepala Keluarga', name='staticText11', parent=self,
              pos=wx.Point(504, 144), size=wx.Size(145, 17), style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(16, 80),
              size=wx.Size(936, 2), style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4,
              label=u'Kembali Ke Menu Utama', name='genBitmapTextButton4',
              parent=self, pos=wx.Point(344, 400), size=wx.Size(264, 31),
              style=0)
        self.genBitmapTextButton4.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton4Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4)

        self.genBitmapTextButton5 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON5, label=u'Cari No KK Tetap',
              name='genBitmapTextButton5', parent=self, pos=wx.Point(744, 48),
              size=wx.Size(176, 32), style=0)

    def __init__(self, parent):
         self._init_ctrls(parent)

    def OnGenBitmapTextButton4Button(self, event):
        self.main=frm_sideka_menu.create(None)
        self.main.Show()
        self.Close()
