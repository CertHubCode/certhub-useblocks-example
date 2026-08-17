from __future__ import annotations

import shutil
from pathlib import Path

# -- Project information -----------------------------------------------------
project = "Sterilisator 20A — Assurance Evidence"
copyright = "2026, CertHub / Cadence"
author = "CertHub / Cadence"

# -- Paths -------------------------------------------------------------------
_SOURCE_DIR = Path(__file__).resolve().parent
_SPHINX_DIR = _SOURCE_DIR.parent
_PROJECT_ROOT = _SPHINX_DIR.parent
_PLANTUML_JAR = _SPHINX_DIR / "utils" / "plantuml.jar"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx_codelinks",
    "sphinxcontrib.test_reports",
]

templates_path = ["_templates"]
# generated/ holds sync/CodeLinks RST fragments (included by pages; not standalone docs)
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "generated"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["needs_furo.css"]
html_title = "Sterilisator 20A — Assurance Evidence"

# -- PlantUML (needflow / needuml) -------------------------------------------
_plantuml_bin = shutil.which("plantuml")
if _plantuml_bin:
    plantuml = _plantuml_bin
elif _PLANTUML_JAR.is_file():
    plantuml = f"java -jar {_PLANTUML_JAR}"
else:
    plantuml = "plantuml"
plantuml_output_format = "svg"

# -- Sphinx-Needs (shared with ubCode via ubproject.toml) --------------------
needs_from_toml = "ubproject.toml"
# Emit needs.json beside HTML for ubCode Needs JSON view ([needs_json] in ubproject.toml)
needs_build_json = True

src_trace_config_from_toml = "../../codelinks.toml"

tr_rootdir = _PROJECT_ROOT
tr_extra_options = ["certhub_test"]
tr_property_link_types = {
    "verifies": "links",
}
tr_report_template = str(_SOURCE_DIR / "_templates" / "test_report_template.txt")
