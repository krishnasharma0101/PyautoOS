import subprocess
import psutil
import logging
import os
from typing import Optional, List, Dict

logger = logging.getLogger("pyautoos.app")

class App:
    """
    App automation: open, close, focus, and query running applications.
    """
    @staticmethod
    def open_app(path: str) -> Optional[object]:
        """Open an application by path (.exe via Popen, .lnk and others via os.startfile)."""
        try:
            ext = os.path.splitext(path)[1].lower()
            if ext == '.exe':
                proc = subprocess.Popen([path])
                logger.info(f"Opened exe app: {path}")
                return proc
            else:
                os.startfile(path)
                logger.info(f"Opened file/app via startfile: {path}")
                return None
        except Exception as e:
            logger.error(f"Failed to open app {path}: {e}")
            raise

    @staticmethod
    def close_app(name: str) -> bool:
        """Close all processes matching the app name."""
        closed = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and name.lower() in proc.info['name'].lower():
                try:
                    proc.terminate()
                    closed = True
                    logger.info(f"Closed app: {proc.info['name']}")
                except Exception as e:
                    logger.error(f"Failed to close app {proc.info['name']}: {e}")
        return closed

    @staticmethod
    def is_app_running(name: str) -> bool:
        """Check if an app is running by name."""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and name.lower() in proc.info['name'].lower():
                return True
        return False

    @staticmethod
    def get_active_app() -> Optional[str]:
        """Get the name of the currently active app (Windows)."""
        try:
            import win32gui, win32process
            hwnd = win32gui.GetForegroundWindow()
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['pid'] == pid:
                    return proc.info['name']
        except Exception as e:
            logger.error(f"Failed to get active app: {e}")
        return None

    @staticmethod
    def focus_app(name: str) -> bool:
        """Focus the first window of the app by name (Windows)."""
        try:
            import win32gui
            def enum_handler(hwnd, result):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if name.lower() in title.lower():
                        win32gui.SetForegroundWindow(hwnd)
                        result.append(hwnd)
            result = []
            win32gui.EnumWindows(enum_handler, result)
            if result:
                logger.info(f"Focused app window: {name}")
                return True
        except Exception as e:
            logger.error(f"Failed to focus app {name}: {e}")
        return False

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
        windows = App.get_window_list()
        return [w for w in windows if name.lower() in w['title'].lower()]

    @staticmethod
    def get_window_geometry(name: str) -> Optional[Dict]:
        """Get geometry of the first window matching name (Windows)."""
        try:
            import win32gui
            windows = App.get_app_windows(name)
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
            import win32gui, win32con
            windows = App.get_app_windows(name)
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
            windows = App.get_app_windows(name)
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
            geom = App.get_window_geometry(name)
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