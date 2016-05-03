

class check_comments(object):

    def __init__(self, file):
        self._filename = file
        filesplit = self._filename.split('.')
        self._name = filesplit[0]
        self._type = ".py"
        self.process()

    def process(self):
        f = open(self._filename, 'r')
        lines = f.readlines()
        commentseparator = ()
        if self._type == ".py":
            commentseparator = ('"""', '#')
        elif self._type == ".cpp" or self._type == ".java":
            commentseparator = ("//", "/*")
        linecount = 0
        commentcount = 0
        functioncount = 0
        for line in lines:
            linecount += 1
            for separator in commentseparator:
                if separator in line:
                    if separator == '"""':
                        commentcount += 0.5 * line.count('"""')
                    else:
                        commentcount += 1
            if "def" in line:
                functioncount += 1
        self._linecount = linecount
        self._commentcount = int(commentcount)
        self._functioncount = functioncount

    def countComments(self):
        return self._commentcount

    def countLines(self):
        return self._linecount

    def functionCount(self):
        return self._functioncount
