# Cadence — CertHub SaMD Engineering Loop: sync, evidence pack, CertHub release push.

UV ?= uv
ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
export PYTHONPATH := $(ROOT)src:$(ROOT)certhub
DASHBOARD := $(ROOT)sphinx/build/html/dashboard.html

VERSION ?=
RC ?= 1
BASELINE ?= $(VERSION)

CERTHUB_TOML := $(ROOT)certhub.toml

# Tenant settings via shared Pydantic reader (no ad-hoc tomllib).
TECHDOC_BASE_URL := $(shell cd "$(ROOT)" && $(UV) run cadence config-get techdoc_base_url 2>/dev/null)
RECORDS_BASE_URL := $(shell cd "$(ROOT)" && $(UV) run cadence config-get records_base_url 2>/dev/null)
TRACER_BASE_URL := $(shell cd "$(ROOT)" && $(UV) run cadence config-get tracer_base_url 2>/dev/null)

#=======================================================================================================================
# OpenAPI codegen (Tech Doc + Records + Tracer)
#=======================================================================================================================
SCHEMA_DIR = schemas
CLIENT_DIR = certhub/certhub_connector/api/clients
MODEL_DIR = certhub/certhub_connector/api/api_models

TECHDOC_SCHEMA_FILE = $(SCHEMA_DIR)/techdoc.json
RECORDS_SCHEMA_FILE = $(SCHEMA_DIR)/records.json
TRACER_SCHEMA_FILE = $(SCHEMA_DIR)/tracer.json

TECHDOC_CLIENT_DIR = $(CLIENT_DIR)/techdoc
RECORDS_CLIENT_DIR = $(CLIENT_DIR)/records
TRACER_CLIENT_DIR = $(CLIENT_DIR)/tracer
TECHDOC_MODEL_DIR = $(MODEL_DIR)/techdoc
RECORDS_MODEL_DIR = $(MODEL_DIR)/records
TRACER_MODEL_DIR = $(MODEL_DIR)/tracer

.PHONY: help install sync show evidence break fix clean \
	test test-connector test-samd \
	tag-rc tag-release push-evidence confirm ensure-plantuml \
	open-requirements open-release-record \
	init-schemas fetch-techdoc-schema fetch-records-schema fetch-tracer-schema \
	filter-techdoc-schema filter-records-schema filter-tracer-schema \
	generate-techdoc-client generate-records-client generate-tracer-client \
	generate-techdoc-models generate-records-models generate-api

help:
	@echo "Cadence — CertHub SaMD Engineering Loop"
	@echo ""
	@echo "Learner (start here — no API key)"
	@echo "  make install                      Install deps (uv)"
	@echo "  make show                         Tests + CodeLinks + verify + open dashboard"
	@echo "  make evidence                     CI evidence pack under evidence/ (no browser)"
	@echo "  make break / make fix             RED/GREEN gate"
	@echo "  make test                         Connector + SaMD tests (no API key)"
	@echo ""
	@echo "Talk to CertHub (needs CERTHUB_API_KEY)"
	@echo "  make sync                         Sync CertHub → Sphinx-Needs + snapshot"
	@echo "  make confirm BASELINE=0.0.99      # live POST+GET proof"
	@echo "  make tag-rc VERSION=1.0.0 RC=1"
	@echo "  make tag-release VERSION=1.0.0"
	@echo "  make push-evidence BASELINE=1.0.0 # dry-run RecordCreate body"
	@echo "  make open-requirements            Open System Requirements KT in CertHub"
	@echo "  make open-release-record          Open Release Record KT in CertHub"
	@echo "  make test-connector               Connector tests only"
	@echo "  make test-samd                    SaMD verification tests only"
	@echo "  make clean"
	@echo ""
	@echo "Maintainer"
	@echo "  make generate-api                 DEV ONLY — regenerate OpenAPI clients"

install:
	$(UV) sync

test: install
	$(UV) run pytest tests src/sterilisator_20a/tests -q

test-connector: install
	$(UV) run pytest tests -q

test-samd: install
	$(UV) run pytest src/sterilisator_20a/tests -q

ensure-plantuml:
	bash scripts/ensure_plantuml.sh

sync: install
	$(UV) run cadence sync

