import logging
from typing import Optional, List, Dict

logger = logging.getLogger("pyautoos.gui")

class GUI:
    """
    GUI content extraction and interaction utilities.
    """
    @staticmethod
    def get_gui_text(app_name: str) -> Optional[str]:
        """Extract visible text from the app's GUI (Windows)."""
        try:
            from pywinauto.application import Application
            app = Application(backend="uia").connect(title_re=app_name, found_index=0)
            dlg = app.top_window()
            text = dlg.window_text()
            logger.info(f"Extracted GUI text from {app_name}.")
            return text
        except Exception as e:
            logger.error(f"Failed to get GUI text for {app_name}: {e}")
            return None

    @staticmethod
    def get_gui_structure(app_name: str) -> Optional[Dict]:
        """Get the GUI element tree structure (Windows)."""
        try:
            from pywinauto.application import Application
            app = Application(backend="uia").connect(title_re=app_name, found_index=0)
            dlg = app.top_window()
            structure = dlg.dump_tree()
            logger.info(f"Extracted GUI structure from {app_name}.")
            return structure
        except Exception as e:
            logger.error(f"Failed to get GUI structure for {app_name}: {e}")
            return None

    @staticmethod
    def find_element(text: str) -> Optional[Dict]:
        """Find a GUI element by visible text (Windows)."""
        try:
            from pywinauto import Desktop
            windows = Desktop(backend="uia").windows()
            for win in windows:
                if text.lower() in win.window_text().lower():
                    logger.info(f"Found element with text: {text}")
                    return {'handle': win.handle, 'title': win.window_text()}
        except Exception as e:
            logger.error(f"Failed to find element with text {text}: {e}")
        return None

    @staticmethod
    def click_element(text: str) -> bool:
        """Click the first GUI element matching text (Windows)."""
        try:
            from pywinauto import Desktop
            windows = Desktop(backend="uia").windows()
            for win in windows:
                if text.lower() in win.window_text().lower():
                    win.click_input()
                    logger.info(f"Clicked element with text: {text}")
                    return True
        except Exception as e:
            logger.error(f"Failed to click element with text {text}: {e}")
        return False 