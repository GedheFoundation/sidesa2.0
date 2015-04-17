#Boa:Frame:edit_surat
import wx
import wx.lib.buttons
import edit_surat_keluar
import edir_surat_masuk


def create(parent):
    return edit_surat(parent)

[wxID_EDIT_SURAT, wxID_EDIT_SURATSTATICLINE1, 
 wxID_EDIT_SURATTOMBOL_INPUT_SURAT, wxID_EDIT_SURATTOMBOL_KEMBALI_KE_MENU, 
 wxID_EDIT_SURATTOMBOL_SURAT_KELUAR, 
] = [wx.NewId() for _init_ctrls in range(5)]

class edit_surat(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_SURAT, name=u'edit_surat',
              parent=prnt, pos=wx.Point(606, 380), size=wx.Size(417, 102),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Administrasi Edit Persuratan')
        self.SetClientSize(wx.Size(417, 102))
        self.Center(wx.BOTH)

        self.tombol_input_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_SURATTOMBOL_INPUT_SURAT, label=u'Edit Surat Masuk',
              name=u'tombol_input_surat', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(184, 31), style=0)
        self.tombol_input_surat.Bind(wx.EVT_BUTTON,
              self.OnTombol_input_suratButton,
              id=wxID_EDIT_SURATTOMBOL_INPUT_SURAT)

        self.tombol_surat_keluar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_SURATTOMBOL_SURAT_KELUAR, label=u'Edit Surat Keluar',
              name=u'tombol_surat_keluar', parent=self, pos=wx.Point(216, 16),
              size=wx.Size(184, 31), style=0)
        self.tombol_surat_keluar.Bind(wx.EVT_BUTTON,
              self.OnTombol_surat_keluarButton,
              id=wxID_EDIT_SURATTOMBOL_SURAT_KELUAR)

        self.tombol_kembali_ke_menu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_SURATTOMBOL_KEMBALI_KE_MENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_ke_menu',
              parent=self, pos=wx.Point(128, 64), size=wx.Size(184, 31),
              style=0)
        self.tombol_kembali_ke_menu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_ke_menuButton,
              id=wxID_EDIT_SURATTOMBOL_KEMBALI_KE_MENU)

        self.staticLine1 = wx.StaticLine(id=wxID_EDIT_SURATSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(8, 56),
              size=wx.Size(400, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

        
    def OnTombol_kembali_ke_menuButton(self, event):
        self.Close()
        

    def OnTombol_surat_keluarButton(self, event):
        self.Close()
        self.main=edit_surat_keluar.create(None)
        self.main.Show()

    def OnTombol_input_suratButton(self, event):
        self.Close()
        self.main=edir_surat_masuk.create(None)
        self.main.Show()


