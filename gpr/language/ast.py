# Annotated Syntax Tree types for gpr language

from langkit.compiled_types import abstract, ASTNode, Field, root_grammar_class, T

from langkit.expressions import Property, Self

## abstract classes
@abstract
@root_grammar_class()
class gprNode(ASTNode):
    """
    Root node class for gpr AST nodes.
    """

@abstract
class SingleTokNode(gprNode):
    tok = Field(type=T.Token)
    name = Property(Self.tok)


## concrete classes
class DeclarativeItem(gprNode):
    lhs = Field(type=T.Identifier)
    rhs = Field(type=T.Expression)

class DeclarativeItems(gprNode):
    items = Field(type=T.DeclarativeItem.list_type())

class Expression(gprNode):
    exp = Field(type=T.Identifier) # FIXME: or string literal, list ...
    
class Identifier(SingleTokNode):
    _repr_name = "Id"

class SimpleProject(gprNode):
    name   = Field(type=T.Identifier)
    items  = Field(type=T.DeclarativeItems)
    end_id = Field(type=T.Identifier)

class StringLiteral(SingleTokNode):
    _repr_name = "Str"

# end of file

