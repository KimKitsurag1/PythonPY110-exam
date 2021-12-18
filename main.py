import json
import random

import faker

def generator(model : str, pk : int, fake:object) -> dict :
    d={}  # коненчный словарь
    faker.Faker.seed(pk) #сид для генераторов
    d['model'] = model
    d['pk'] = pk
    fields = {}
    def get_title(): #получение названия книги
        with open('books.txt', encoding='utf-8') as titles:
            title_list=[i for i in titles]
            title=random.choice(title_list)
        return title

    fields['title'] = get_title()

    def get_year():#получение года выпуска
        year=random.randint(1900, 2021)
        return year

    fields['year'] = get_year()

    def get_number_of_pages():#получение количества страниц
        pages=random.randint(25, 1000)
        return pages

    fields['pages'] = get_number_of_pages()

    def get_isbn13():#получение isbn13
        return fake.isbn13()

    fields['isbn13'] = get_isbn13()

    def get_rating():#получение рейтинга
        return random.uniform(1., 5.)

    fields['rating'] = get_rating()

    def get_price():#получение цены
        return random.uniform(random.random()*random.normalvariate(100, 10), random.random()*random.normalvariate(100, 10))

    fields['price'] = get_price()

    def get_author():#получение списка авторов
        authors=[]
        author_count=random.randint(1,3)
        for i in range(author_count):
            authors.append(fake.name())
        return authors

    fields['author']=get_author()

    d['fields']=fields
    return d

def main():
    fake = faker.Faker() #генерация объекта для получения isbn и авторов
    from conf import MODEL
    spisok=[0]*100
    for i in range(100):
        spisok[i]=generator(MODEL,i+1,fake)
    with open("output.json", "w") as f:
        json.dump(spisok, f, indent=4, ensure_ascii=False)
if __name__ == "__main__":
    main()