# Continues after pytest/verify failure so RED still builds + opens the dashboard.
# Exits non-zero when the certification gate is BLOCKED.
show: install ensure-plantuml
	mkdir -p reports reports/codelinks_raw sphinx/source/generated
	-$(UV) run pytest --junitxml=reports/junit.xml
	$(UV) run python scripts/run_codelinks.py
	@status=0; \
	$(UV) run cadence verify || status=$$?; \
	$(UV) run cadence report; \
	rm -rf sphinx/build/html; \
	$(UV) run sphinx-build -b html sphinx/source sphinx/build/html; \
	echo ""; \
	echo "Dashboard: $(DASHBOARD)"; \
	echo "Opening $(DASHBOARD)"; \
	open "$(DASHBOARD)" 2>/dev/null || xdg-open "$(DASHBOARD)" 2>/dev/null || \
		python3 -c "import webbrowser; webbrowser.open('file://$(DASHBOARD)')"; \
	exit $$status

# CI-friendly cousin of show: same gate, no browser; writes evidence/.
evidence: install ensure-plantuml
	mkdir -p reports reports/codelinks_raw sphinx/source/generated
	-$(UV) run pytest --junitxml=reports/junit.xml
	$(UV) run python scripts/run_codelinks.py
	@status=0; \
	$(UV) run cadence verify || status=$$?; \
	$(UV) run cadence report; \
	rm -rf sphinx/build/html; \
	$(UV) run sphinx-build -b html sphinx/source sphinx/build/html; \
	$(UV) run cadence package-evidence || status=$$?; \
	echo "Evidence pack: $(ROOT)evidence/"; \
	exit $$status

tag-rc:
	@test -n "$(VERSION)" || (echo "USAGE: make tag-rc VERSION=1.0.0 RC=1"; exit 2)
	$(UV) run python scripts/tag_release.py rc --version "$(VERSION)" --rc "$(RC)" --push

tag-release:
	@test -n "$(VERSION)" || (echo "USAGE: make tag-release VERSION=1.0.0"; exit 2)
	$(UV) run python scripts/tag_release.py release --version "$(VERSION)" --push

# Dry-run by default. Set CERTHUB_PUSH=1 to POST.
push-evidence: install
	@test -n "$(BASELINE)" || (echo "USAGE: make push-evidence BASELINE=1.0.0"; exit 2)
	$(UV) run cadence push-evidence --baseline "$(BASELINE)" --from evidence

# Live round-trip proof. Example: make confirm BASELINE=0.0.99
confirm: evidence
	@test -n "$(BASELINE)" || (echo "USAGE: make confirm BASELINE=0.0.99"; exit 2)
	$(UV) run cadence confirm --baseline "$(BASELINE)" --from evidence

open-requirements: install
	$(UV) run cadence open-requirements

open-release-record: install
	$(UV) run cadence open-release-record

break:
	@python3 scripts/gate_mutate.py break
	@echo "Broken. Run: make show"

fix:
	@python3 scripts/gate_mutate.py fix
	@echo "Restored. Run: make show"

