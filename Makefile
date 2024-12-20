.PHONY: build clean

clean:
	rm -rf build dist __pycache__ quicko.spec

build:
	pyinstaller --onefile quicko.py
	./script.sh clean_up_build_fragments
	$(MAKE) clean

deposit:
	./script.sh replace_binary

help:
	@echo "Targets:"
	@echo "	build	Build the binary and clean up scraps."
	@echo "	deposit	Replace the binary with the latest"
	