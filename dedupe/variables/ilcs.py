import numpy
import ilcs_parser
from parseratorvariable import ParseratorType

CITATION = (
    ('chapter', ('Chapter',)),
    ('act prefix', ('ActPrefix',)),
    ('section', ('Section',)),
    ('subsection', ('SubSection',)),
)


class ILCSType(ParseratorType):
    type = 'ILCS'

    def tagger(self, field):
        return self.tag(field)

    def __init__(self, definition):
        self.components = (('Citation', self.compareFields, CITATION),)
        block_parts = ('Citation',)
        super().__init__(definition, ilcs_parser.tag, block_parts)
        # Add exact match and attempted indicators to the distance vector
        self.num_additional_indicators = 2
        self.expanded_size += self.num_additional_indicators

    def fields(self, field):
        """
        Override the parent method to append an exact match field.
        """
        fields = super().fields(field)
        fields += [('attempted match', 'Dummy'), ('exact match', 'Exact')]
        return fields

    def comparator(self, field_1, field_2):
        """
        Override the parent method to append an exact match field.
        """
        # Temporarily subtract the exact and attempted match indicators from
        # expanded_size, since the parent method assumes that the last element
        # of the distance vector is the full-string comparison
        self.expanded_size -= self.num_additional_indicators
        distances = super().comparator(field_1, field_2)
        self.expanded_size += self.num_additional_indicators

        # Set the attempted match indicator variable
        try:
            parsed_variable_1 = self.tagger(field_1)
            parsed_variable_2 = self.tagger(field_2)
        except TypeError:
            attempted = 0
        else:
            variable_type_1, variable_type_2 = parsed_variable_1[1], parsed_variable_2[1]
            if 'Ambiguous' in (variable_type_1, variable_type_2):
                attempted = 0
            else:
                attempted = int(parsed_variable_1.is_attempted == parsed_variable_2.is_attempted)
        distances = numpy.append(distances, attempted)

        # Set the exact match indicator variable
        exact_match = 1 if field_1 == field_2 else 0
        distances = numpy.append(distances, exact_match)

        return distances
