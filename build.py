'''import os
import shutil
import sys
from distutils.core import setup

# courtesy of https://github.com/r0x0r/pywebview/blob/docs/examples/todos/setup.py

def tree(src):
    return [
        (
            root,
            map(
                lambda f: os.path.join(root, f),
                filter(lambda f: os.path.splitext(f)[1] != '.map', files),
            ),
        )
        for (root, dirs, files) in os.walk(os.path.normpath(src))
    ]


APP = ['start.py']
DATA_FILES = tree('assets')
OPTIONS_OSX = {
    'argv_emulation': False,
    'strip': True,
    'includes': ['WebKit', 'Foundation', 'webview'],
}

if os.path.exists('build'):
    shutil.rmtree('build')

if os.path.exists('dist'):
    shutil.rmtree('dist')

if sys.platform == 'darwin':
    import py2app

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS_OSX},
        setup_requires=['py2app'],
    )
'''