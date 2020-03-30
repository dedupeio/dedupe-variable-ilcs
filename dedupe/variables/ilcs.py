import ilcs_parser
from parseratorvariable import ParseratorType

CITATION = (
    ('chapter', ('Chapter',)),
    ('act prefix', ('ActPrefix')),
    ('section', ('Section')),
    ('subsection', ('SubSection')),
    ('attempted', ('Attempted'))
)


class ILCSType(ParseratorType):
    type = 'ILCS'

    def tagger(self, field):
        return self.tag(field)

    def __init__(self, definition):
        self.components = (('Citation', self.compareFields, CITATION),)
        block_parts = ('Citation',)
        super().__init__(definition, ilcs_parser.tag, block_parts)
