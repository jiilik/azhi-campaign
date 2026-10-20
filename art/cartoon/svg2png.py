import sys
from playwright.sync_api import sync_playwright
src, dst, w, h = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': w, 'height': h})
    pg.set_content(f'<html><body style="margin:0">{open(src).read()}</body></html>'); pg.wait_for_timeout(300)
    pg.screenshot(path=dst, clip={'x':0,'y':0,'width':w,'height':h}); b.close()
