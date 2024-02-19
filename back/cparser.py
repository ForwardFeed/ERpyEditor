import re

'''
    functions to parse the C
'''

# a list of rules to parse a selected
parsingList = [
    ("property", "regexDetect", "regexGrab"),
    ("changeParsingList")
]


# filter C comments
def filterCComments(filepath):
    
    with open(filepath, 'r') as file:
        line = re.sub(regexSingleLineComment,'',line)

# filter C pre processing macros
def filterMacros(filepath):
    print

# basic reading files
def readFile(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().split('\n')
        lineNumber = 0
        for line in lines:
            print(line)
            lineNumber += 1


class CParser:
    def __init__(self, filesPath):
        self.filesPath = filesPath
        self.uncommentedData = ""
        self.readFiles()
    
    def readFiles(self):
        for filepath in self.filesPath:
            with open(filepath, 'r') as file:
                self.uncommentedData += self.filterCComments(file.read())
        print(self.uncommentedData)

    def filterCComments(self, filedata: list[str]):
        regexSingle = re.compile('\/\/[^\r\n]*')
        regexMultiple = re.compile('\/\*+[^*]*\*\/', re.DOTALL)
        return re.sub(regexMultiple, '', re.sub(regexSingle, '', filedata))
    
CParser(['back/tests/file1.h', 'back/tests/file2.h'])