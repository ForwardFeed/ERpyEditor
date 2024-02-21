import re

'''
    functions to parse the C
'''

# a list of rules to parse a selected
parsingList = [
    ("property", "regexDetect", "regexGrab"),
    ("changeParsingList")
]


class CParsibleFile:
    def __init__(self, filedata: str, macros: dict[int|bool] = {}, unsolved = []):
        self.uncommented_data: str = ""
        self.macros = macros
        self.unsolved_macros = unsolved
        # 0 => do not read
        # 1 => please read
        # 2 => do not read and do not set to read until next endif
        self.is_ok_to_read: int = 1
        self.lines_ok_to_read: list[str] = []
        self.filter_c_comments(filedata)
        self.grab_macro_definition()
    
    def filter_c_comments(self, filedata:str):
        regex_single = re.compile('\/\/[^\r\n]*')
        regex_multiple = re.compile('\/\*+[^*]*\*\/', re.DOTALL)
        self.uncommented_data = re.sub(regex_multiple, '', re.sub(regex_single, '', filedata))

    # in order not to mangle the c processing macros
    def filterMacros(self):
        lines: list[str] = self.uncommented_data.split('\n')
        line_number: int = -1
        for line in lines:
            line_number += 1
        return
    
    # take the list of macros definition in the file
    def grab_macro_definition(self):
        re_define = re.compile(r"#define")
        re_directive = re.compile(r"#(if)|(else)|(endif)|(elif)")
        lines: list[str] = self.uncommented_data.split('\n')
        line_number: int = -1
        for line in lines:
            line_number += 1
            if re.search(re_directive,line):
                self.found_directive(line)
            if self.is_ok_to_read == 1:
                self.lines_ok_to_read.append(line_number)
            if re.search(re_define, line):
                self.found_define(line)  
            print(line)

        while self.try_solve_unsolved_macros():
            continue

    def found_directive(self, line):
        re_directive = re.compile(r"(?<=#)((if)|(else)|(endif)|(elif))\w*")
        directive = re.search(re_directive, line)
        if not directive:
            print("could not find directive : " + line)
            return
        directive = directive.group()
        if directive == "else":
            if self.is_ok_to_read == 0:
                self.is_ok_to_read = 1
            elif self.is_ok_to_read == 1:
                self.is_ok_to_read = 0
            return
        if directive == "endif":
            self.is_ok_to_read = 1
            return
        re_directive_data = re.compile(r"(?<=" + directive + "\s).*")
        directive_data = re.search(re_directive_data, line)
        if not directive_data:
            print("could not find directive data: " + line)
            return
        directive_data = directive_data.group()
        if directive == "ifdef":
            if directive_data in self.macros:
                self.is_ok_to_read = 1
            else:
                self.is_ok_to_read = 0
            return
        elif directive == "ifndef":
            if directive_data in self.macros:
                self.is_ok_to_read = 0
            else:
                self.is_ok_to_read = 1
            return
        re_split = re.compile(r"\s+")
        re_remove_parenthesis = re.compile(r"[\(\)]")
        parenths = list(filter(lambda el: el , re.split(re_remove_parenthesis, directive_data)))
        resolve = ""
        if len(parenths) == 1:
            elements = re.split(re_split, parenths[0])
            elements.insert(0, '_')
            resolve = self.resolve_machine(elements)
        elif not len(parenths) % 3:
            a = re.split(re_split, parenths[0])
            a.insert(0, '_')
            op = parenths[1]
            b = re.split(re_split, parenths[2])
            b.insert(0, '_')
            resolve = ['_', self.resolve_machine(a), op, self.resolve_machine(b)]
        else:
            print("could not resolve directive data : " + line)
            resolve = False
        
        if directive == "if":    
            if resolve and resolve[1]:
                self.is_ok_to_read = 1
            else:
                self.is_ok_to_read = 0
        elif directive == "elif":
            if self.is_ok_to_read == 1:
                self.is_ok_to_read = 2
            elif resolve and resolve[1]:
                self.is_ok_to_read = 1
                
    
    def found_define(self, line):
        re_define_data = re.compile(r"(?<=#define).*")
        re_define_split = re.compile(r"\s+")
        re_remove_parenthesis = re.compile(r"[\(\)]")
        define_value = re.search(re_define_data, line)
        if not define_value:
            print("matched a define but didn't found the data : ",line) # maybe throw an exception
            return
        elements = list(filter(lambda x: x, re.split(re_define_split, define_value.group())))
        elements = list(map(lambda el: re.sub(re_remove_parenthesis, '', el), elements))
        if not self.try_resolve_macro(elements):
            self.unsolved_macros.append(elements)
        else:
            self.try_solve_unsolved_macros()
    
    def try_solve_unsolved_macros(self):
        oneSolvedAtLeast = False
        indexToRemove = []
        lenA = len(self.unsolved_macros)
        for i in range(0, lenA):
            unsolved = self.unsolved_macros[i]
            result = self.try_resolve_macro(unsolved)
            if result:
                indexToRemove.append(i)
                oneSolvedAtLeast = True
        
        ohohohomickey = 0
        for index in indexToRemove:
            del self.unsolved_macros[index - ohohohomickey]
            ohohohomickey += 1
        return oneSolvedAtLeast

    def resolve_macro(self, key: str, data: any):
        if type(data) is int or type(data) is bool:
            self.macros[key] = data
        else:
            print('could not resolve macro : ' + data )

    def try_resolve_macro(self, elements: list[str]):
        isResolved = self.resolve_machine(elements)
        if isResolved:
            self.macros[isResolved[0]] = isResolved[1]
        return bool(isResolved)

    def resolve_machine(self, __elements__: list[str]):
        elements = __elements__.copy()
        key = elements[0]
        del elements[0]
        if len(elements) == 0:
            return (key, True)
        elements = list(map(lambda el: self.try_resolve_element(el), elements))
        if len(elements) == 1:
            a = elements[0]
            if type(a) is str:
                return None
            return (key, a)
        if len(elements) % 2:
            for opIndex in range(1, len(elements), 2):
                a = elements[opIndex - 1]
                op = elements[opIndex]
                b = elements[opIndex + 1]
                if type(a) is str:
                    a = False
                if type(b) is str:
                    b = False
                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == ">=":
                    result = a >= b
                elif op == "==":
                    result = a == b
                elif op == "<=":
                    result = a <= b
                elif op == ">":
                    result = a > b
                elif op == "<":
                    result = a < b
                elif op == "!=":
                    result = a != b
                elif op == "||":
                    result = bool(a or b)
                elif op == "&&":
                    result = bool(a and b)
                else:
                    print('could not determine operator : ' + str(op))
                    return None
                elements[opIndex + 1] = result
            return (key, elements[-1])
        if len(elements) % 2:
            print("how am i to resolve this : " + elements)
            return None


    def try_resolve_element(self, element: str):
        resolve = None
        if element.isdigit():
            resolve = int(element)
        elif re.match(r"(\|\|)|(\&\&)|(\+)", element):
            resolve = element
        elif element in self.macros:
            resolve = self.macros[element]
        else:
            resolve = element
        return resolve
    


class CParser:
    def __init__(self, files_path: list[str]):
        self.files_path: list[str] = files_path
        self.files: list[CParsibleFile] = []
        self.read_files()
    
    def read_files(self):
        for file_path in self.files_path:
            with open(file_path, 'r') as file:
                self.files.append(CParsibleFile(file.read()))
            #print(self.files[0].unsolved_macros)

    
if __name__ == '__main__':
    #CParser(['back/tests/file1.h', 'back/tests/file2.h', 'back/tests/global.h', 'back/tests/abilities.h'])
    #CParser(['back/tests/items.h'])
    CParser(['back/tests/global.h', 'back/tests/abilities.h'])