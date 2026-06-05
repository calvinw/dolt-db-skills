-- Fix ADS.DE FY2018 and FY2019 SGA — previously G&A-only, now full SGA
-- Source: Adidas Annual Report 2019 (income statement, 2018 comparison column)
--   FY2018: Marketing & Point-of-Sale 3,001M + Distribution & Selling 4,450M + G&A 1,576M = 9,027M
--   FY2019: Marketing & Point-of-Sale 3,042M + Distribution & Selling 4,997M + G&A 1,652M = 9,691M
-- Methodology consistent with FY2020+ (sum of 3 functional categories, excluding D&A)
-- All values in thousands of euros (EUR)

UPDATE financials
SET `SGA` = 9027000
WHERE company_name = 'Adidas' AND year = 2018;

UPDATE financials
SET `SGA` = 9691000
WHERE company_name = 'Adidas' AND year = 2019;
