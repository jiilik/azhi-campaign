"""Printable progression wheels (Troy, 2026-11-11) -> progression-wheels-print.pdf.

Two US Letter pages, in colour, for scribbling on and for explaining the
progression rules to a reviewer:
  1. the skills grid (skills_grid.py -> skills-grid.pdf)
  2. the species advancement wheel (art/cartoon/species_advancement.py --print,
     white page -> art/cartoon/output/species_advancement.pdf)
Both are regenerated first, then each is scaled to fit its page.

Usage: python3 canon/diagrams/print_wheels.py
"""
import os
import subprocess
import sys
from pypdf import PdfReader, PdfWriter, Transformation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
CARTOON = os.path.join(ROOT, "art", "cartoon")
W, H, M = 612, 792, 27  # US Letter in points, 3/8 inch margin

subprocess.run([sys.executable, os.path.join(HERE, "skills_grid.py")], check=True)
subprocess.run([sys.executable, os.path.join(CARTOON, "species_advancement.py"), "--print"],
               check=True, cwd=CARTOON)

out = PdfWriter()
for src in (os.path.join(HERE, "skills-grid.pdf"),
            os.path.join(CARTOON, "output", "species_advancement.pdf")):
    page = PdfReader(src).pages[0]
    x0, y0 = float(page.mediabox.left), float(page.mediabox.bottom)
    w, h = float(page.mediabox.width), float(page.mediabox.height)
    k = min((W - 2 * M) / w, (H - 2 * M) / h)
    page.add_transformation(Transformation().translate(-x0, -y0).scale(k)
                            .translate((W - w * k) / 2, (H - h * k) / 2))
    page.mediabox.lower_left = (0, 0)
    page.mediabox.upper_right = (W, H)
    blank = out.add_blank_page(W, H)
    blank.merge_page(page)
dest = os.path.join(HERE, "progression-wheels-print.pdf")
out.write(dest)
print(dest)
