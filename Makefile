default: install

PYTHON ?= $(shell \
	     (which python3) \
	     || (python -c 'import sys; sys.exit(sys.version < "3.1")' && \
	      which python) \
			 )
PYTHON_INSTALLER = $(shell (python -c 'import installer' &> /dev/null || echo "1"))
PYTHON_BUILD ?= $(shell (python -c 'import build' &> /dev/null || echo "1"))

install: check_build_dependencies
	python -m build
	python -m installer dist/*.whl
	cp example-file.dharma /etc/quotebook.txt

check_build_dependencies:
ifeq ($(PYTHON),)
	$(error No suitable Python version installed)
endif
ifeq ($(PYTHON_INSTALLER), 1)
	$(error Installation requires python-installer module. \
	 				Please install python-installer in your system)
endif
ifeq ($(PYTHON_BUILD), 1)
	$(error Installation requires python-build module. \
	 				Please install python-build in your system)
endif


.PHONY: default install check_build_dependencies
