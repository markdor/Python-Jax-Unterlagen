import random


class HtmlCreator:
    def __init__(self, model):
        self.model = model

    def export_as_html(self):
        result = """     <html>
                             <head>
                                  <style>
                                     td {
                                         font-size: 18pt;
                                     }
                                 </style>
                             </head>
                         <body>
                         """

        result += self.create_table()
        result += self.create_word_list()

        result += """        </body>
                         </html>
                         """

        return result

    def create_word_list(self):
        result = "<ul>"

        for word in self.model.get_words_to_search():
            result += "<li>" + word + "</li>"

        result += "</ul>"
        result += "\n"

        return result

    def create_table(self):
        result = "<table border = '3' style='text-align:center'"
        result += "\n"

        for y in range(self.model.get_board_height()):
            result += "<tr>"
            for x in range(self.model.get_board_width()):
                result += "<td>" + self.model.get_at(x, y) + "</td>"
            result += "</tr>"
            result += "\n"

        result += "</table>"

        # result += "<ul>"
        # for (String word: getWordsToSearch())
        # result += "<li>" + word + "</li>";
        #
        # result += "</ul>"
        result += """
                                    </body>
                                </html>
                                """
        return result
