# File Errata / Known Issues

There are known issues with the 2011-2021 Alaska Energy Statistics Workbooks. Since this repository is to host the deliverable of the workbooks, we maintain this errata as opposed to directly addressing the issues in the workbooks. We record known issues by workbook in the following sections. The [table of contents](#table-of-contents) allows you to quickly move around the errata. 

# Table of Contents
## General Issues
- The Eva Creek Wind Farm is a power plant in the GVEA service territory that goes by "Eva Creek" from 2011 to 2013, and then "Eva Creek Wind" from 2014 onward.

## File Specific Issues
- [2022 Alaska Energy Statistics Workbook](#2022-alaska-energy-statistics-workbook)
- [2021 Alaska Energy Statistics Workbook](#2021-alaska-energy-statistics-workbook)
- [2020 Alaska Energy Statistics Workbook](#2020-alaska-energy-statistics-workbook)
- [2015 Alaska Energy Statistics Workbook](#2015-alaska-energy-statistics-workbook)
- [2014 Alaska Energy Statistics Workbook](#2014-alaska-energy-statistics-workbook)
- [2013 Alaska Energy Statistics Workbook](#2013-alaska-energy-statistics-workbook)
- [2012 Alaska Energy Statistics Workbook](#2012-alaska-energy-statistics-workbook)

## 2022 Alaska Energy Statistics Workbook

> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2022_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2022_AK_Energy_Statistics.xlsx)

- Bradley Lake data from the EIA does not match utility purchase data as reported to the Regulatory Commission of Alaska (RCA). In particular, the following difference is found: `EIA 376,661 MWh -- Utility purchases 367,214 MWh`.

## 2021 Alaska Energy Statistics Workbook

> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2021_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2021_AK_Energy_Statistics.xlsx)

- Bradley Lake data from the EIA does not match utility purchase data as reported to the Regulatory Commission of Alaska (RCA). In particular, the following difference is found: `EIA 391,018 MWh -- Utility purchases 421,446 MWh`.

## 2020 Alaska Energy Statistics Workbook

> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2020_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2020_AK_Energy_Statistics.xlsx)

- `Table 2.5a` Data from EIA861S needs to be scrutinized. Customer-level data are supposed to be imputed using share data from most recent EIA861 but in most cases, the cells result in  `#REF!`. Reporting names for those to examine are:
    - City & Borough of Sitka
    - Barrow Utilities & Electric Cooperative Inc.
    - City of Petersburg
    - City of Wrangell
- `Table 2.5a` Missing data from these communities: Stevens Village, Tuluksak, King Cove, Koyukuk, Diomede
- `Table 2.5a` Stevens Village and King Cove each have duplicate entries. No data though.
- `Table 1.j / Table 2.5a` Starting this year, the number of 'Other' customer accounts jumps from approximately 5,000 the year before to over 11,000 this year. Needs an explanation
- Bradley Lake data from the EIA does not match utility purchase data as reported to the Regulatory Commission of Alaska (RCA). In particular, the following difference is found: `EIA 466,635 MWh -- Utility purchases 453,872 MWh`.

## 2015 Alaska Energy Statistics Workbook
> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2015_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2015_AK_Energy_Statistics.xlsx)

- Table 2.5a. Reporting name "Ekwok" is listed as being in the Southeast AEA energy region. It should be in Bristol Bay. Possible larger issue with intertie lookup tables? No lookup tables are included with this file.

## 2014 Alaska Energy Statistics Workbook
> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2014_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2014_AK_Energy_Statistics.xlsx)

- Table 2.5a. Reporting name "Ekwok" is listed as being in the Southeast AEA energy region. It should be in Bristol Bay. Possible larger issue with intertie lookup tables? No lookup tables are included with this file.

## 2011 Alaska Energy Statistics Workbook
> [https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2011_AK_Energy_Statistics.xlsx](https://github.com/acep-uaf/ak-energy-statistics-2011_2021/blob/main/workbooks/2011_AK_Energy_Statistics.xlsx)

- `Table 2.3b` The community of Unalaska has a missing name for their power plant. According to the data in the workbooks from 2012-2021, this should be "Unalaska Power Module". We recommend accounting for this if the plant names are used in your analysis.