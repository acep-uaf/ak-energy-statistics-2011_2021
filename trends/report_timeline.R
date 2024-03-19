
library(timevis)
library(tibble)


##################
# Example format #
##################

# data <- data.frame(
#   id      = 1:4,
#   content = c("Item one"  , "Item two"  ,"Ranged item", "Item four"),
#   start   = c("2016-01-10", "2016-01-11", "2016-01-20", "2016-02-14 15:00:00"),
#   end     = c(NA          ,           NA, "2016-02-04", NA)
# )
# 
# timevis(data)


data <- data.frame(
  content = character(),
  start = character(),
  end = character()
)



test <- data %>%
  add_row(content = "Federal Alaska Power Administration published Alaska Electric Power Statistics report (AEPS)",
          start = "1973-01-01",
          end = "1984-01-01") %>%
  add_row(content = "Alaska Energy Authority (AEA, formerly Alaska Power Authority) begins gathering statistical data and publishing annual report",
          start = "1985-01-01",
          end = NA) %>%
  add_row(content = "AEPS report becomes combined effort of the Alaska Systems Coordinating Council (ASCC) and AEA",
          start = "1988-01-01",
          end = NA) %>%
  add_row(content = "AEPS becomes joint effort of the ASCC and the Alaska Department of Community and Regional Affairs, Division of Energy",
          start = "1993-01-01",
          end = NA) %>%
  add_row(content = "No reports published",
          start = "1995-01-01",
          end = "2003-01-01") %>%
  add_row(content = "The Institute of Social and Economic Research (ISER) at the University of Alaska Anchorage (UAA) prepare a report with funding from AEA, the Regulatory Commission of Alaska (RCA), and the Denali Commission",
          start = "2003-01-01",
          end = NA) %>%
  add_row(content = "ISER prepares Alaska Energy Statistics updates with funding from AEA",
          start = "2008-01-01",
          end = "2012-01-01") %>%
  add_row(content = "AEA prepares Excel workbook with updated data, but no report",
          start = "2013-01-01",
          end = NA)
  
  
  timevis(test)











