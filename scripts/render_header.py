"""Build the original Sea Field profile header. Requires fontTools locally.

The four Chinese name glyphs are outlined so GitHub renders the same typography
on every platform. SVGs remain self-contained and have accessible descriptions.
Run: python scripts/render_header.py
"""

from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
FONT = Path("C:/Windows/Fonts/msyhbd.ttc")


def outlined_name(x, baseline, size, color):
    font = TTFont(FONT, fontNumber=0)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    parts = []
    for char in "海生不浪":
        glyph_name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[glyph_name].draw(pen)
        parts.append(f'<path d="{pen.getCommands()}" transform="translate({x:.2f} {baseline}) scale({scale:.6f} {-scale:.6f})" fill="{color}"/>')
        x += glyphs[glyph_name].width * scale + size * .07
    font.close()
    return "\n".join(parts)


def render(theme, mobile=False):
    dark = theme == "dark"
    width, height = (620, 300) if mobile else (1200, 340)
    bg, fg, muted, line, accent = (
        ("#0D1117", "#F0F6FC", "#8B9BB0", "#243244", "#7DDFE7") if dark else
        ("#FFFFFF", "#162131", "#637186", "#E2E8EF", "#087F8C")
    )
    left = 32 if mobile else 52
    name_size = 76 if mobile else 94
    baseline = 149 if mobile else 180
    name = outlined_name(left, baseline, name_size, fg)
    wave_x = 345 if mobile else 720
    wave_opacity = ".16" if mobile else ".65"
    waves = []
    for n in range(17):
        shift = n * 13
        waves.append(f'<path d="M-35 {62+shift}C60 {6+shift} 135 {-62+shift} 238 {22+shift}S366 {162+shift} 510 {60+shift}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">海生不浪 · ZJY-HSBL</title>
  <desc id="desc">Computer vision research and practical software engineering. An original editorial wordmark with flowing sea contours.</desc>
  <defs>
    <linearGradient id="sea" x1="0" y1="220" x2="490" y2="50" gradientUnits="userSpaceOnUse"><stop stop-color="{line}"/><stop offset=".56" stop-color="{accent}"/><stop offset="1" stop-color="{line}"/></linearGradient>
    <clipPath id="bounds"><rect width="{width}" height="{height}"/></clipPath>
  </defs>
  <style>
    .current {{ stroke-dasharray: 170 580; animation: current 24s linear infinite; }}
    @keyframes current {{ to {{ stroke-dashoffset: -750; }} }}
    @media (prefers-reduced-motion: reduce) {{ .current {{ animation: none; stroke-dasharray: none; opacity: .35; }} }}
  </style>
  <g clip-path="url(#bounds)">
    <rect width="{width}" height="{height}" fill="{bg}"/>
    <g transform="translate({wave_x} 20)" stroke="url(#sea)" stroke-width="1" opacity="{wave_opacity}">{''.join(waves)}</g>
    <path class="current" d="M{wave_x-35} 173C{wave_x+60} 117 {wave_x+135} 49 {wave_x+238} 133S{wave_x+366} 273 {wave_x+510} 171" stroke="{accent}" stroke-width="2" opacity=".5"/>
    <g font-family="'Cascadia Code', Consolas, monospace" font-size="{'15' if mobile else '16'}" letter-spacing="1.6" fill="{muted}">
      <text x="{left}" y="42">ZJY-HSBL</text>
      {'' if mobile else f'<text x="1148" y="42" text-anchor="end">RESEARCH / ENGINEERING</text>'}
    </g>
    {name}
    <path d="M{left} {baseline+30}h48" stroke="{accent}" stroke-width="3"/>
    <g font-family="'Segoe UI', Arial, sans-serif">
      <text x="{left}" y="{baseline+81}" fill="{muted}" font-size="{22 if mobile else 24}" letter-spacing=".2">Computer vision. Useful software.</text>
    </g>
    <path d="M{left} {height-14}H{width-left}" stroke="{line}"/>
    <circle cx="{width-left}" cy="{height-14}" r="3" fill="{accent}"/>
  </g>
</svg>
'''


if __name__ == "__main__":
    for theme in ("light", "dark"):
        for mobile in (False, True):
            suffix = f"mobile-{theme}" if mobile else theme
            (ROOT / "assets" / f"header-{suffix}.svg").write_text(render(theme, mobile), encoding="utf-8", newline="\n")
    print("Rendered four self-contained desktop/mobile header SVGs.")
