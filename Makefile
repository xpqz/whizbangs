# Repeatable PDF -> Markdown pipeline for the Collected Whizbangs booklet.
#
#   make extract   PDF  -> build/{pages,text,bps}           (deterministic)
#   make build     src/pages/*.md -> docs/collected-whizbangs.md
#   make lint      APL fidelity checks on every code fence
#   make all       extract, build, lint
#
# The transcription of record is src/pages/*.md. Everything in build/ is
# derived and can be deleted at any time.

PDF := 197808_APL Plus Collected WhizBangs_P036-0878.pdf
OUT := docs/collected-whizbangs.md
PAGES := $(sort $(wildcard src/pages/*.md))

.PHONY: all extract build lint review clean check-tools corrected site serve

all: build lint

extract:
	bash tools/extract.sh

build: $(OUT)

$(OUT): $(PAGES) tools/build.py
	python3 tools/build.py

lint:
	python3 tools/lint_apl.py

lint-list:
	python3 tools/lint_apl.py --list

# Rebuild the review crops that each transcription was checked against.
# Any code fence in the sources is re-rendered from the PDF at 1200dpi.
review:
	@mkdir -p build/review
	@echo "review crops live in build/review/; regenerate any block with:"
	@echo "  tools/crop.sh PAGE X Y W H DPI build/review/NAME.png"

# Corrected copy and the Zensical site built from it (needs: python3 -m venv .venv && .venv/bin/pip install zensical).
ZENSICAL ?= .venv/bin/zensical

corrected:
	python3 tools/mkcorrected.py

site: corrected
	python3 tools/mksite.py
	$(ZENSICAL) build

serve: corrected
	python3 tools/mksite.py
	$(ZENSICAL) serve

check-tools:
	@for t in pdftotext pdftoppm pdfinfo tesseract python3; do \
	  command -v $$t >/dev/null || echo "missing: $$t"; \
	done

clean:
	rm -rf build

.PHONY: FORCE
FORCE:
