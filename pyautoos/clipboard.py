import pyperclip
import logging
from typing import Optional

logger = logging.getLogger("pyautoos.clipboard")

class Clipboard:
    """
    Clipboard utilities: get, set, and monitor clipboard content.
    """
    @staticmethod
    def set_clipboard(text: str) -> None:
        """Set clipboard text."""
        try:
            pyperclip.copy(text)
            logger.info("Clipboard set.")
        except Exception as e:
            logger.error(f"Failed to set clipboard: {e}")
            raise

    @staticmethod
    def get_clipboard() -> str:
        """Get clipboard text."""
        try:
            text = pyperclip.paste()
            logger.info("Clipboard retrieved.")
            return text
        except Exception as e:
            logger.error(f"Failed to get clipboard: {e}")
            raise

    @staticmethod
    def clipboard(action: str, text: Optional[str] = None) -> Optional[str]:
        """Perform clipboard action: 'copy', 'paste'."""
        if action == 'copy' and text is not None:
            Clipboard.set_clipboard(text)
        elif action == 'paste':
            return Clipboard.get_clipboard()
        else:
            logger.error("Invalid clipboard action or missing text.")
            raise ValueError("Invalid clipboard action or missing text.") 