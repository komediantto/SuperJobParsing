import scrapy
from scrapy.http import Response

from .call_api import get_phones  # type: ignore


class Vacancies(scrapy.Spider):
    name = "superjob"
    start_urls = ["https://www.superjob.ru/vacancy/search/"]

    def parse(self, response: Response):  # type: ignore
        for link in response.css(  # type: ignore
            "div.f-test-search-result-item a::attr(href)"
        ).getall():
            if link.startswith("/vakansii"):
                id_numbers = link.split("-")[-1].split(".")[0]
                yield response.follow(
                    link, callback=self.parse_vacancy, cb_kwargs=dict(id=id_numbers)
                )

        # Для парсинга всех возможных вакансий можно бесконечно увеличивать номер страницы до возникновений ошибки, так как даже если мы выйдем за пределы 50 - начнутся скрытые от пользователя страницы на самом сайте
        for page in range(1, 3):
            next_page = f"https://www.superjob.ru/vacancy/search/?page={page}"
            yield response.follow(next_page, callback=self.parse)

    def parse_vacancy(self, response: Response, id):
        phones = get_phones(id)
        yield {"name": response.css("h1::text").get(), "phone_number": phones}
