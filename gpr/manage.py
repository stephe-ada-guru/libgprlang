#! /usr/bin/env python

import os

from langkit.libmanage import ManageScript


class Manage(ManageScript):
    def create_context(self, args):
        from langkit.compile_context import CompileCtx

        from language.lexer import gpr_lexer
        from language.parser import gpr_grammar

        return CompileCtx(lang_name='gpr',
                          lexer=gpr_lexer,
                          grammar=gpr_grammar)

if __name__ == '__main__':
    Manage().run()
