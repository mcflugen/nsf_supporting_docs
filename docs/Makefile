MD_SOURCES= \
  Hutton_Bio_Sketch.md \
  Hutton_Current_and_Pending.md \
  Hutton_Statement_of_Work.md \
  Hutton_Budget_Justification.md  \
  Hutton_Facilities_and_Equipment.md \
  Hutton_Results_from_Prior.md \
  Hutton_Results_from_Prior_References.md \
	Project_Personnel.md \
	Data_Management_Plan.md \
	Mentoring_Plan.md
CSV_SOURCES=Hutton_Conflict_of_Interest.csv

WORD_DOCS=${MD_SOURCES:.md=.docx} ${CSV_SOURCES:.csv=.docx}
PDF_DOCS=${MD_SOURCES:.md=.pdf} ${CSV_SOURCES:.csv=.pdf}
HTML_DOCS=${MD_SOURCES:.md=.html} ${CSV_SOURCES:.csv=.html}

TO_PDF_OPTS=-N --variable mainfont="Times New Roman" --variable sansfont="Helvetica" --variable monofont="Courier" --variable fontsize=12pt --latex-engine=xelatex
TO_DOCX_OPTS=--to=docx --reference-docx=templates/nsf_template.docx
TO_HTML_OPTS=--to=html

.SUFFIXES : .md .csv .docx .pdf .html

.md.html:
	pandoc ${TO_HTML_OPTS} $< -o $@

.md.pdf:
	pandoc --to=latex $< ${TO_PDF_OPTS} -o $@

.md.docx:
	pandoc ${TO_DOCX_OPTS} $< -o $@

.csv.md:
	../scripts/coi_to_caa.py $< > $@

all: docx

docx: ${WORD_DOCS}
	mv Hutton_Conflict_of_Interest.docx Hutton_Collaborators_and_Affiliations.docx

pdf: ${PDF_DOCS}
	mv Hutton_Conflict_of_Interest.pdf Hutton_Collaborators_and_Affiliations.pdf

html: ${HTML_DOCS}
	mv Hutton_Conflict_of_Interest.html Hutton_Collaborators_and_Affiliations.html

clean:
	rm -f ${WORD_DOCS} ${PDF_DOCS} ${HTML_DOCS} Hutton_Collaborators_and_Affiliations.docx Hutton_Collaborators_and_Affiliations.pdf Hutton_Collaborators_and_Affiliations.html
