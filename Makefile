# wykys LaTeX Makefile

LATEX = pdflatex
FLAGS = -halt-on-error -interaction=nonstopmode

NAME = book
PDF_READER = zathura

.PHONY: clean

# make document
all: $(NAME)
	$(LATEX) $(FLAGS) $(NAME).tex
	$(LATEX) $(FLAGS) $(NAME).tex
	ps -a | grep $(PDF_READER) || $(PDF_READER) $(NAME).pdf
