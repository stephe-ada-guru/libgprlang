d# Lexer definition for AdaCore gpr language.
#
# Language definition in (info "(gnat_ugn) Project Files for gnatxref and gnatfind")

from langkit.lexer import Ignore, Lexer, LexerToken, Literal, NoCase, Pattern, WithSymbol, WithText, WithTrivia

class Token(LexerToken):
    # Keywords
    Assign     = WithText()
    End        = WithText()
    Identifier = WithSymbol()
    Is         = WithText()
    Project    = WithText()

    # Punctuation
    Semicolon  = WithText()

    # Trivia
    Comment = WithTrivia()


gpr_lexer = Lexer(Token)

gpr_lexer.add_patterns(
    ('char', r'(\"([0-9A-F][0-9A-F]){2,4}\")'),
    ('identifier',
     r"\$?(\P{ID_Start}|{char})"
     r"(\P{ID_Continue}*|{char})*"),
)

gpr_lexer.add_rules(
    (NoCase("end"),     Token.End),
    (NoCase("is"),      Token.Is),
    (NoCase("project"), Token.Project),

    (Literal(";"),  Token.Semicolon),
    (Literal(":="), Token.Assign),

    (gpr_lexer.patterns.identifier, Token.Identifier),

    (Pattern(r"[ \t\r\n\r\f]+"), Ignore()), # whitespace
)
