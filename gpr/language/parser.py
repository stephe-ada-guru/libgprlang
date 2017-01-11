# Grammar definition for AdaCore gpr language
#
# Language definition in (info "(gnat_ugn) Project Files for gnatxref and gnatfind")

from langkit.compiled_types import ASTNode, abstract, root_grammar_class
from langkit.parsers import Grammar, Row


@abstract
@root_grammar_class()
class gprNode(ASTNode):
    """
    Root node class for gpr AST nodes.
    """
    pass

class ExampleNode(gprNode):
    pass

gpr_grammar = Grammar('main_rule')
gpr_grammar.add_rules(
    main_rule=Row('example') ^ ExampleNode
)
