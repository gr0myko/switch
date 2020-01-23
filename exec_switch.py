import re

a, b, c = 2, 4, 5
d = None


def exec_switch_support(func):
    def wrapper(*args):
        new_args = ''
        cases = {}

        if 'switch' in args[0]:
            args_list = args[0].split('\n')

            for arg in args_list:
                if "break" in arg:
                    index = args_list.index(arg)
                    args_list.pop(index)

            while args_list:
                line = args_list.pop(0)
                if line.startswith('switch'):
                    switch = re.search('switch (.*):', line).group(1)
                    condition = args_list.pop(0)
                    while condition.startswith('    '):
                        if 'case' in condition:
                            case = re.search("case (.*):", condition).group(1)
                        elif condition.startswith('        '):
                            result = ''
                            result += f"{condition.replace(' ', '')}\n\t"
                            if case not in cases:
                                cases[case] = result
                            else:
                                cases[case] += result
                        condition = args_list.pop(0)
                    for num, case in enumerate(cases.keys()):
                        if num == 0:
                            new_args += f"if {switch} == {case}:\n\t" \
                                        f"{cases[case]}"
                        else:
                            new_args = new_args[:-1]
                            new_args += f"elif {switch} == {case}:\n\t" \
                                        f"{cases[case]}\n"
                else:
                    new_args += f"{line}\n"
        else:
            new_args = args[0]
        return func(new_args, globals())
    return wrapper


exec = exec_switch_support(exec)


exec("""
switch a*a:
    case b:
        print('Foo')
        d = 1
        break
    case c:
        print('Bar')
        d = 2
        break

assert d == 1
""")
