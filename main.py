#!/usr/bin/env python3

import os

import webview

from back.api import Api

"""
An example of serverless app architecture
courtesy of https://github.com/r0x0r/pywebview/blob/docs/examples/todos/start.py
"""


if __name__ == '__main__':
    api = Api()
    webview.create_window('ERpyEditor', 'front/index.html', js_api=api, min_size=(600, 450), fullscreen=True)
    webview.start(debug=True)
