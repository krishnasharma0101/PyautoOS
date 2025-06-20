"""
pyautoos: Cross-platform (Windows-first) automation library for system-level tasks.
"""

from .app import App
from .clipboard import Clipboard
from .input import Input
from .gui import GUI
from .tasks import Tasks
from .window import Window
from .screen import Screen
from .web import Web
from .utils import Utils

__version__ = "0.1.0"

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pyautoos")

# Automatically ensure Tesseract is available on import (Windows only)
import platform
if platform.system() == "Windows":
    try:
        Utils.ensure_tesseract()
    except Exception as e:
        logger.error(f"Tesseract auto-setup failed: {e}")

logger.info("pyautoos initialized successfully") 