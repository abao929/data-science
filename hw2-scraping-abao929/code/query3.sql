select companies.symbol, companies.name
from quotes left join companies on quotes.symbol = companies.symbol
where quotes.price > 35 and abs(quotes.price - quotes.avg_price) < 5
order by abs(quotes.price - quotes.avg_price) asc