

class check_comments(object):

    def __init__(self, file):
        self._filename = file
        filesplit = self._filename.split('.')
        self._name = filesplit[0]
        self._type = filesplit[1]
        self.process()

    def process(self):
        f = open(self._filename, 'r')
        lines = f.readlines()
        commentseparator = ()
        if self._type is ".cpp" or ".java":
            commentseparator = ("//", "/*")
        elif self._type is ".py":
            commentseparator = ('"""', '#')
        linecount = 0
        commentcount = 0
        functioncount = 0
        for line in lines:
            linecount += 1
            for separator in commentseparator:
                if separator in line:
                    commentcount += 1
                if "def" in line:
                    functioncount += 1
        self._linecount = linecount
        self._commentcount = commentcount
        self._functioncount = functioncount

    def countComments(self):
        return self._commentcount

    def countLines(self):
        return self._linecount

    def functionCount(self):
        return self._functioncount
