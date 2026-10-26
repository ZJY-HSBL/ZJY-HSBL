# Profile design notes

Redesigned on 2026-10-26. This is the GitHub profile repository, not a separate hosted website.

## References

- [RyMe.md / Sleek Hero](https://github.com/ryanpolasky/ryme.md/blob/main/src/lib/templates/sleek-header.ts): studied its use of a large name, restrained metadata, one accent, and a self-contained SVG. The Sea Field wordmark, outlined Chinese lettering and contour artwork in this repository are original; the template code is not copied.
- [Anurag Hazra](https://github.com/anuraghazra/anuraghazra): a distinct typographic introduction followed by concise work and project links.
- [Tw93](https://github.com/tw93/tw93): a short introduction with direct product and release links.
- [Brian-Ckwu](https://github.com/Brian-Ckwu/Brian-Ckwu): selected publications with clear venues and resource links.

The current design uses a sea-contour identity, a neutral light/dark palette with one teal accent, a compact project directory, an actual product screenshot, and expandable secondary material. Mobile gets a separate header composition rather than a scaled-down desktop banner.

## Sources and maintenance

Project descriptions and technologies are based on the corresponding repository READMEs. ScolioVision is described as a manual four-point measurement research prototype. Vitrunda remains a preview. Iterduca's screenshot is the public application screenshot using demonstration data. The original publication titles, author positions, DOIs, counts and awards are retained.

The four SVGs in `assets/` are the deployable assets and require no external font or image service. Chinese name glyphs are outlined. To regenerate the wordmark on Windows, install `fonttools` and run `python scripts/render_header.py`; the generator reads the installed Microsoft YaHei Bold font. The generated SVGs include accessible descriptions, have no scripts, and respect reduced-motion preferences. Existing technical icons and contribution-snake generation are retained.

Verification covers Unicode, local asset paths, preserved publication links, XML validity, deterministic generation, and static header rendering. Browser inspection was stopped by the computer-use URL safety check, so the actual GitHub page and responsive layout were not visually verified in a live browser.
