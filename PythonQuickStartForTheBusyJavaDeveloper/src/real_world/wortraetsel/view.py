import webbrowser
from os import path

from src.real_world.wortraetsel.htmlcreator import HtmlCreator


class View:
    def __init__(self, model):
        self.model = model

    def display_on_console(self):
        for y in range(self.model.get_board_height()):
             for x in range(self.model.get_board_width()):
                print(self.model.get_at(x, y), end ="")
             print()

        print("Search for: ", self.model.get_words_to_search())

    def display_in_browser(self):
        html_file = self.create_html()

        path_ = path.realpath(html_file.name)
        print(path_)
        #webbrowser.get("firefox").open_new_tab("file:///" + path_)
        webbrowser.open_new_tab("file:///" + path_)

    def create_html(self):
        html = HtmlCreator(self.model).export_as_html()

        html_file = open("words.html", "w+", encoding='utf-8')
        html_file.write(html)

        return html_file

