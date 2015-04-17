#Boa:Frame:data_statistik

import wx
import wx.lib.buttons

def create(parent):
    return data_statistik(parent)

[wxID_DATA_STATISTIK, wxID_DATA_STATISTIKLABEL_STATISTIKA_KEMISKINAN, 
 wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA, 
 wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU, wxID_DATA_STATISTIKTOMBOL_PROG, 
] = [wx.NewId() for _init_ctrls in range(5)]

class data_statistik(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_DATA_STATISTIK, name=u'data_statistik',
              parent=prnt, pos=wx.Point(530, 312), size=wx.Size(306, 173),
              style=wx.FRAME_NO_TASKBAR, title=u'Data Statistik Kemiskinan')
        self.SetClientSize(wx.Size(306, 173))
        self.Center(wx.BOTH)

        self.label_statistika_kemiskinan = wx.StaticBox(id=wxID_DATA_STATISTIKLABEL_STATISTIKA_KEMISKINAN,
              label=u'Statistik Kemiskinan',
              name=u'label_statistika_kemiskinan', parent=self, pos=wx.Point(16,
              16), size=wx.Size(272, 105), style=0)

        self.tombol_data_miskin_desa = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA,
              label=u'Data Miskin Desa', name=u'tombol_data_miskin_desa',
              parent=self, pos=wx.Point(32, 40), size=wx.Size(240, 31),
              style=0)
        self.tombol_data_miskin_desa.Bind(wx.EVT_BUTTON,
              self.OnTombol_data_miskin_desaButton,
              id=wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA)

        self.tombol_prog = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_PROG,
              label=u'Perbandingan Prog. Perlindungan', name=u'tombol_prog',
              parent=self, pos=wx.Point(32, 80), size=wx.Size(240, 31),
              style=0)
        self.tombol_prog.Bind(wx.EVT_BUTTON, self.OnTombol_progButton,
              id=wxID_DATA_STATISTIKTOMBOL_PROG)

        self.tombol_kembali_kemenu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(32, 128), size=wx.Size(240, 31),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_data_miskin_desaButton(self, event):
        event.Skip()

    def OnTombol_progButton(self, event):
        event.Skip()

    def OnTombol_kembali_kemenuButton(self, event):
        self.Close()
