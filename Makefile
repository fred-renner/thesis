#!/bin/bash
FILE=main
FILES=`ls -1 */*.tex`

all: $(FILE).tex
	# ./prepBib.sh
	latex ${FILE}.tex
	bibtex ${FILE}
	# ./feynmaenner.sh
	latex ${FILE}.tex
	latex ${FILE}.tex

spell:  
	for file in $(FILES); do \
	aspell -t -c $${file}; \
	done;

ps: $(FILE).dvi
	dvips ${FILE}.dvi

pdf: $(FILE).dvi
	dvipdf ${FILE}.dvi

clean:
	rm -f *.bbl *.blg *.dvi *.lof *.aux *.lot *.out *.toc *.ps *.dvi *.log *.toc *.600gf *.600pk *.log *.mf *.t1 *.tfm *.synctex.gz *.fdb_latexmk *.fls
