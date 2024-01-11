import cianparser
data = cianparser.parse(
    deal_type="rent_long",
    accommodation_type="flat",
    location="Москва",
    rooms=(2, 3),
    start_page=1,
    end_page=2,
    is_saving_csv=True,
)