#Boa:Dialog:dialog_bantuan

import wx
import wx.richtext
import frm_sideka_menu

def create(parent):
    return dialog_bantuan(parent)

[wxID_DIALOG_BANTUAN, wxID_DIALOG_BANTUANISI_BANTUAN, 
 wxID_DIALOG_BANTUANTOMBOL_TUTUP_BANTUAN, 
] = [wx.NewId() for _init_ctrls in range(3)]

class dialog_bantuan(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG_BANTUAN, name=u'dialog_bantuan',
              parent=prnt, pos=wx.Point(650, 266), size=wx.Size(399, 281),
              style=wx.CAPTION, title=u'Bantuan')
        self.SetClientSize(wx.Size(399, 281))
        self.Center(wx.BOTH)

        self.isi_bantuan = wx.StaticText(id=wxID_DIALOG_BANTUANISI_BANTUAN,
              label=u'Developer  :\nTeam Gerakan Desa Membangun\n\nDibangun dan dikembangkan dengan Menggunakan\nPemrograman Python Dan SQLite3\n\nUntuk penjelasan Mengenai Bantuan Penggunaan Dapat\nMembuka Website Resmi Developer Pengembang\nAplikasi Gerakan Desa Membangun Desa 2.0  \ndi http://dev.gedhe.or.id\n\nLicense GPL 2.0',
              name=u'isi_bantuan', parent=self, pos=wx.Point(16, 24),
              size=wx.Size(367, 204), style=0)

        self.tombol_tutup_bantuan = wx.Button(id=wxID_DIALOG_BANTUANTOMBOL_TUTUP_BANTUAN,
              label=u'Tutup Bantuan', name=u'tombol_tutup_bantuan', parent=self,
              pos=wx.Point(224, 232), size=wx.Size(152, 30), style=0)
        self.tombol_tutup_bantuan.Bind(wx.EVT_BUTTON,
              self.OnTombol_tutup_bantuanButton,
              id=wxID_DIALOG_BANTUANTOMBOL_TUTUP_BANTUAN)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_tutup_bantuanButton(self, event):
        self.Close()
