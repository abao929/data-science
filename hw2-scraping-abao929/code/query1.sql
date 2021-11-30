select quotes.symbol, companies.name
from quotes left join companies on quotes.symbol = companies.symbol
order by quotes.price/quotes.avg_price desc
limit 1