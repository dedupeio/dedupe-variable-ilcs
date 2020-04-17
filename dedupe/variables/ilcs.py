import string
import math
import functools

import numpy
import ilcs_parser
from parseratorvariable import ParseratorType, consolidate

CITATION = (
    ('chapter', ('Chapter',)),
    ('act prefix', ('ActPrefix',)),
    ('section', ('Section',)),
    ('subsection', ('SubSection',)),
    ('attempted', ('Attempted',))
)


class ILCSType(ParseratorType):
    type = 'ILCS'

    def tagger(self, field):
        return self.tag(field)

    def __init__(self, definition):
        self.components = (('Citation', self.compareFields, CITATION),)
        block_parts = ('Citation',)
        super().__init__(definition, ilcs_parser.tag, block_parts)
        # Add exact match to the distance vector
        self.expanded_size += 1

    def fields(self, field):
        """
        Override the parent method to append an exact match field.
        """
        fields = super().fields(field)
        fields += [('exact match', 'Exact')]
        return fields

    def comparator(self, field_1, field_2):
        """
        Override the parent method to append an exact match field.
        """
        # Temporarily subtract the exact match indicator from expanded_size,
        # since the parent method assumes that the last element of the distance
        # vector is the full-string comparison.
        self.expanded_size -= 1
        distances = super().comparator(field_1, field_2)
        self.expanded_size += 1

        # Set the exact match indicator variable.
        exact_match = 1 if field_1 == field_2 else 0
        distances = numpy.append(distances, exact_match)

        return distances
