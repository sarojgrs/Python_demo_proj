from abc import ABC, abstractmethod
import os
import time


class FileProcessor(ABC):
    data: str

    @abstractmethod
    def load(self, filepath):
        pass

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def save(self, outputFilePath) -> str:
        return self.data


class CsvFileProcessor(FileProcessor):
    data: str

    def load(self, filepath):
        print(f"loading csv file {filepath}")
        data = 'Csv file data'
        return super().load(filepath)

    def format(self):
        print("Formatting CSV file")
        self.data = 'Formatting CSV file data'
        return super().format()

    def process(self):
        print("Processing CSV file")
        self.data += " Processed"
        pass

    # def save(self, outputFilePath) -> str:
    #     print(f"Saving CSV file to: {outputFilePath}")
    #     # save data
    #     print("CSV file saved: {outputFilePath}")
    #     return self.data

    def save(self, outputFilePath) -> str:
        print(f"Saving CSV file to: {outputFilePath}")
        # save data
        print("CSV file saved: {outputFilePath}")
        return self.data
        # return super().save(outputFilePath)


class XmlFileProcessor(FileProcessor):
    data: str

    def load(self, filepath):
        print(f"loading Xml file {filepath}")
        data = 'Xml file data'
        return super().load(filepath)

    def format(self):
        print("Formatting Xml file")
        self.data = 'Formatting Xml file data'
        return super().format()

    def process(self):
        print("Processing Xml file")
        self.data += " Processed"
        pass

    def save(self, outputFilePath) -> str:
        print(f"Saving Xml file to: {outputFilePath}")
        # save data
        print("Xml file saved: {outputFilePath}")
        return self.data


class FileProcessorFactory(ABC):
    @abstractmethod
    def createFileProcessor():
        pass


class CsvFileProcessorFactory(FileProcessorFactory):
    def createFileProcessor(self):
        return CsvFileProcessor()


class XmlFileProcessorFactory(FileProcessorFactory):
    def createFileProcessor(self):
        return XmlFileProcessor()


class FactoryMethodImplementation:
    def CreateFileProcessorFactory(self, fileExtension: str):
        if fileExtension.lower() == '.csv':
            return CsvFileProcessorFactory()
        elif fileExtension.lower() == '.xml':
            return XmlFileProcessorFactory()
        else:
            return None

    def run(self) -> str:
        inputFiles = ["file2.xml", "file1.csv"]
        result: str = ""
        for input_file in inputFiles:
            file_extension = os.path.splitext(input_file)[1]
            factory = self.CreateFileProcessorFactory(file_extension)

            if (factory is not None):
                fileProcessor = factory.createFileProcessor()
                # series of process..
                outputFilePath = "output file" + input_file + file_extension
                fileProcessor.load(input_file)
                fileProcessor.format()
                fileProcessor.process()
                data = fileProcessor.save(outputFilePath)
                # result += data
                yield data

            else:
                print(f"unsupported file format {file_extension}")

        return result
