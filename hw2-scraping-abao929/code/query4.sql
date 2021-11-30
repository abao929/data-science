select location, count(*)
from companies
group by location
order by location asc