# The Rhode Island Traffic Stops Dataset

## Credit

This dataset is taken from the [Stanford Open Policing Project](https://openpolicing.stanford.edu/). We used the [Kaggle-available version](https://www.kaggle.com/yassershrief/dataset-of-traffic-stops-in-rhode-island) of this dataset.

## Note

We acknowledge that police brutality is an extremely important matter in the United States, where this dataset was created and is being used for analysis in CS1951A at Brown University. The dataset was taken from the Stanford Open Policing Project, which aims to investigate and improve the daily interactions between police and the public. Some data points taken from this data set may have been instances where police brutality happened, which we acknowledge. We foresee no harm being caused by the usage of this dataset in the course, and we hope that the wonderful work happening at the Stanford Open Policing Project can help further the much needed work of police reform in the United States.

## Data Description

Features available in this dataset (and the associated type)
- `stop_year`: The year that a traffic stop happened (`int`)
- `stop_month`: The month that a traffic stop happened (`int`)
- `stop_day`: The day that a traffic stop happened (`int`)
- `stop_time`: The time of day at which a traffic stop happened (`int` - `1`: morning, `2`: afternoon, `3`: evening, `4`: night)
- `stop_duration`: The duration of the traffic stop (`int` - `1`: 0-15 mins, `2`:  16-30 mins, `3`: 30+ mins)
- `county_name`: The county in RI where the stop happened (`str`, categorical variable, **ARTIFICIALLY CONSTRUCTED**)
- `county_fips`: The FIPS code pertaining to the county in RI whhere the stop happened (`int`, **ARTIFICIALLY CONSTRUCTED**)
- `driver_gender`: The gender of the driver who was stopped by the police (`str`, either `M`, `F`)
- `driver_age_raw`: The year of birth of the driver (a number)
- `driver_age`: The age of the driver at the moment of the traffic stop (a number)
- `violation`: The category of violation (`str`, categorical )
- `search_conducted`: Whether a car search was conducted (`bool`)
- `search_type`: The category with which the search was justified (`str`, categorical variable)
- `stop_outcome`: The outcome of the stop (`str`, categorical)
- `is_arrested`: Whether or not the driver is arrested (`bool`)
- `drugs_related_stop`: Whether a stop was drugs related or not (`bool`)