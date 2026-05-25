"""Static artifact contracts for the RetractionImpact single-file app."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = REPO_ROOT / "index.html"
README = REPO_ROOT / "README.md"
ASSET_RE = re.compile(r'<(?:link|script)[^>]+(?:href|src)="([^"]+)"', re.IGNORECASE)


def test_readme_methods_are_reflected_in_app_shell() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    assert "# RetractionImpact" in readme
    assert "Retraction Fragility Index" in readme
    assert "<title>RetractionImpact" in html
    assert "Retraction Fragility Quantifier" in html
    assert "Max retraction depth" in html
    assert "reverses statistical significance" in html


def test_core_plots_and_exports_exist() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")

    expected_markers = [
        "waterfallCanvas",
        "fragilityCanvas",
        "looCanvas",
        "baujatCanvas",
        "goshCanvas",
        "temporalCanvas",
        "radialCanvas",
        "doiCanvas",
        "exportCSV()",
        "exportPlot('waterfallCanvas','retraction_waterfall')",
    ]

    for marker in expected_markers:
        assert marker in html


def test_local_assets_resolve() -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")
    assets = ASSET_RE.findall(html)

    assert assets, "expected at least one linked local asset"

    missing = [
        asset
        for asset in assets
        if not asset.startswith(("http://", "https://"))
        if not (REPO_ROOT / asset).resolve().is_file()
    ]
    assert not missing, f"missing linked assets: {missing}"
