from setuptools import setup, find_packages

setup(
    name="pyautoos",
    version="0.1.0",
    description="Cross-platform (Windows-first) automation library for system-level tasks.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "pyautogui",
        "pyperclip",
        "pytesseract",
        "pywinauto",
        "psutil",
        "opencv-python",
        "mss",
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    url="https://github.com/yourusername/pyautoos",
    project_urls={
        "Source": "https://github.com/yourusername/pyautoos",
    },
) 