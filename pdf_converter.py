import os
from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        regular_font_path = os.path.join(
            current_dir, "JetBrainsMono Nerd Font", "JetBrainsMonoNerdFont-Regular.ttf"
        )
        bold_font_path = os.path.join(
            current_dir, "JetBrainsMono Nerd Font", "JetBrainsMonoNerdFont-Bold.ttf"
        )
        italic_font_path = os.path.join(
            current_dir, "JetBrainsMono Nerd Font", "JetBrainsMonoNerdFont-Italic.ttf"
        )

        self.add_font("JetBrainsMono", "", regular_font_path, uni=True)
        self.add_font("JetBrainsMono", "B", bold_font_path, uni=True)
        self.add_font("JetBrainsMono", "I", italic_font_path, uni=True)

    def header(self):
        self.set_font("JetBrainsMono", "B", 20)
        self.cell(0, 10, "PDF Report", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("JetBrainsMono", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")
