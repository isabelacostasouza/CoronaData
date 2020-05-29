# Database

In addition to storing data from different sources, it will be necessary to store the CSV of the structured data obtained on the drive.

### Database structure
| TABLE | COLUMNS | RELATIONSHIP |
| ------ | ------ | ------ |
| State           | acronym, name  |                                           |
| City            | id_ibge, name  | city (1 state to n cities)                |
| Segmented Data  | date, raw_text | city (1 city for n segmented data)        |
| Structured Data | deaths, ICU's.. | (1 data_segumented to 1 structured data) |