"""Aplicação principal do chá de panela."""

from pathlib import Path
import runpy


runpy.run_path(str(Path(__file__).with_name("chadepanela_prototipo.py")))
