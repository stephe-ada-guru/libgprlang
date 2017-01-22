#! /usr/bin/env python

from langkit.utils import Colors

# we run under Emacs, so we don't want ANSI escape sequences
# Do this before anything else so no module copies the sequences
Colors.disable_colors() 

import os

from langkit.libmanage import ManageScript
import langkit.diagnostics


class Manage(ManageScript):

    def __init__(self):
        super(Manage, self).__init__()

        self.test_parser = test_parser = self.subparsers.add_parser(
            'test', help=self.do_test.__doc__)
        test_parser.add_argument(
            'testsuite-args', nargs='*',
            help='Arguments to pass to testsuite.py.')
        test_parser.set_defaults(func=self.do_test)

    def create_context(self, args):
        from langkit.compile_context import CompileCtx

        from language.lexer import gpr_lexer
        from language.parser import gpr_grammar

        return CompileCtx(lang_name='gpr',
                          lexer=gpr_lexer,
                          grammar=gpr_grammar)

    def do_test(self, args):
        """
        Run the testsuite.
        """
        self.set_context(args)

        # Make builds available in env.PATH
        env = self.derived_env()

        argv = [
            'python',
            self.dirs.lang_source_dir('testsuite', 'testsuite.py'),
            '--show-error-output',]
        
        if not args.enable_shared:
            argv.append('--disable-shared')
            
        argv.extend(getattr(args, 'testsuite-args'))

        try:
            self.check_call(args, 'Testsuite', argv, env=env)
        except subprocess.CalledProcessError as exc:
            print >> sys.stderr, 'Testsuite failed: {}'.format(exc)
            sys.exit(1)
        except KeyboardInterrupt:
            # At this point, the testsuite already made it explicit we stopped
            # after a keyboard interrupt, so we just have to exit.
            sys.exit(1)


if __name__ == '__main__':
    Manage().run()

# end of file
