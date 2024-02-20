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
    def __init__(self, filedata: str, macros: dict[int|bool] = {}):
        self.uncommented_data: str = ""
        self.macros = macros
        self.unsolved_macros = []
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
        re_define_data = re.compile(r"(?<=#define).*")
        re_define_split = re.compile(r"\s+")
        lines: list[str] = self.uncommented_data.split('\n')
        line_number: int = -1
        for line in lines:
            line_number += 1
            if re.search(re_define, line):
                define_value = re.search(re_define_data, line)
                if not define_value:
                    print("matched a define but didn't found the data : ",line) # maybe throw an exception
                    continue
                elements: list[str] = list(filter(lambda x: x, re.split(re_define_split, define_value.group())))
                isResolved = self.try_resolve_macro(elements)
                if isResolved:
                    self.macros[isResolved[0]] = isResolved[1]
                    self.try_solve_unsolved_macros()
                else:
                    self.unsolved_macros.append(elements)

        print(self.macros)
        return

    def try_solve_unsolved_macros(self):
        for unsolved in self.unsolved_macros:
            isResolved = self.try_resolve_macro(unsolved)
            if isResolved:
                self.macros[isResolved[0]] = isResolved[1]
                del self.unsolved_macros[unsolved]
            

    def resolve_macro(self, key: str, data: any):
        if type(data) is int or type(data) is bool:
            self.macros[key] = data
        else:
            print('could not resolve macro : ' + data )

    def try_resolve_macro(self, list_elements: list[str]):
        elements = list_elements.copy()
        key = elements[0]
        del elements[0]
        if len(elements) == 0:
            return (key, True)
        elements = list(map(lambda el: self.try_resolve_element(el), elements))
        if len(elements) == 1:
            return (key, elements[0])
        if len(elements) % 2:
            for opIndex in range(1, len(elements), 2):
                a = elements[opIndex - 1]
                op = elements[opIndex]
                b = elements[opIndex + 1]
                if type(a) is str or type(b) is str:
                    #print('could not resolve nested macro : ', list_elements)
                    return None
                if op == "+":
                    result = a + b
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
        #print(self.files[2].uncommented_data)

    
    
    

CParser(['back/tests/file1.h', 'back/tests/file2.h', 'back/tests/global.h', 'back/tests/abilities.h'])