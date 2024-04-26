# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Types of changes
- **Added** for new features.
- **Changed** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features.
- **Removed** for now removed features.
- **Fixed** for any bug fixes.
- **Security** in case of vulnerabilities.

## [2.0.0] - 2024-03-01

### Added
 
- errata.md  
- Annual_Summary_Tables.xlsx  
- Energy_Stats_Financial_Tables.xlsx  
- Energy_Stats_Generation_Tables.xlsx  
- Energy_Stats_Infrastructure_2021.xlsx  
- Table_1_PCE_worksheets.xlsx

### Updated workbooks by Neil McMahon

- Update Lookup for Sales Reporting, Plants, and Operator to make Operator names consistent
- Updated Intertie current IDs for several interties
- Updated underlying data for SW Bailey Plant
- Changed Noorvik from WT to PV
- Updated titles in Generation (2.2a, 2.3a, 2.3b, 2.3c, 2.4a) w/ Utility/operator
- Added definitions to Tables 1.e, 1.f, 1.g
  - Added Other to 1.e and 1.f. 
- Removed OBL from Oil in 1.e and 1.f
- Add definition to Table 2.3b
- Fixed queries for Coal in column Q of Table 2.3b
- Fixed queries for Oil in column O of Table 2.3b
- Fixed cell references in Table 2.3c
- Removed extra Stony River row from 2.3b and 2.4a
- Added Cordova Eyak BESS to 2.3c and 2.4a [check on infrastructure tabs]
- Added UAF JF/ST to 2.3c and 2.4a
- Changed conversion of MWH to MMBtu from 3.4203 to 3.412
- Add Kotz solar to 2.3c, 2.4a [check infrastructure]
- Added Deering solar to 2.3c and 2.4a [check on infrastructure tabs]
- Added Kake Hydro to 2.3c and 2.4a [check on infrastructure tabs]
- Fixed monthly data for Bethel—some months had incorrect utility name
- Fixed calculation error for Annual Operations Consolidated dataset
  - Moved PCE station service to “Consumed by Facility”
  - Changed Total Losses to “Unaccountable/Energy Losses”. Created equation such that Unaccountable/Energy Losses balanced the consumption and generation for PCE communities
- Update 2.2a template. Included “Consumed by Facility” and Consumed by Respondent w/o Charge” under Used by Facility.
- Updated 2.2a Generation column title
- Changed Table 1.f title. Removed “Net”
- Table 2.3b Changed queries for Hydro, wind, solar, storage, and Other to capture cases where some data came from PCE and some data from EIA923
- Fixed issues with Sand Point. Replaced Sand Point Generating, LLC info for TDX Power info in multiple LOOKUP tables.
- Removed entries with no data
- Updated charts for each workbook


## [1.0.0] - 2023-12-11

### Added
- The 2011-2021 excel workbooks from Neil via Steve.
- Initial structure for the website to present the data and context of the data.
- Add CC-BY-SA 4.0 License

