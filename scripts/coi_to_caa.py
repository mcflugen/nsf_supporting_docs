#! /usr/bin/env python
from __future__ import print_function

import os
import argparse
import csv
import warnings
from collections import namedtuple, defaultdict

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


Conflict = namedtuple('Conflict', ['first', 'last', 'institute', 'type'])


def render_document(conflicts):
    collaborators = conflicts['Collaborator']
    advisors = conflicts['Advisor']
    advisees = conflicts['Advisee']

    return _TEMPLATE.format(
        collaborators=os.linesep.join(collaborators or ['None']),
        number_of_collaborators=len(collaborators),
        advisors=os.linesep.join(advisors or ['None']),
        number_of_advisors=len(advisors),
        advisees=os.linesep.join(advisees or ['None']),
        number_of_advisees=len(advisees))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='CSV-file of conflicts')
    parser.add_argument('--no-header', dest='with_header',
                        action='store_false', default=True,
                        help='The input file does not contain a header line')
    parser.add_argument('--output',
                        type=argparse.FileType('w'),
                        help='Output markdown file')
    
    args = parser.parse_args()

    reader = csv.reader(args.file, delimiter=',')
    if args.with_header:
        reader.next()

    conflicts = defaultdict(list)
    for row in reader:
        conflict = Conflict(row[3], row[4], row[5], row[6])
        item = '1. {last}, {first} ({institute})'.format(**conflict._asdict())
        if conflict.type not in ['Collaborator', 'Advisor', 'Advisee']:
            warnings.warn(
                '{type}: conflict type not understood'.format(type=ctype))
        else:
            conflicts[conflict.type].append(item)

    print(render_document(conflicts), file=args.output)


if __name__ == '__main__':
    main()
