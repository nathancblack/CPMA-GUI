# src/ui/components.py
import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        style = ttk.Style()
        bg_color = style.lookup("TFrame", "background")
        self.canvas = tk.Canvas(self, highlightthickness=0, background=bg_color)
        self.scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_content = ttk.Frame(self.canvas)
        self.window_id = self.canvas.create_window(
            (0, 0), window=self.scrollable_content, anchor="nw"
        )

        self.scrollable_content.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.bind("<Enter>", self._bound_to_mousewheel)
        self.bind("<Leave>", self._unbound_to_mousewheel)

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.window_id, width=event.width)

    def _bound_to_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")


def make_clickable(widget, callback):
    widget.bind("<Button-1>", callback)
    widget.bind(
        "<Enter>",
        lambda e: widget.config(
            font=("calibre", 10, "underline"), cursor="hand2", foreground="blue"
        ),
    )
    widget.bind(
        "<Leave>", lambda e: widget.config(font=("calibre", 10), foreground="black")
    )


def show_help(event, text):
    tooltip = tk.Toplevel()
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{event.x_root + 15}+{event.y_root + 10}")

    label = tk.Label(
        tooltip,
        text=text,
        background="#ffffe0",
        relief="solid",
        borderwidth=1,
        justify="left",
    )
    label.pack()

    event.widget.tooltip_window = tooltip


def hide_help(event):
    if hasattr(event.widget, "tooltip_window"):
        event.widget.tooltip_window.destroy()
        del event.widget.tooltip_window
