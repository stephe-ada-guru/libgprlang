# Grammar definition for AdaCore gpr language
#
# Language definition in (info "(gnat_ugn) Project Files for gnatxref and gnatfind")

from langkit.parsers import Grammar, List, Or, Opt, Row, Tok

from language.lexer import Token

from language.ast import *

gpr_grammar = Grammar('compilation')
G = gpr_grammar

gpr_grammar.add_rules(
    # rules in alphabetical order
    compilation=Or(G.simple_project),

    declarative_item=Row(G.identifier, ":=", G.expression, ";") ^ DeclarativeItem,
    
    declarative_items=List(G.declarative_item) ^ DeclarativeItems,

    expression=Or(G.identifier) ^ Expression,
    
    identifier=Tok(Token.Identifier, keep=True) ^ Identifier,
    
    simple_project=Row(
        "project", G.identifier, "is", Opt(G.declarative_items), "end", Opt(G.identifier), ";") ^ SimpleProject,
)
