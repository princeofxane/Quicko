.PHONY: build clean

install:
	pip install -r requirements.txt

build: install
	pyinstaller --onefile --add-data "config/config.yaml:config" quicko.py
	./script.sh clean_up_build_fragments
	$(MAKE) clean

clean:
	rm -rf build dist __pycache__ quicko.spec

deposit:
	./script.sh replace_binary

help:
	@echo "Targets:"
	@echo "	build	Build binary"
	@echo "	deposit	Replace the binary with the latest"