#!/usr/bin/env bash
# Download PlantUML jar when the system `plantuml` binary is unavailable.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JAR_DIR="${ROOT}/sphinx/utils"
JAR="${JAR_DIR}/plantuml.jar"
VERSION="1.2024.8"
URL="https://github.com/plantuml/plantuml/releases/download/v${VERSION}/plantuml-${VERSION}.jar"

if command -v plantuml >/dev/null 2>&1; then
  echo "Using system plantuml: $(command -v plantuml)"
  exit 0
fi

if [[ -f "${JAR}" ]]; then
  echo "PlantUML jar present: ${JAR}"
  exit 0
fi

mkdir -p "${JAR_DIR}"
echo "Downloading PlantUML ${VERSION} → ${JAR}"
curl -fsSL -o "${JAR}" "${URL}"
echo "Done."
