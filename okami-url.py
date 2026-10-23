import sys
import customtkinter as ctk
import pyperclip
from curl_cffi import requests


APP_TITLE = "Okami URL - Link Shortener"
API_URL = "https://is.gd/create.php"
BG = "#1a1a2e"
FG = "#eaeaea"
ACCENT = "#e94560"
ENTRY_BG = "#16213e"
FONT = ("Segoe UI", 13)
FONT_BOLD = ("Segoe UI", 15, "bold")


def shorten(url: str) -> str:
    r = requests.get(
        API_URL,
        params={"format": "simple", "url": url},
        impersonate="chrome",
        timeout=15,
    )
    r.raise_for_status()
    result = r.text.strip()
    if result.startswith("Error:"):
        raise ValueError(result)
    return result


class OkamiURL(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title(APP_TITLE)
        self.geometry("560x300")
        self.resizable(False, False)
        self.configure(fg_color=BG)

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self, text="◆ Okami URL", font=("Segoe UI", 22, "bold"),
            text_color=ACCENT, fg_color="transparent",
        ).pack(pady=(22, 4))

        ctk.CTkLabel(
            self, text="Paste a link and hit Shorten",
            font=FONT, text_color=FG, fg_color="transparent",
        ).pack()

        self.entry = ctk.CTkEntry(
            self, width=480, height=40, font=FONT,
            fg_color=ENTRY_BG, text_color=FG,
            placeholder_text="https://example.com/very/long/link...",
        )
        self.entry.pack(pady=16)
        self.entry.bind("<Return>", lambda _e: self.on_shorten())

        self.btn = ctk.CTkButton(
            self, text="Shorten", font=FONT_BOLD, height=42, width=200,
            fg_color=ACCENT, hover_color="#c73650", command=self.on_shorten,
        )
        self.btn.pack()

        self.result_var = ctk.StringVar(value="")
        self.result_label = ctk.CTkLabel(
            self, textvariable=self.result_var, font=FONT,
            text_color="#4ecca3", fg_color="transparent", cursor="hand2",
        )
        self.result_label.pack(pady=(18, 2))
        self.result_label.bind("<Button-1>", lambda _e: self.copy_result())

        self.status_var = ctk.StringVar(value="")
        ctk.CTkLabel(
            self, textvariable=self.status_var, font=("Segoe UI", 11),
            text_color="#888888", fg_color="transparent",
        ).pack()

        self._short_url = None

    def on_shorten(self):
        url = self.entry.get().strip()
        if not url:
            self.status_var.set("Enter a link first")
            return
        self.status_var.set("Contacting API...")
        self.btn.configure(state="disabled")
        self.update()

        try:
            short = shorten(url)
        except Exception as exc:
            self.status_var.set(f"Error: {exc}")
            self.btn.configure(state="normal")
            return

        self._short_url = short
        self.result_var.set(short)
        self.status_var.set("Done! Click the link to copy it.")
        self.btn.configure(state="normal")

    def copy_result(self):
        if self._short_url:
            pyperclip.copy(self._short_url)
            self.status_var.set("Copied to clipboard!")


if __name__ == "__main__":
    app = OkamiURL()
    app.mainloop()
