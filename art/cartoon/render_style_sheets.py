"""Render build/sheet_<style>.svg (from party.py) to output/dragonborn_<style>.png with headless Chromium."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import sys, asyncio
from playwright.sync_api import sync_playwright
keys = sys.argv[1:] or ['bold','chibi','storybook','geo']
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width':2440,'height':960})
    for k in keys:
        svg = open(f'build/sheet_{k}.svg').read()
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
        pg.wait_for_timeout(300)
        pg.screenshot(path=f'output/dragonborn_{k}.png', clip={'x':0,'y':0,'width':2440,'height':960})
        print(k)
    b.close()
