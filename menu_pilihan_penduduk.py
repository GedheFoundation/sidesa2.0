#Boa:Frame:menu_input_penduduk

import wx
import wx.lib.buttons
import kk_sementara

def create(parent):
    return menu_input_penduduk(parent)

[wxID_MENU_INPUT_PENDUDUK, wxID_MENU_INPUT_PENDUDUKBUTTON_INPUT, 
] = [wx.NewId() for _init_ctrls in range(2)]

class menu_input_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MENU_INPUT_PENDUDUK,
              name=u'menu_input_penduduk', parent=prnt, pos=wx.Point(580, 239),
              size=wx.Size(304, 61), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Pilihan Data Penduduk')
        self.SetClientSize(wx.Size(302, 36))

        self.button_input = wx.Button(id=wxID_MENU_INPUT_PENDUDUKBUTTON_INPUT,
              label=u'Input KK Sementara', name=u'button_input', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(302, 36), style=0)
        self.button_input.Bind(wx.EVT_BUTTON, self.OnButton_inputButton,
              id=wxID_MENU_INPUT_PENDUDUKBUTTON_INPUT)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton_inputButton(self, event):
        self.main=kk_sementara.create(None)
        self.main.Show()
        self.Close()
