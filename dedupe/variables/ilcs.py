import string
import math
import functools

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
'''
        # Add exact match to the distance vector
        self.expanded_size += 1

    def fields(self, field):
        """
        Override the parent method to append an exact match field.
        """
        fields = super().fields(field)
        fields += [('exact match', 'Exact')]
        return fields
'''
