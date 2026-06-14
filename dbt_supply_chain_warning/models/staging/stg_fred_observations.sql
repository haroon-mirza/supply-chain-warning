select
    series_id,
    cast(date as date) as observation_date,
    cast(nullif(value, '.') as numeric) as indicator_value
from {{ source('raw', 'bronze_fred_observations') }}
where nullif(value, '.') is not null