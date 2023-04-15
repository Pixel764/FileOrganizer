import os
import shutil

files_extension = {
    'aac', 'adt', 'adts', 'accdb', 'accde', 'accdr', 'accdt', 'aif', 'aifc',
    'aiff', 'aspx', 'avi', 'bat', 'bin', 'bmp', 'cab', 'cda', 'csv', 'dif',
    'dll', 'doc', 'docm', 'docx', 'dot', 'dotx', 'eml', 'eps', 'exe', 'flv',
    'gif', 'htm', 'html', 'ini', 'iso', 'jar', 'jpg', 'jpeg', 'm4a', 'mdb',
    'mid', 'midi', 'mov', 'mp3', 'mp4', 'mpeg', 'mpg', 'msi', 'mui', 'pdf',
    'png', 'pot', 'potm', 'potx', 'ppam', 'pps', 'ppsm', 'ppsx', 'ppt',
    'pptm', 'pptx', 'psd', 'pst', 'pub', 'rar', 'rtf', 'sldm', 'sldx', 'swf',
    'sys', 'tif', 'tiff', 'tmp', 'txt', 'vob', 'vsd', 'vsdm', 'vsdx', 'vss',
    'vssm', 'vst', 'vstm', 'vstx', 'wav', 'wbk', 'wks', 'wma', 'wmd', 'wmv',
    'wmz', 'wms', 'wpd', 'wp5', 'xla', 'xlam', 'xll', 'xlm', 'xls', 'xlsm',
    'xlsx', 'xlt', 'xltm', 'xltx', 'xps', 'zip'
}


class Organizer:
    def __init__(self, path: str):
        self.path = path
        self.errors_logs = []

    def organize(self):
        if not self.is_directory_exists():
            return 'Path doesn\'t exists or path is not dir.'

        self.process()
        return self.errors_logs

    def is_directory_exists(self) -> bool:
        if os.path.exists(self.path):
            if os.path.isdir(self.path):
                if self.path[-1] != '/':
                    self.path += '/'
                return True
        return False

    def process(self) -> None:
        for file in os.listdir(self.path):
            if os.path.isfile(self.path + file):
                try:
                    file_extension = file.split('.')[-1]

                    if file_extension in files_extension:
                        # Check if dir with extension name exists
                        if not os.path.exists(self.path + file_extension):
                            os.mkdir(self.path + file_extension)
                        shutil.move(self.path + file, self.path + file_extension + '/' + file)  # Move file in extension dir
                except Exception:
                    self.errors_logs.append(f'{Exception} | File: {file}')
