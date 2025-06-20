import logging
from typing import Optional, List

logger = logging.getLogger("pyautoos.web")

class Web:
    """
    Web and file automation utilities: search, browser, file I/O, directory listing.
    """
    @staticmethod
    def search_web(query: str) -> None:
        """Search the web using the default browser."""
        try:
            import webbrowser
            webbrowser.open(f"https://www.google.com/search?q={query}")
            logger.info(f"Searched web for: {query}")
        except Exception as e:
            logger.error(f"Failed to search web: {e}")
            raise

    @staticmethod
    def open_file(path: str) -> None:
        """Open a file with the default application."""
        try:
            import os
            os.startfile(path)
            logger.info(f"Opened file: {path}")
        except Exception as e:
            logger.error(f"Failed to open file {path}: {e}")
            raise

    @staticmethod
    def read_file(path: str) -> str:
        """Read the contents of a file as text."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
            logger.info(f"Read file: {path}")
            return data
        except Exception as e:
            logger.error(f"Failed to read file {path}: {e}")
            raise

    @staticmethod
    def write_file(path: str, data: str) -> None:
        """Write text data to a file."""
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(data)
            logger.info(f"Wrote to file: {path}")
        except Exception as e:
            logger.error(f"Failed to write file {path}: {e}")
            raise

    @staticmethod
    def list_dir(path: str) -> List[str]:
        """List files and directories in a given path."""
        try:
            import os
            items = os.listdir(path)
            logger.info(f"Listed directory: {path}")
            return items
        except Exception as e:
            logger.error(f"Failed to list directory {path}: {e}")
            raise 