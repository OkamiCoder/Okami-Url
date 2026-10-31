# Okami URL

<p>
  <img src="./assets/banner.png" alt="project banner" width="100%">
</p>

A sleek, dark-themed desktop link shortener built with **CustomTkinter**. Paste a long URL, hit **Shorten**, and copy the result with a single click.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-1F6AA5)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## ✨ Features

- 🖥️ Modern dark GUI built with CustomTkinter
- 🔗 Shortens links via the [is.gd](https://is.gd) API - no API key required
- 📋 One-click copy to clipboard (just click the shortened link)
- ⌨️ Press `Enter` to shorten instantly
- 🕵️ Chrome-impersonated requests with `curl_cffi` to avoid bot-blocking
- ⚡ Lightweight - single file, zero bloat

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/OkamiCoder/okami-url.git
cd okami-url
```

Install the dependencies:

```bash
pip install customtkinter pyperclip curl_cffi
```

## 🚀 Usage

```bash
python okami-url.py
```

1. Paste a long URL into the input field
2. Click **Shorten** (or press `Enter`)
3. Click the resulting short link to copy it to your clipboard

## 🛠️ Built With

| Library | Purpose |
|---|---|
| [customtkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern dark-themed GUI |
| [curl_cffi](https://github.com/yifeikong/curl_cffi) | HTTP requests with browser impersonation |
| [pyperclip](https://github.com/asweigart/pyperclip) | Cross-platform clipboard access |

## 📋 Requirements

- Python 3.6+
- Internet connection (for the is.gd API)

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Made with <3 by <a href="https://github.com/OkamiCoder/">OkamiCoder</a></p>
