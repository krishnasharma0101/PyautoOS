import logging
from typing import Optional, Tuple
from pyautoos.utils import Utils

logger = logging.getLogger("pyautoos.screen")

class Screen:
    """
    Screen utilities: screenshot, OCR, find image/text on screen, highlight text.
    """
    @staticmethod
    def screenshot(save_path: Optional[str] = None):
        """Take a screenshot of the screen."""
        try:
            import pyautogui
            img = pyautogui.screenshot()
            if save_path:
                img.save(save_path)
                logger.info(f"Screenshot saved to {save_path}")
                return save_path
            logger.info("Screenshot taken.")
            return img
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return None

    @staticmethod
    def get_screen_text() -> str:
        """Extract text from the screen using OCR."""
        try:
            if not Utils.ensure_tesseract():
                logger.error("Tesseract is not available and could not be installed.")
                return ""
            import pyautogui
            import pytesseract
            img = pyautogui.screenshot()
            text = pytesseract.image_to_string(img)
            logger.info("Extracted text from screen.")
            return text
        except Exception as e:
            logger.error(f"Failed to extract text from screen: {e}")
            return ""

    @staticmethod
    def find_on_screen(image_path: str) -> Optional[Tuple[int, int, int, int]]:
        """Find an image on the screen. Returns (left, top, width, height) or None."""
        try:
            import pyautogui
            box = pyautogui.locateOnScreen(image_path)
            if box:
                logger.info(f"Found image on screen: {image_path}")
                return box
        except Exception as e:
            logger.error(f"Failed to find image on screen: {e}")
        return None

    @staticmethod
    def highlight_text_on_screen(text: str) -> bool:
        """Highlight the first occurrence of text on the screen using OCR and OpenCV."""
        try:
            if not Utils.ensure_tesseract():
                logger.error("Tesseract is not available and could not be installed.")
                return False
            import pyautogui
            import pytesseract
            import cv2
            import numpy as np
            img = pyautogui.screenshot()
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
            for i, word in enumerate(data['text']):
                if text.lower() in word.lower():
                    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                    cv2.rectangle(img_cv, (x, y), (x+w, y+h), (0,255,0), 2)
                    logger.info(f"Highlighted text '{text}' on screen.")
                    return True
        except Exception as e:
            logger.error(f"Failed to highlight text on screen: {e}")
        return False 