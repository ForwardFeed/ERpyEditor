import watchfiles
import webview

from back.api import Api

def watch_and_reload(window):
    for change in watchfiles.watch('./front'):
        ## i couldn't get window.load_url() to actually work so I used this instead
        window.evaluate_js('window.location.reload()')


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('ERpyEditor', 'front/index.html', js_api=api, min_size=(600, 450), fullscreen=False)
    webview.start(watch_and_reload, window, debug=True)
