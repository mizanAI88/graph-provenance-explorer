PYTHON ?= python
PACKAGE = graph_provenance_explorer

.PHONY: setup smoke demo test evaluate export-graph figure clean

setup:
	pip install -e . && pip install pytest

smoke:
	$(PYTHON) -m $(PACKAGE) smoke

demo:
	$(PYTHON) -m $(PACKAGE) demo

test:
	$(PYTHON) -m pytest -q

evaluate:
	$(PYTHON) -m $(PACKAGE) evaluate --mode all

export-graph:
	$(PYTHON) -m $(PACKAGE) export-graph

figure:
	$(PYTHON) tools/render_figure.py

clean:
	rm -rf examples/output/smoke examples/output/evaluate .pytest_cache
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
