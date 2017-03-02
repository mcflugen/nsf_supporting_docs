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

### Graduate Advisors ({number_of_advisors}) ###

{advisors}

### PhD Advisor ({number_of_advisees}) ###

{advisees}
""".strip()


Conflict = namedtuple('Conflict', ['first', 'last', 'institute', 'type'])


def render_conflict(conflict):
    return '1. {last}, {first} (*{institute}*)'.format(**conflict._asdict())


def render_conflict_list(conflicts):
    conflict_list = []
    for conflict in conflicts:
        conflict_list.append(render_conflict(conflict))
    return conflict_list


def render_document(conflicts):
    collaborators = render_conflict_list(conflicts.get('Collaborator', []))
    advisors = render_conflict_list(conflicts.get('Advisor', []))
    advisees = render_conflict_list(conflicts.get('Advisee', []))

    return _TEMPLATE.format(
        collaborators=os.linesep.join(collaborators or ['None']),
        number_of_collaborators=len(collaborators),
        advisors=os.linesep.join(advisors or ['None']),
        number_of_advisors=len(advisors),
        advisees=os.linesep.join(advisees or ['None']),
        number_of_advisees=len(advisees))


def load_conflicts(path_to_file, with_header=True):
    reader = csv.reader(path_to_file, delimiter=',')
    if with_header:
        reader.next()

    conflicts = [Conflict(row[4], row[3], row[5], row[6]) for row in reader]
    conflicts.sort(cmp=lambda a, b: cmp(a.last, b.last))

    conflict_groups = defaultdict(list)
    for conflict in conflicts:
        if conflict.type not in ['Collaborator', 'Advisor', 'Advisee']:
            warnings.warn(
                '{type}: conflict type not understood'.format(type=conflict.type))
        else:
            conflict_groups[conflict.type].append(conflict)

    return conflict_groups


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
    conflicts = load_conflicts(args.file, with_header=args.with_header)

    print(render_document(conflicts), file=args.output)


if __name__ == '__main__':
    main()
