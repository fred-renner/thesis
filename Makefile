#!/bin/bash
FILE=main
FILES=`ls -1 */*.tex`

all: $(FILE).tex
	# ./prepBib.sh
	pdflatex ${FILE}.tex
	bibtex ${FILE}
	# ./feynmaenner.sh
	pdflatex ${FILE}.tex
	pdflatex ${FILE}.tex

spell:  
	for file in $(FILES); do \
	hunspell -t -l $${file}; \
	done;

ps: $(FILE).dvi
	dvips ${FILE}.dvi

pdf: $(FILE).dvi
	dvipdf ${FILE}.dvi

clean:
	rm -f *.bbl *.blg *.dvi *.lof *.aux *.lot *.out *.toc *.ps *.dvi *.log *.toc *.600gf *.600pk *.log *.mf *.t1 *.tfm *.synctex.gz *.fdb_latexmk *.fls
