import string
import math
import functools

import ilcs_parser
import numpy
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

    def compareFields(self, parts, field_1, field_2):
        """
        Override the base comparison function to provide more semantically
        meaningful comparisons of field_1 and field_2, depending on the type
        of the field.
        """
        joinParts = functools.partial(consolidate, components=parts)
        for part, (part_1, part_2) in zip(parts, zip(*map(joinParts, [field_1, field_2]))):
            if part == ('Attempted',):
                # We expect Attempted indicators like "(att)" to be strings
                yield self.compareString(part_1, part_2)
            else:
                if part_1.isdigit() and part_2.isdigit():
                    # If the fields are both all numeric, compare as numbers.
                    # Use root difference so that each additional unit of
                    # difference is less significant as the delta gets large
                    yield math.sqrt(abs(int(part_1) - int(part_2)))
                else:
                    def is_single_alpha(x): return len(x) == 1 and set(x.lower()) < set(string.ascii_lowercase)
                    if is_single_alpha(part_1) and is_single_alpha(part_2):
                        # Both fields are single alphabetic characters, like
                        # 'a', so we can compare the alphabetic distance.
                        # Use root difference to scale the delta as the distance
                        # across the alphabet grows
                        def get_alpha_idx(x): return string.ascii_lowercase.index(x.lower())
                        yield math.sqrt(abs(get_alpha_idx(part_1) - get_alpha_idx(part_2)))
                    else:
                        yield self.compareString(part_1, part_2)
