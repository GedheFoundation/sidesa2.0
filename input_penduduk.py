#Boa:Frame:login_input_penduduk

import wx
import peringatan
import menu_pilihan_penduduk

def create(parent):
    return login_input_penduduk(parent)

[wxID_LOGIN_INPUT_PENDUDUK, wxID_LOGIN_INPUT_PENDUDUKGARIS_ATAS, 
 wxID_LOGIN_INPUT_PENDUDUKINPUT_PASSWORD, 
 wxID_LOGIN_INPUT_PENDUDUKLABEL_MASUKAN_PASSWORD, 
 wxID_LOGIN_INPUT_PENDUDUKLABEL_PASSWORD, 
 wxID_LOGIN_INPUT_PENDUDUKTOMBOL_KEMBALI_KEMENU, 
 wxID_LOGIN_INPUT_PENDUDUKTOMBOL_LANJUTKAN, 
] = [wx.NewId() for _init_ctrls in range(7)]

class login_input_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LOGIN_INPUT_PENDUDUK,
              name=u'login_input_penduduk', parent=prnt, pos=wx.Point(479, 317),
              size=wx.Size(414, 170), style=wx.DEFAULT_FRAME_STYLE,
              title=u'login')
        self.SetClientSize(wx.Size(412, 145))

        self.label_password = wx.StaticText(id=wxID_LOGIN_INPUT_PENDUDUKLABEL_PASSWORD,
              label=u'Password', name=u'label_password', parent=self,
              pos=wx.Point(16, 56), size=wx.Size(64, 24), style=0)

        self.input_password = wx.TextCtrl(id=wxID_LOGIN_INPUT_PENDUDUKINPUT_PASSWORD,
              name=u'input_password', parent=self, pos=wx.Point(96, 56),
              size=wx.Size(296, 25), style=wx.TE_PASSWORD, value='')

        self.label_masukan_password = wx.StaticText(id=wxID_LOGIN_INPUT_PENDUDUKLABEL_MASUKAN_PASSWORD,
              label=u'MASUKAN PASSWORD DAHULU', name=u'label_masukan_password',
              parent=self, pos=wx.Point(104, 16), size=wx.Size(203, 17),
              style=0)

        self.tombol_lanjutkan = wx.Button(id=wxID_LOGIN_INPUT_PENDUDUKTOMBOL_LANJUTKAN,
              label=u'Lanjutkan', name=u'tombol_lanjutkan', parent=self,
              pos=wx.Point(208, 96), size=wx.Size(184, 30), style=0)
        self.tombol_lanjutkan.SetBitmap(wx.Bitmap(u'/home/gedhe/python-sideka/png/a.png',
              wx.BITMAP_TYPE_PNG))
        self.tombol_lanjutkan.Bind(wx.EVT_BUTTON, self.OnTombol_lanjutkanButton,
              id=wxID_LOGIN_INPUT_PENDUDUKTOMBOL_LANJUTKAN)

        self.tombol_kembali_kemenu = wx.Button(id=wxID_LOGIN_INPUT_PENDUDUKTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(16, 96), size=wx.Size(184, 30),
              style=0)
        self.tombol_kembali_kemenu.SetBitmap(wx.Bitmap(u'/home/gedhe/python-sideka/png/a.png',
              wx.BITMAP_TYPE_PNG))
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_LOGIN_INPUT_PENDUDUKTOMBOL_KEMBALI_KEMENU)

        self.garis_atas = wx.StaticLine(id=wxID_LOGIN_INPUT_PENDUDUKGARIS_ATAS,
              name=u'garis_atas', parent=self, pos=wx.Point(16, 40),
              size=wx.Size(368, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_lanjutkanButton(self, event):
        oneng = 'andri'
        user_password = self.input_password.GetValue()
        if user_password == oneng:
            self.main=menu_pilihan_penduduk.create(None)
            self.main.Show()
            self.Close()
         
        else:
            
            self.main=peringatan.create(None)
            self.main.Show()
            self.Close()

    def OnTombol_kembali_kemenuButton(self, event):
            self.Close()
