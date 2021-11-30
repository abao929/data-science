select companies.name
from quotes left join companies on quotes.symbol = companies.symbol
where quotes.num_articles < 11
order by quotes.price desc
limit 1