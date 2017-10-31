# wykys LaTeX Makefile

LATEX = pdflatex
FLAGS = -halt-on-error -interaction=nonstopmode

NAME = book

.PHONY: clean

# make document
all: $(NAME)
		$(LATEX) $(FLAGS) $(NAME).tex
		$(LATEX) $(FLAGS) $(NAME).tex
		$(LATEX) $(FLAGS) $(NAME).tex
