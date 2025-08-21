# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

gdal_data = collect_data_files('rasterio', includes=['gdal_data/*'])


# Add pyproj/proj folder which includes proj.db
# Safe pyproj proj.db handling
try:
    import pyproj
    proj_data = [(pyproj.datadir.get_data_dir(), 'pyproj/proj')]
except ImportError:
    proj_data = []

a = Analysis(
    ['main_window.py'],
    pathex=[],
    binaries=[],
    datas=gdal_data + proj_data,
    hiddenimports=[
        'rasterio.sample',
        'pyproj',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main_window',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
