import scrapy
import json


class DivanSpider(scrapy.Spider):
    name = "divan"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Получаем все элементы с товарами диваны
        divan_items = response.css('div._c9h0M_')

        # Проходим по каждому товару
        for item in divan_items:
            yield {
                'name': item.css('div.lsooF span::text').get(),  # Название товара
                'price': item.css('div.pY3d2 span::text').get(),  # Цена товара
                'url': response.urljoin(item.css('a').attrib['href'])  # Ссылка на товар с полным URL
            }

        # Переход на следующую страницу (если есть пагинация)
        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

# Чтение и вывод данных из сохраненного JSON-файла:
with open('C:/Users/a0803/PycharmProjects/PS05/divan_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Если файл содержит список товаров, выводим их
if isinstance(data, list):
    for item in data:
        print(item)  # Печатаем каждый элемент списка
