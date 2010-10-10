all: MontyCarlo.pdf

MontyCarlo.tex: MontyCarlo.Plw
	Pweave -f tex MontyCarlo.Plw

MontyCarlo.pdf: MontyCarlo.tex
	pdflatex MontyCarlo.tex
	pdflatex MontyCarlo.tex
	pdflatex MontyCarlo.tex