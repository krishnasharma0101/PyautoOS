# pyautoos

**pyautoos** is a cross-platform (Windows-first) automation library for system-level tasks, designed for easy scripting, chaining, and future LLM integration. The API is inspired by pandas/numpy for argument-driven, chainable automation.

---

## 🚀 Features

| Area         | Functionality                                                                 |
|--------------|-------------------------------------------------------------------------------|
| App          | Open, close, focus, check, and list running apps                             |
| Window       | List, move, resize, capture, and get geometry of windows                     |
| Clipboard    | Get/set clipboard, copy/paste actions                                        |
| Input        | Keyboard typing, key press, mouse move/click/scroll                          |
| GUI          | Extract GUI text/structure, find/click elements                              |
| Screen       | Screenshot, OCR (Tesseract), find image/text, highlight text                 |
| Web/File     | Web search, open/read/write files, list directories                          |
| Tasks        | Chain tasks, LLM prompt compatibility, run task chains                       |
| Utils        | Platform detection, system info, logging, wait, take notes                   |

### Main Functions
- `open_app(path: str)`
- `close_app(name: str)`
- `is_app_running(name: str)`
- `get_active_app()`
- `focus_app(name: str)`
- `get_window_list()`
- `get_app_windows(name: str)`
- `get_window_geometry(name: str)`
- `resize_window(name, width, height)`
- `move_window(name, x, y)`
- `capture_window(name)`
- `clipboard(action: str, text: Optional[str])`
- `set_clipboard(text: str)`
- `get_clipboard()`
- `keyboard_input(text: str)`
- `press_key(key: str)`
- `mouse_click(x, y, button='left')`
- `mouse_move(x, y)`
- `mouse_scroll(amount: int)`
- `get_gui_text(app_name: str)`
- `get_gui_structure(app_name: str)`
- `find_element(text: str)`
- `click_element(text: str)`
- `screenshot(save_path=None)`
- `get_screen_text()`
- `find_on_screen(image_path: str)`
- `highlight_text_on_screen(text: str)`
- `search_web(query: str)`
- `open_file(path: str)`
- `read_file(path: str)`
- `write_file(path: str, data: str)`
- `list_dir(path: str)`
- `run_task(task: str)`
- `get_system_info()`
- `log_activity(enable=True)`
- `wait(seconds: int)`
- `take_note(text: str)`
- `run([...])` (chain of commands)

---

## 🛠️ Installation

```bash
pip install pyautoos
```

- On first use, Tesseract OCR will be installed automatically on Windows if not found (may require admin rights).
- All other dependencies are installed via pip.

---

## 📝 Example Usage

```python
from pyautoos import App, Clipboard, Input, Screen

# Open Notepad (or any app)
App.open_app(r"C:\Windows\System32\notepad.exe")

# Type text
Input.keyboard_input("Hello from pyautoos!\n")

# Copy to clipboard
Clipboard.set_clipboard("Copied text")

# Take a screenshot and OCR
Screen.screenshot("screen.png")
print(Screen.get_screen_text())
```

---

## 🤖 Future Scope & Contributions

- **Cross-platform support:** Full Linux/macOS support and abstraction.
- **Advanced GUI automation:** Deep UI tree navigation, accessibility, and automation.
- **LLM integration:** Natural language task parsing and execution.
- **App-specific plugins:** Office automation, browser automation, etc.
- **Headless/remote automation:** Run scripts on remote or headless systems.
- **Better error handling and user prompts.**
- **Community-contributed modules and recipes.**

**Contributions are welcome!**
- Open issues or pull requests for new features, bug fixes, or documentation.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines (coming soon).

---

## ⚠️ Notes
- Some features require Windows and admin rights (for Tesseract auto-install).
- For OCR, Tesseract will be installed or detected automatically.
- For best results, run scripts in a virtual environment.

---

## License
MIT 