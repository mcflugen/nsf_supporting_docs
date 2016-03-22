#! /usr/bin/env python
from __future__ import print_function

import os
import argparse
import csv

_TEMPLATE = """
# Collaborators and Other Affiliations #

## Eric Hutton ##

*The Institute of Arctic and Alpine Research*  
*University of Colorado*

### Collaborators and Co-Editors ({number_of_collaborators}) ###

{collaborators}

### Graduate Advisors and Postdoctoral Sponsors ({number_of_advisors}) ###

{advisors}

### Thesis Advisor and Postdoctoral Sponsor ({number_of_advisees}) ###

{advisees}
""".strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='CSV-file of conflicts')
    parser.add_argument('--output',
                        type=argparse.FileType('w'),
                        help='Output markdown file')
    
    args = parser.parse_args()

    reader = csv.reader(args.file, delimiter=',')

    collaborators = []
    advisors = []
    advisees = []
    for row in reader:
        last, first, institute, ctype = (row[3].strip(), row[4].strip(),
                                         row[5].strip(), row[6].strip())

        # name, institute, ctype = (row[2].strip(), row[3].strip(),
        #                           row[4].strip())
        name = '{last}, {first}'.format(last=last, first=first)
        if ctype == 'Collaborator':
            collaborators.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        elif row[-1].strip() == 'Advisor':
            advisors.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        elif row[-1].strip() == 'Advisee':
            advisees.append("1. {name} ({institute})".format(
                name=name, institute=institute))
        else:
            warnings.warn(
                '{type}: conflict type not understood'.format(type=ctype))

    print(_TEMPLATE.format(collaborators=os.linesep.join(collaborators),
                           number_of_collaborators=len(collaborators),
                           advisors=os.linesep.join(advisors),
                           number_of_advisors=len(advisors),
                           advisees=os.linesep.join(advisees),
                           number_of_advisees=len(advisees)),
         file=args.output)


if __name__ == '__main__':
    main()
