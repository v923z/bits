import simplejson

class NotebookSearch(object):

    def __init__(self, fn):
        with open(fn, 'r') as fin:
            self.notebook = simplejson.load(fin)

    def search_string(self, string, cell_type=['code']):
        for worksheet in self.notebook['worksheets']:
            for cell in worksheet['cells']:
                for ct in cell_type:
                    if self.search_in_cell(cell, string, ct) is True: return True
            return False

    def search_in_cell(self, cell, string, cell_type, extra=['input']):
        if cell['cell_type'] in cell_type:
            if cell['cell_type'] in ('code'):
                if 'input' in extra:
                    for line in cell['input']:
                        if string in line: return True
                if 'outputs' in extra:
                    for sub_cell in cell['outputs']:
                        if sub_cell['output_type'] in 'stream':
                            for line in sub_cell['text']:
                                if string in line: return True
                    
            if cell['cell_type'] in ('markdown', 'raw', 'heading'):
                    for line in cell['source']:
                        if string in line: return True                

        return False
