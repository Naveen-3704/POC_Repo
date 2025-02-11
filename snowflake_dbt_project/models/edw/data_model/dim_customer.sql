{{
  config(
    materialized = "table"
  )
}}

SELECT TOP 1000 *
FROM {{ source('tpcds_sf100tcl', 'customer') }}