from src.real_world.wortraetsel import wordimporter
from src.real_world.wortraetsel.model import Model
from src.real_world.wortraetsel.view import View

wordsToUse = wordimporter.import_words()

model = Model(wordsToUse, 10)

view = View(model)
view.display_on_console()
view.display_in_browser()
