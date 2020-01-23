import inspect


def switch_support(func):
    def wrapper(*args):
        args_name = inspect.getfullargspec(func)[0]
        args_dict = dict(zip(args_name, args))
        parsed_docstring = [s.replace(':', '').lstrip() for s in
                            func.__doc__.split('\n') if s.strip()]
        cases = {}
        while parsed_docstring:
            s = parsed_docstring.pop(0)
            if 'switch' in s:
                switch = s.split()[1]
            elif 'case' in s:
                case = s.split(' ', 1)[1]
                if case in args_dict.keys():
                    case = args_dict[case]
                try:
                    case = int(case)
                except ValueError:
                    case = eval(case)
                result = parsed_docstring.pop(0).split()[1]
                cases[case] = int(result)
        if switch in args_dict.keys():
            switch = args_dict[switch]
        return cases[switch]
    return wrapper


@switch_support
def test_function(a, b, c, d):
    """
    switch a:
         case b:
              return 1
         case c:
              return 2
         case d:
              return 3
         case sum([1, 14, -2, 4]):
              return 4
    """
