import logging
import platform
import time
import os
import sys
import urllib.request
import zipfile
import subprocess
from typing import Dict, Any, Optional

logger = logging.getLogger("pyautoos.utils")

TESSERACT_64BIT_URL = "https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe"

class Utils:
    """
    Utility functions: platform detection, system info, logging, wait, notes, and Tesseract auto-install.
    """
    @staticmethod
    def get_system_info() -> Dict[str, Any]:
        """Get basic system information."""
        try:
            info = {
                'platform': platform.system(),
                'platform_release': platform.release(),
                'platform_version': platform.version(),
                'architecture': platform.machine(),
                'processor': platform.processor(),
                'python_version': platform.python_version(),
                'user': os.getlogin()
            }
            logger.info("Retrieved system info.")
            return info
        except Exception as e:
            logger.error(f"Failed to get system info: {e}")
            return {}

    @staticmethod
    def log_activity(enable: bool = True) -> None:
        """Enable or disable activity logging."""
        if enable:
            logger.setLevel(logging.INFO)
            logger.info("Activity logging enabled.")
        else:
            logger.setLevel(logging.WARNING)
            logger.info("Activity logging disabled.")

    @staticmethod
    def wait(seconds: int) -> None:
        """Wait for a number of seconds."""
        try:
            time.sleep(seconds)
            logger.info(f"Waited for {seconds} seconds.")
        except Exception as e:
            logger.error(f"Failed to wait: {e}")
            raise

    @staticmethod
    def take_note(text: str, note_path: str = "pyautoos_notes.txt") -> None:
        """Append a note to a notes file."""
        try:
            with open(note_path, 'a', encoding='utf-8') as f:
                f.write(text + '\n')
            logger.info(f"Note taken: {text}")
        except Exception as e:
            logger.error(f"Failed to take note: {e}")
            raise

    @staticmethod
    def install_tesseract_windows(installer_url: Optional[str] = None) -> Optional[str]:
        """
        Download and install the 64-bit Tesseract OCR for Windows and add to PATH.
        Only the official 64-bit version is supported.
        Returns the path to tesseract.exe if successful, else None.
        """
        import shutil
        try:
            tesseract_dir = os.path.join(os.getcwd(), 'tesseract')
            tesseract_exe = os.path.join(tesseract_dir, 'tesseract.exe')
            if os.path.exists(tesseract_exe):
                logger.info("Tesseract already installed.")
                Utils._add_to_path(tesseract_dir)
                return tesseract_exe

            if installer_url is None:
                installer_url = TESSERACT_64BIT_URL
            installer_path = os.path.join(os.getcwd(), "tesseract-installer.exe")
            logger.info(f"Downloading Tesseract installer from {installer_url} ...")
            urllib.request.urlretrieve(installer_url, installer_path)
            logger.info("Running Tesseract installer (silent)...")
            install_cmd = [installer_path, "/SILENT", f"/DIR={tesseract_dir}"]
            result = subprocess.run(install_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logger.error(f"Tesseract installer failed: {result.stderr}")
                os.remove(installer_path)
                return None
            os.remove(installer_path)
            if os.path.exists(tesseract_exe):
                Utils._add_to_path(tesseract_dir)
                logger.info(f"Tesseract installed at {tesseract_exe} and added to PATH.")
                return tesseract_exe
            else:
                logger.error("Tesseract installation failed: tesseract.exe not found.")
                return None
        except Exception as e:
            logger.error(f"Tesseract installation error: {e}")
            return None

    @staticmethod
    def _add_to_path(directory: str):
        """Add a directory to the PATH for the current process and future subprocesses."""
        if directory not in os.environ["PATH"]:
            os.environ["PATH"] = directory + os.pathsep + os.environ["PATH"]
            logger.info(f"Added {directory} to PATH.")

    @staticmethod
    def ensure_tesseract():
        """Ensure Tesseract is installed and available in PATH."""
        import shutil
        if shutil.which("tesseract"):
            logger.info("Tesseract is available.")
            return True
        # Try adding the user-provided path
        tess_exe = r"C:\Program Files\tesseract.exe"
        tess_dir = os.path.dirname(tess_exe)
        if os.path.exists(tess_exe):
            if tess_dir not in os.environ["PATH"]:
                os.environ["PATH"] = tess_dir + os.pathsep + os.environ["PATH"]
                logger.info(f"Added {tess_dir} to PATH.")
            if shutil.which("tesseract"):
                logger.info("Tesseract found after updating PATH.")
                return True
        # Also try adding C:\Program Files to PATH
        if r"C:\Program Files" not in os.environ["PATH"]:
            os.environ["PATH"] = r"C:\Program Files" + os.pathsep + os.environ["PATH"]
            logger.info("Added C:\Program Files to PATH.")
        if shutil.which("tesseract"):
            logger.info("Tesseract found after adding C:\Program Files to PATH.")
            return True
        if platform.system() == "Windows":
            exe = Utils.install_tesseract_windows()
            if exe and shutil.which("tesseract"):
                return True
            logger.error("Tesseract could not be installed or found after installation attempt.")
            return False
        logger.error("Tesseract auto-install is only supported on Windows.")
        return False 