# -*- mode: python ; coding: utf-8 -*-
# 资源文件路径
dirs = [
('D:/python/test/mypygame/myTools/img','img'),
('D:/python/test/mypygame/myTools/lib','lib'),
('D:/python/test/mypygame/myTools/img','img')
]

a = Analysis(
    ['__init__.py',
     'baseDir.py'],
    pathex=['D:/python/test/mypygame/myTools'],
    binaries=[],
    datas=dirs,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='初号机',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
#    不显示控制台
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
#    图标
    icon = 'D:/python/test/mypygame/myTools/img/aet1v-zqt6v-001.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='__init__'
)
