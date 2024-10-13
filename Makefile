.PHONY: build clean

clean:
	rm -rf build dist __pycache__ quicko.spec

build:
	pyinstaller --onefile quicko.py
	./script.sh
	$(MAKE) clean




	