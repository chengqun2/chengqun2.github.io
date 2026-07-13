"""Export local HTML files to PDF using Playwright (Chromium)."""

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ("index.html", "index.pdf"),
    ("eng_resume.html", "eng_resume.pdf"),
]


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for html_name, pdf_name in PAIRS:
            html_path = ROOT / html_name
            if not html_path.is_file():
                raise FileNotFoundError(html_path)
            page.goto(
                html_path.as_uri(),
                wait_until="networkidle",
                timeout=120_000,
            )
            page.pdf(
                path=str(ROOT / pdf_name),
                format="A4",
                print_background=True,
                margin={"top": "12mm", "right": "12mm", "bottom": "12mm", "left": "12mm"},
            )
        browser.close()


if __name__ == "__main__":
    main()
