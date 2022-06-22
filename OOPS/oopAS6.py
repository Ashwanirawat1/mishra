class ConsoleLogger:
    def log(self, message):
        print(message)

c = ConsoleLogger()
c.log("hello")


class TextFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()

f = open("./PythonDD/textfile.txt", "w")
txt = TextFileLogger(f)
txt.log("Hello Python")
txt.log("Hello Java")

class CSVLogger:
    def __init__(self,file_object):
        self.file_object = file_object
    
    def log(self, message):
        words = message.split()
        from csv import writer
        csv_writer =writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()

f = open("./PythonDD/covid-test.csv", "w")
csv_logger = CSVLogger(f)
csv_logger.log("This is a new String")

class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

# with open("./PythonDD/sample.log") as f:
#     logger = FilteredConsoleLogger ("EVENT")
#     for line in f:
#         logger.log(line)

        


class FilteredTextFileLogger(TextFileLogger):
    def __init__(self,pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

with open("./PythonDD/sample.log") as f:
    with open("./PythonDD/events.txt", "w") as  fw:
         logger = FilteredTextFileLogger ("EVENT", fw)
         for line in f:
             logger.log(line)

class FilteredCSVLogger(CSVLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

with open("./PythonDD/sample.log") as f:
    with open("./PythonDD/covid-test.csv", "w") as fw:
        logger = FilteredCSVLogger("INFO", fw)
        for line in f:
            logger.log(line)


class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)
