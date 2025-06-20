import pyautogui
import logging
from typing import Optional

logger = logging.getLogger("pyautoos.input")

class Input:
    """
    Keyboard and mouse automation utilities.
    """
    @staticmethod
    def keyboard_input(text: str) -> None:
        """Type text using the keyboard."""
        try:
            pyautogui.write(text)
            logger.info(f"Typed text: {text}")
        except Exception as e:
            logger.error(f"Failed to type text: {e}")
            raise

    @staticmethod
    def press_key(key: str) -> None:
        """Press a single key."""
        try:
            pyautogui.press(key)
            logger.info(f"Pressed key: {key}")
        except Exception as e:
            logger.error(f"Failed to press key {key}: {e}")
            raise

    @staticmethod
    def mouse_click(x: int, y: int, button: str = 'left') -> None:
        """Click the mouse at (x, y)."""
        try:
            pyautogui.click(x, y, button=button)
            logger.info(f"Mouse clicked at ({x},{y}) with {button} button.")
        except Exception as e:
            logger.error(f"Failed to click mouse: {e}")
            raise

    @staticmethod
    def mouse_move(x: int, y: int) -> None:
        """Move the mouse to (x, y)."""
        try:
            pyautogui.moveTo(x, y)
            logger.info(f"Mouse moved to ({x},{y}).")
        except Exception as e:
            logger.error(f"Failed to move mouse: {e}")
            raise

    @staticmethod
    def mouse_scroll(amount: int) -> None:
        """Scroll the mouse wheel by amount."""
        try:
            pyautogui.scroll(amount)
            logger.info(f"Mouse scrolled by {amount}.")
        except Exception as e:
            logger.error(f"Failed to scroll mouse: {e}")
            raise 