
all: documento.pdf

documento.pdf: documento.tex bibliografia.bib
	pdflatex documento.tex
	biber documento
	pdflatex documento.tex
	pdflatex documento.tex

clean:
	rm -f *.aux *.blg *.bbl *.toc *.log *.lof *.lot *.log.xml *.bcf *.out documento.pdf *.run.xml
