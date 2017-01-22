# Toplevel makefile for gpr langkit project

all : force
	gpr/manage.py --parsable-errors make

generate : force
	gpr/manage.py --parsable-errors generate

build : force
	gpr/manage.py --parsable-errors build

test : all
	gpr/manage.py --parsable-errors test

.PHONY : force

# Local Variables:
# eval: (load-file "prj.el")
# end:
