import watchfiles
import webview
import signal

from back.api import Api
from back.api_expose import ApiExpose

def watch_and_reload(window):
    for change in watchfiles.watch('./front'):
        ## i couldn't get window.load_url() to actually work so I used this instead
        window.evaluate_js('window.location.reload()')


if __name__ == '__main__':
    debug = True
    if debug:
        api = ApiExpose()
        api.test()
        window = webview.create_window('ERpyEditor', 'front/index.html', js_api=api, min_size=(600, 450), fullscreen=False)

        def signal_handler(sig, frame):
            try:
                window.destroy()
            except Exception:
                pass
            finally:
                exit()
            
        signal.signal(signal.SIGINT, signal_handler)

        webview.start(watch_and_reload, window, debug=True)
        exit()
    api = Api()
    window = webview.create_window('ERpyEditor', 'front/index.html', js_api=api, min_size=(600, 450), fullscreen=False)

    

    webview.start(watch_and_reload, window, debug=True)
