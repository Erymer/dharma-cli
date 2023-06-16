default: install


PYTHON ?= $(shell \
	     (which python3) \
	     || (python -c 'import sys; sys.exit(sys.version < "3.1")' && \
	      which python) \
			 )
PYTHON_INSTALLER = $(shell (python -c 'import installer' &> /dev/null && echo "0"))
PYTHON_BUILD ?= $(shell (python -c 'import build' &> /dev/null && echo "0"))
PIP = $(shell (which pip))


install: build_dependencies
	@python -m build && python -m installer dist/*.whl
	@install -D -m644 doc/quotebook.txt /etc/quotebook.txt
	@install -D -m644 doc/zennin.1 /usr/share/man/man1/zennin.1


uninstall: uninstall_dependecies
	@pip uninstall zennin
	@rm -rf /etc/quotebook.txt
	@rm -rf /usr/share/man/man1/zennin.1


build_dependencies:
ifeq ($(PYTHON),)
	$(error No suitable Python version installed)
endif

ifeq ($(PYTHON_INSTALLER),)
	$(error Installation requires python-installer module. \
	 				Please install python-installer in your system)
endif

ifeq ($(PYTHON_BUILD),)
	$(error Installation requires python-build module. \
	 				Please install python-build in your system)
endif


uninstall_dependecies:
ifeq ($(PIP),)
	$(error Removing Zennin requires python package manager "pip".\
	 				Please install "python pip" in your system)
endif



.PHONY: default install build_dependencies uninstall uninstall_dependecies
