"""Export local HTML files to PDF using Playwright (Chromium)."""

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ("index.html", "index.pdf"),
    ("eng_resume.html", "eng_resume.pdf"),
]

PRINT_CSS = """
@media print {
  html { scroll-behavior: auto; }
  body { background: white !important; }
  body > .pointer-events-none { display: none !important; }
  .animate-fade-rise {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
  header { box-shadow: none !important; break-inside: avoid; }
  header > .relative { padding: 20px 24px !important; }
  header img { width: 72px !important; height: 72px !important; }
  header .mt-5 { display: none !important; }
  header ul {
    margin-top: 12px !important;
    padding-top: 10px !important;
    gap: 8px 14px !important;
    font-size: 10px !important;
  }
  main { max-width: none !important; padding: 16px 0 0 !important; }
  main > section {
    padding: 14px 18px !important;
    margin-top: 16px !important;
    background: white !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
  }
  main > section:first-child { margin-top: 0 !important; }
  main > section:first-child .space-y-4 > * + * { margin-top: 10px !important; }
  dl { gap: 8px !important; }
  dl > div { padding: 8px !important; }
  dd { font-size: 12px !important; }
  h2 { margin-bottom: 12px !important; break-after: avoid; }
  article { padding: 12px !important; break-inside: avoid; }
  article > div:first-child { break-after: avoid; }
  main > section:nth-of-type(4) > div { display: block !important; }
  main > section:nth-of-type(4) article + article { margin-top: 10px; }
  main > section:nth-of-type(2),
  main > section:nth-of-type(5),
  main > section:nth-of-type(6) { break-inside: avoid; }
  main > section:nth-of-type(5) { break-after: avoid; }
  main > p:last-child { margin-top: 12px !important; padding-bottom: 0 !important; }
  .text-sm { font-size: 12px !important; line-height: 1.55 !important; }
  .text-xs { font-size: 10px !important; }
  p { orphans: 3; widows: 3; }
}
"""


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.emulate_media(media="print", reduced_motion="reduce")
        for html_name, pdf_name in PAIRS:
            html_path = ROOT / html_name
            if not html_path.is_file():
                raise FileNotFoundError(html_path)
            page.goto(
                html_path.as_uri(),
                wait_until="networkidle",
                timeout=120_000,
            )
            page.evaluate("document.fonts.ready")
            page.add_style_tag(content=PRINT_CSS)
            page.pdf(
                path=str(ROOT / pdf_name),
                format="A4",
                print_background=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=(
                    '<div style="width:100%;text-align:center;font-size:8px;color:#64748b">'
                    '<span class="pageNumber"></span> / <span class="totalPages"></span>'
                    '</div>'
                ),
                margin={"top": "12mm", "right": "12mm", "bottom": "14mm", "left": "12mm"},
            )
            print(f"Wrote {pdf_name}")
        browser.close()


if __name__ == "__main__":
    main()
