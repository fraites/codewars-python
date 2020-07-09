import re
class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        regex = re.compile('\d+_(.*)\..*')
        file_name = regex.search(dirty_file_name)
        return file_name.group(1)
