import sys, re
class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)  #return the method we need, and check if callable
        if callable(method): return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):                         #come back and comment later
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:  result = match.group(0)
            return result
        return substitution


class HTMLRender(Handler):
    def start_table(self):
        print('<table border="1">')
    def end_table(self):
        print('</table>')
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self, match):
        return '<a href= "%s">%s<\a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def feed(self, data):
        if data[0:13] != 'table_note_rp':
            print(data)
            return

        data = re.sub('table_note_rp', '', data)
        data = data.splitlines()
        first_line = 1
        for row in data:
            print('<tr>')
            words = row.split()
            first_column = 1

            for word in words:
                if first_column or first_line:
                    first_column = 0
                    print('<th>')
                    print(word)
                    print('</th>')
                else:
                    print('<td>')
                    print(word)
                    print('</td>')

            print('</tr>')
            first_line = 0







#some space
