import logging
from typing import List, Dict, Optional

logger = logging.getLogger("pyautoos.window")

class Window:
    """
    Window management utilities for listing, resizing, moving, and capturing windows.
    """
    @staticmethod
    def get_window_list() -> List[Dict]:
        """Get a list of all top-level windows (Windows)."""
        try:
            import win32gui
            windows = []
            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    windows.append({
                        'hwnd': hwnd,
                        'title': win32gui.GetWindowText(hwnd)
                    })
            win32gui.EnumWindows(enum_handler, None)
            return windows
        except Exception as e:
            logger.error(f"Failed to get window list: {e}")
            return []

    @staticmethod
    def get_app_windows(name: str) -> List[Dict]:
        """Get all windows belonging to an app by name (Windows)."""
        windows = Window.get_window_list()
        return [w for w in windows if name.lower() in w['title'].lower()]

    @staticmethod
    def get_window_geometry(name: str) -> Optional[Dict]:
        """Get geometry of the first window matching name (Windows)."""
        try:
            import win32gui
            windows = Window.get_app_windows(name)
            if windows:
                hwnd = windows[0]['hwnd']
                rect = win32gui.GetWindowRect(hwnd)
                return {'x': rect[0], 'y': rect[1], 'width': rect[2]-rect[0], 'height': rect[3]-rect[1]}
        except Exception as e:
            logger.error(f"Failed to get window geometry for {name}: {e}")
        return None

    @staticmethod
    def resize_window(name: str, width: int, height: int) -> bool:
        """Resize the first window matching name (Windows)."""
        try:
            import win32gui
            windows = Window.get_app_windows(name)
            if windows:
                hwnd = windows[0]['hwnd']
                x, y, _, _ = win32gui.GetWindowRect(hwnd)
                win32gui.MoveWindow(hwnd, x, y, width, height, True)
                logger.info(f"Resized window {name} to {width}x{height}")
                return True
        except Exception as e:
            logger.error(f"Failed to resize window {name}: {e}")
        return False

    @staticmethod
    def move_window(name: str, x: int, y: int) -> bool:
        """Move the first window matching name to (x, y) (Windows)."""
        try:
            import win32gui
            windows = Window.get_app_windows(name)
            if windows:
                hwnd = windows[0]['hwnd']
                _, _, width, height = win32gui.GetWindowRect(hwnd)
                win32gui.MoveWindow(hwnd, x, y, width, height, True)
                logger.info(f"Moved window {name} to ({x},{y})")
                return True
        except Exception as e:
            logger.error(f"Failed to move window {name}: {e}")
        return False

    @staticmethod
    def capture_window(name: str, save_path: Optional[str] = None) -> Optional[str]:
        """Capture a screenshot of the first window matching name (Windows)."""
        try:
            import pyautogui
            geom = Window.get_window_geometry(name)
            if geom:
                x, y, w, h = geom['x'], geom['y'], geom['width'], geom['height']
                img = pyautogui.screenshot(region=(x, y, w, h))
                if save_path:
                    img.save(save_path)
                    logger.info(f"Saved window screenshot to {save_path}")
                    return save_path
                return img
        except Exception as e:
            logger.error(f"Failed to capture window {name}: {e}")
        return None 