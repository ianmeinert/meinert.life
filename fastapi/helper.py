from pathlib import Path

class FileUtility(object):
    
    @staticmethod
    def readfile(path) -> str:
        with open(path, 'r', encoding='UTF-8') as f:
            return f.read()
        
    @staticmethod
    def load_properties(filepath, sep='=', comment_char='#'):
        """Read the file passed as a properties file

        Args:
            filepath (str): the file to be read
            sep (str, optional): the delimeter used in kvp. Defaults to '='.
            comment_char (str, optional): the comment string char. Defaults to '#'.
        """
        
        props = {}
        
        with open(filepath, 'rt') as f:
            for line in f:
                l = l.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
                    
        return props