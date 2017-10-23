class HtmlOutputer():
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write("<html>")
            f.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
            f.write("<body>")
            f.write('<table>')
            for data in self.datas:
                f.write('<tr>')
                f.write('<td width="100px">%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'])
                f.write('<td>%s</td>' % data['summary'])
                f.write('</tr>')
            f.write('</table>')
            f.write("</body>")
            f.write("</html>")
