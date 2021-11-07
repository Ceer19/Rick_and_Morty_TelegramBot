from translate import translate


def processing(response):
    name = response.json()["results"][0]["name"]
    earth = response.json()["results"][0]["origin"]["name"]
    image = response.json()["results"][0]["image"]
    status = response.json()["results"][0]["status"]
    gender = response.json()["results"][0]["gender"]
    species = response.json()["results"][0]["species"]
    return f"📟 <b>Данные по персонажу</b> 📟\n" \
           f"<b>Имя</b> {name}\n" \
           f"<b>Планета</b> {earth}\n" \
           f"<b>Статус</b> {translate(status)}\n" \
           f"<b>Пол</b> {translate(gender)}\n" \
           f"<b>Раса</b> {translate(species)}\n"\
           f"{image}"


def random_params(response):
    name = response.json()["name"]
    earth = response.json()["origin"]["name"]
    status = response.json()["status"]
    gender = response.json()["gender"]
    species = response.json()["species"]
    image = response.json()["image"]
    return f"📟 <b>Данные по персонажу</b> 📟\n" \
           f"<b>Имя</b> {name}\n" \
           f"<b>Планета</b> {earth}\n" \
           f"<b>Статус</b> {translate(status)}\n" \
           f"<b>Пол</b> {translate(gender)}\n" \
           f"<b>Раса</b> {translate(species)}\n"\
           f"{image}"

