import numpy as np
import argparse
'''https://docs.python.org/3/library/argparse.html'''

def Operation(x,y,minus,verbose,list, inspect):
    if verbose:
        print("{} ^ {} equals {}".format(x, y, x**y))
    else:
        print(x**y)
    print("Above answer minus {} is {}".format(minus, x**y-minus))
    print('The list output is:', list)
    print('boolen inspect is:', inspect)

if __name__=='__main__':
    '''
    Step 1: Using the argparse is creating an ArgumentParser object
            ----------------------------------------------------------------------------
            Parameters:

            prog - The name of the program (default: sys.argv[0])
            usage - The string describing the program usage (default: generated from arguments added to parser)
            description - Text to display before the argument help (default: none)
            epilog - Text to display after the argument help (default: none)
            parents - A list of ArgumentParser objects whose arguments should also be included
            formatter_class - A class for customizing the help output
            prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
            fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)
            argument_default - The global default value for arguments (default: None)
            conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
            add_help - Add a -h/--help option to the parser (default: True)
            allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)

    '''
    parser = argparse.ArgumentParser(prog='Argparse_Test', description='Process some integers.')


    '''
    Step 2: Filling an ArgumentParser with information about program arguments.

            Generally, these calls tell the ArgumentParser how to take the strings on the command line and turn them into objects.
            This information is stored and used when parse_args() is called.
            ----------------------------------------------------------------------------
            Parameters:

            name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
            action - The basic type of action to be taken when this argument is encountered at the command line.
            nargs - The number of command-line arguments that should be consumed.
            const - A constant value required by some action and nargs selections.
            default - The value produced if the argument is absent from the command line.
            type - The type to which the command-line argument should be converted.
            choices - A container of the allowable values for the argument.
            required - Whether or not the command-line option may be omitted (optionals only).
            help - A brief description of what the argument does.
            metavar - A name for the argument in usage messages.
            dest - The name of the attribute to be added to the object returned by parse_args().
    '''
    # Positional argument (will be called automatically, and must assign a value for this variable)
    parser.add_argument(
        'x',
        # This is a positional argument.
        help='x is the base',
        type=int
    )

    parser.add_argument(
        'y',
        # This is a positional argument.
        help='y is the exponent',
        type=int
    )

    # Optional argument (will skip if not assigned)
    parser.add_argument(
        '--minus',
        # in case of having 1 letter optional argument, we only need '-',
        # '--' is for multiple letters optional argument.
        help='minus the assigned value',
        type=float,
        # type: https://docs.python.org/3/library/argparse.html#type
        default=3.1415926
    )

    parser.add_argument(
        '-v',
        '--verbose',
        # -v and --verbose have same effect. -v is a short option for --verbose
        action='store_true',
        # action: https://docs.python.org/3/library/argparse.html#action
        # if -v with out assigned value appears in option. verbose = Trueself.
        help='increase output verbosity'
    )

    # Optional argument (will skip if not assigned)
    parser.add_argument(
        '--list-haha',
        help='This input should be a list rather than a individual value.' ,
        nargs='*',
        default=[1,2,3],
        # nargs: https://docs.python.org/3/library/argparse.html#nargs
        # '*'. All command-line arguments present are gathered into a list.
        # nargs generally are not used on positional argument.
        type=float
    )
    
    # by default, it is False, but in case of having it appearing as flag, it would be True
    parser.add_argument(
    	'--inspect-input',
    	action='store_true',
    	default=False,
    	help='inspect input tensors'
    )
    
    parser.add_argument(
    	'--dropout',
    	default=0,
    	type=int,
    	choices=range(0, 10)
    )


    '''
    Step 3: ArgumentParser parses arguments through the parse_args() method.

            This will inspect the command line, convert each argument to the appropriate type
            and then invoke the appropriate action.
    '''
    args=parser.parse_args()
    print(args.__dict__)
    Operation(args.x, args.y, args.minus, args.verbose, args.list_haha, args.inspect_input)
