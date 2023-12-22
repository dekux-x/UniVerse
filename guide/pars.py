
import requests
from bs4 import BeautifulSoup
from .models import Grant, GrantsList
class Pars():
    url = "https://www.testcenter.kz/ru/press-tsentr/novosti/detail.php?ID=6266"

    def do_pars(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find("table")
        rows = table.find_all("tr")
        grants_programs = []
        grants = GrantsList()
        grants_list = grants.get_list()
        for row in rows[2:210]:
            cells = row.find_all("td")
            if len(cells) >= 6:  # Убедитесь, что есть достаточно ячеек
                program_code = cells[1].text.strip() if len(cells) == 7 else cells[0].text.strip()
                program_name = cells[2].text.strip() if len(cells) == 7 else cells[1].text.strip()
                grant_count = cells[3].text.strip() if len(cells) == 7 else cells[2].text.strip()
                grants_programs.append({"Код программы": program_code, "Название программы": program_name, "Грантов": grant_count})
        grant_objects = [
            Grant(code=data["Код программы"], name=data["Название программы"], amount=data["Грантов"], year=2023, max=grant_info["max"], min=grant_info["min"])
            for data in grants_programs for grant_info in grants_list if data["Код программы"] == grant_info["Код"] ]
        Grant.objects.bulk_create(grant_objects)
