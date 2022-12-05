# import all module
from os import path
import asyncio
import os
import pathlib
import subprocess


#prepare
pathlib.Path("_Data_").mkdir(parents=True, exist_ok=True)

#parameters
_App_ = pathlib.Path(r'_App_')
logiFN = (r'Launch_EAapps_Loader.exe')
appFolCheck = (r'_App_')
scFolCheck = (r'_Script_')
titlewindow = 'fahmiyufrizal@2022'
ProgDat = path.expandvars(r'%ProgramData%')
ProgDatConfig = path.expandvars(r'%ProgramData%\eaapps_configured.f2y')

#protection
if not path.exists (logiFN):
	print('[-] Original Filename changed! Be careful!')
	print('[-] Make sure you are downloading this app from')
	print('[-] github.com/fahmiyufrizal')
	print('[-] ')
	print('[-] IF YOU BOUGHT FOR IT')
	print('[-] ASK FOR REFUND!')
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()
if not path.exists (appFolCheck):
	tk.messagebox.showerror(titlewindow,'Folder _App_ tidak ditemukan, silahkan cek kembali!')
	exit()
if not path.exists (scFolCheck):
	tk.messagebox.showerror(titlewindow,'Folder _Script_ tidak ditemukan, silahkan cek kembali!')
	exit()

#parameter for app
