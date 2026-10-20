"""Render the two Saturday-Morning Bold dragonborn scenes used in the handout -> output/dragonborn_spine.png, output/dragonborn_innersea.png."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
from party import STYLES, scene_svg
st = STYLES['bold']
for key, name in (('A', 'dragonborn_spine'), ('B', 'dragonborn_innersea')):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">{scene_svg(st, key)}</svg>'
    open(f'build/{name}.svg', 'w').write(svg)
    subprocess.run([sys.executable, 'svg2png.py', f'build/{name}.svg', f'output/{name}.png', '1200', '800'], check=True)
    print(name)
