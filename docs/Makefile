MD_SOURCES= \
  Hutton_Bio_Sketch.md \
  Hutton_Current_and_Pending.md  \
  Hutton_Statement_of_Work.md \
  Hutton_Budget_Justification.md  \
  Hutton_Facilities_and_Equipment.md \
  Hutton_Results_from_Prior.md \
  Hutton_CSDMS_2_References.md \
	Hutton_CSDMS_2_Abstracts.md \
	Project_Personnel.md \
	Data_Management_Plan.md \
	Mentoring_Plan.md
CSV_SOURCES=Hutton_Conflict_of_Interest.csv
DOCS=${MD_SOURCES:.md=.docx} ${CSV_SOURCES:.csv=.docx}
PDF_DOCS=${MD_SOURCES:.md=.pdf} ${CSV_SOURCES:.csv=.pdf}

OPTIONS=-N --template=template.tex --variable mainfont="Arial" --variable sansfont="Helvetica" --variable monofont="Courier" --variable fontsize=12pt --latex-engine=xelatex

.SUFFIXES : .md .csv .docx .pdf

.md.pdf:
	pandoc --to=latex $< ${OPTIONS} -o $@

.md.docx:
	pandoc --to=docx $< -o $@

.csv.pdf:
	../scripts/coi_to_caa.py $< | pandoc --to=latex ${OPTIONS} -o $@

.csv.docx:
	../scripts/coi_to_caa.py $< | pandoc --to=docx -o $@

all: docx

docx: ${DOCS}
	mv Hutton_Conflict_of_Interest.docx Hutton_Collaborators_and_Affiliations.docx

pdf: ${PDF_DOCS}
	mv Hutton_Conflict_of_Interest.pdf Hutton_Collaborators_and_Affiliations.pdf

clean:
	rm -f ${DOCS} ${PDF_DOCS} Hutton_Collaborators_and_Affiliations.docx Hutton_Collaborators_and_Affiliations.pdf