clean:
	rm -rf sphinx/build reports/junit.xml reports/codelinks_analysis.json
	rm -rf reports/codelinks_raw
	# Keep committed Sphinx-Needs catalog RST; remove only per-build fragments + raw API dumps.
	rm -f sphinx/source/generated/codelinks_needextend.rst \
		sphinx/source/generated/certification_summary.rst
	rm -rf certhub/generated/*
	rm -rf evidence
	rm -rf .pytest_cache
	mkdir -p sphinx/source/generated certhub/generated
	touch sphinx/source/generated/.gitkeep certhub/generated/.gitkeep
	@echo "Cleaned generated artifacts (catalog RST kept)."

# ---- Schema fetch + client/model generation ----

init-schemas:
	mkdir -p $(SCHEMA_DIR) $(CLIENT_DIR) $(MODEL_DIR)

fetch-techdoc-schema: init-schemas install
	@test -f "$(CERTHUB_TOML)" || (echo "Missing $(CERTHUB_TOML)"; exit 2)
	@test -n "$(TECHDOC_BASE_URL)" || (echo "techdoc_base_url missing in certhub.toml"; exit 2)
	@echo "Fetching TechDoc schema from $(TECHDOC_BASE_URL)..."
	curl -fSL -o $(TECHDOC_SCHEMA_FILE) "$(TECHDOC_BASE_URL)/openapi.json"
	@echo "Validating TechDoc schema (best-effort)..."
	@$(UV) run --group codegen openapi-spec-validator $(TECHDOC_SCHEMA_FILE) \
		|| echo "WARNING: openapi-spec-validator failed for TechDoc (continuing)"

fetch-records-schema: init-schemas install
	@test -f "$(CERTHUB_TOML)" || (echo "Missing $(CERTHUB_TOML)"; exit 2)
	@test -n "$(RECORDS_BASE_URL)" || (echo "records_base_url missing in certhub.toml"; exit 2)
	@echo "Fetching Records schema from $(RECORDS_BASE_URL)..."
	curl -fSL -o $(RECORDS_SCHEMA_FILE) "$(RECORDS_BASE_URL)/openapi.json"
	@echo "Validating Records schema (best-effort)..."
	@$(UV) run --group codegen openapi-spec-validator $(RECORDS_SCHEMA_FILE) \
		|| echo "WARNING: openapi-spec-validator failed for Records (continuing)"

fetch-tracer-schema: init-schemas install
	@test -f "$(CERTHUB_TOML)" || (echo "Missing $(CERTHUB_TOML)"; exit 2)
	@test -n "$(TRACER_BASE_URL)" || (echo "tracer_base_url missing in certhub.toml"; exit 2)
	@echo "Fetching Tracer schema from $(TRACER_BASE_URL)..."
	curl -fSL -o $(TRACER_SCHEMA_FILE) "$(TRACER_BASE_URL)/openapi.json"
	@echo "Validating Tracer schema (best-effort)..."
	@$(UV) run --group codegen openapi-spec-validator $(TRACER_SCHEMA_FILE) \
		|| echo "WARNING: openapi-spec-validator failed for Tracer (continuing)"

# Keep only @public_api / x-public: true operations (same contract as CertHub docs).
filter-techdoc-schema: fetch-techdoc-schema
	$(UV) run python -m certhub_connector.api.filter_public $(TECHDOC_SCHEMA_FILE)

filter-records-schema: fetch-records-schema
	$(UV) run python -m certhub_connector.api.filter_public $(RECORDS_SCHEMA_FILE)

filter-tracer-schema: fetch-tracer-schema
	$(UV) run python -m certhub_connector.api.filter_public $(TRACER_SCHEMA_FILE)

generate-techdoc-client: filter-techdoc-schema
	rm -rf $(TECHDOC_CLIENT_DIR)
	mkdir -p $(CLIENT_DIR)
	$(UV) run --group codegen openapi-python-client generate \
		--path $(TECHDOC_SCHEMA_FILE) \
		--output-path $(TECHDOC_CLIENT_DIR) \
		--meta none \
		--overwrite

generate-records-client: filter-records-schema
	rm -rf $(RECORDS_CLIENT_DIR)
	mkdir -p $(CLIENT_DIR)
	$(UV) run --group codegen openapi-python-client generate \
		--path $(RECORDS_SCHEMA_FILE) \
		--output-path $(RECORDS_CLIENT_DIR) \
		--meta none \
		--overwrite

generate-tracer-client: filter-tracer-schema
	rm -rf $(TRACER_CLIENT_DIR)
	mkdir -p $(CLIENT_DIR)
	$(UV) run --group codegen openapi-python-client generate \
		--path $(TRACER_SCHEMA_FILE) \
		--output-path $(TRACER_CLIENT_DIR) \
		--meta none \
		--overwrite

generate-techdoc-models: filter-techdoc-schema
	mkdir -p $(TECHDOC_MODEL_DIR)
	$(UV) run --group codegen python -m datamodel_code_generator \
		--input $(TECHDOC_SCHEMA_FILE) \
		--output $(TECHDOC_MODEL_DIR)/techdoc_models.py \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--output-datetime-class datetime \
		--use-standard-collections \
		--use-union-operator \
		--collapse-root-models \
		--target-python-version 3.12

generate-records-models: filter-records-schema
	mkdir -p $(RECORDS_MODEL_DIR)
	$(UV) run --group codegen python -m datamodel_code_generator \
		--input $(RECORDS_SCHEMA_FILE) \
		--output $(RECORDS_MODEL_DIR)/records_models.py \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--output-datetime-class datetime \
		--use-standard-collections \
		--use-union-operator \
		--collapse-root-models \
		--target-python-version 3.12

generate-api: generate-techdoc-client generate-records-client generate-tracer-client \
	generate-techdoc-models generate-records-models
	@echo ""
	@echo "Generated public-only TechDoc + Records + Tracer clients; TechDoc + Records Pydantic models."
	@echo "  schemas: $(SCHEMA_DIR)/  (x-public filtered)"
	@echo "  clients: $(CLIENT_DIR)/"
	@echo "  models:  $(MODEL_DIR)/ (no tracer Pydantic — attrs client models only)"
	@rm -rf $(TRACER_MODEL_DIR)
