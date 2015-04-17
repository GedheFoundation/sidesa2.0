#Boa:Dialog:peringatan

import wx


def create(parent):
    return peringatan(parent)

[wxID_PERINGATAN, wxID_PERINGATANLABEL_PERINGATAN, 
 wxID_PERINGATANTOMBOL_KEMBALI_KEMENU, 
] = [wx.NewId() for _init_ctrls in range(3)]

class peringatan(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PERINGATAN, name=u'peringatan',
              parent=prnt, pos=wx.Point(557, 314), size=wx.Size(270, 124),
              style=wx.CAPTION, title=u'Peringatan !!!')
        self.SetClientSize(wx.Size(270, 124))
        self.Center(wx.BOTH)

        self.label_peringatan = wx.StaticText(id=wxID_PERINGATANLABEL_PERINGATAN,
              label=u'Anda Tidak Berhak\nMelakukan Perubahan\nDan Penambahan Data !!!',
              name=u'label_peringatan', parent=self, pos=wx.Point(56, 8),
              size=wx.Size(170, 51), style=0)

        self.tombol_kembali_kemenu = wx.Button(id=wxID_PERINGATANTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(24, 72), size=wx.Size(224, 32),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_PERINGATANTOMBOL_KEMBALI_KEMENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    
    def OnTombol_kembali_kemenuButton(self, event):
        self.Close()
