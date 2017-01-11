# Lexer definition for AdaCore gpr language.
#
# Language definition in (info "(gnat_ugn) Project Files for gnatxref and gnatfind")

from langkit.lexer import Eof, Lexer, LexerToken, Literal, WithText


class Token(LexerToken):
    Example = WithText()

gpr_lexer = Lexer(Token)
gpr_lexer.add_rules(
    (Eof(),              Token.Termination),
    (Literal("example"), Token.Example),
)
