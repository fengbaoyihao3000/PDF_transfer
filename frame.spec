# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['frame.py', 'pdf_easy.py', 'pdf_hard.py', 'pdf_normal.py', 'pdf_Process.py'],
             pathex=['C:\\Users\\wws\\Desktop\\网络情报获取大作业'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='frame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='bitbug_favicon.ico')
