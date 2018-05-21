#TwitchChat
#Redd

import wx

class Example(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs) 
		self.InitUI()
		self.Centre()
		self.Show(True)

	def InitUI(self):    
		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		sitem = fileMenu.Append(wx.ID_ANY, 'Settings')
		qitem = fileMenu.Append(wx.ID_EXIT, 'Quit')
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.OpenSettings, sitem)
		self.Bind(wx.EVT_MENU, self.OnQuit, qitem)
		self.SetSize((500, 250))
		self.SetTitle('TwitchChat')

		panel = wx.Panel(self)
		panel.SetBackgroundColour('#4f5049')
		box = wx.BoxSizer(wx.HORIZONTAL)
		chat = wx.TextCtrl(panel)
		box.Add(chat, 1, wx.EXPAND|wx.ALL, 5)
		panel.SetSizer(box)

	def OpenSettings(self, e):
		props = wx.Frame(self, -1,'Properties', size=(320,190))
		props.Centre()
		panel = wx.Panel(props)
		sizer = wx.GridBagSizer(4,4)

		text = wx.StaticText(panel, label="Username")
		sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

		user = wx.TextCtrl(panel)
		sizer.Add(user, pos=(1,0), span=(1,5),
			flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

		text2 = wx.StaticText(panel, label="Password")
		sizer.Add(text2, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

		passwd = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
		sizer.Add(passwd, pos=(3,0), span=(1,5),
			flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

		bttnOkay = wx.Button(panel,label="Ok", size=(90,28))
		sizer.Add(bttnOkay, pos=(4,3),
			flag=wx.RIGHT|wx.BOTTOM, border=5)

		sizer.AddGrowableCol(1)
		sizer.AddGrowableRow(2)
		panel.SetSizerAndFit(sizer)
		props.Show()

		props.Bind(wx.ID_ANY, self.saveInfo(),bttnOkay)
	def saveInfo(self, e):
		pass
	def OnQuit(self, e):
		self.Close()

def main():
	ex = wx.App()
	Example(None)
	ex.MainLoop()    

if __name__ == '__main__':
	main()