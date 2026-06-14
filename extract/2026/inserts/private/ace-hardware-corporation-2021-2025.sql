-- Ace Hardware Corporation
-- Source: PDF annual reports (private company)
-- Generated: 2026-06-14
-- All values in thousands USD

REPLACE INTO private_company_info
  (company, display_name, segment, subsegment, currency, units, source_pdf)
VALUES
  ('Ace Hardware Corporation', 'Ace Hardware Corporation', 'Retail', 'Home Improvement', 'USD', 'thousands',
   '2023_Financials_2023-2021.pdf, 2026 Financials2024-2022.pdf, 2025financialreportfinal.pdf');

-- FY2021 (year ended January 1, 2022)
REPLACE INTO private_financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware Corporation', 2021, '2022-01-01', 8594200, 7299800, 1294400,
   222500, 338800, 330000, 1224300, 1917400, 3141400,
   1618200, 2333300, 808100, 3141400,
   '2023_Financials_2023-2021.pdf');

-- FY2022 (year ended December 31, 2022) — verified against 2026 Financials2024-2022.pdf
REPLACE INTO private_financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware Corporation', 2022, '2022-12-31', 9169800, 7808400, 1361400,
   244600, 341900, 340600, 1303700, 2096000, 3491000,
   1730500, 2599200, 891800, 3491000,
   '2023_Financials_2023-2021.pdf, 2026 Financials2024-2022.pdf (verified)');

-- FY2023 (year ended December 30, 2023) — verified against 2025financialreportfinal.pdf
REPLACE INTO private_financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware Corporation', 2023, '2023-12-30', 9131100, 7653200, 1477900,
   314700, 361100, 323400, 1235100, 2060700, 3957600,
   1702900, 3036200, 921400, 3957600,
   '2026 Financials2024-2022.pdf, 2025financialreportfinal.pdf (verified)');

-- FY2024 (year ended December 28, 2024) — verified against 2025financialreportfinal.pdf
REPLACE INTO private_financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware Corporation', 2024, '2024-12-28', 9491400, 7946300, 1545100,
   342400, 317300, 314100, 1197900, 2092000, 4292800,
   1893400, 3370900, 921900, 4292800,
   '2026 Financials2024-2022.pdf, 2025financialreportfinal.pdf (verified)');

-- FY2025 (year ended January 3, 2026)
REPLACE INTO private_financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware Corporation', 2025, '2026-01-03', 10043600, 8370600, 1673000,
   384900, 319800, 293400, 1200800, 2117900, 4445300,
   1898800, 3545200, 900100, 4445300,
   '2025financialreportfinal.pdf');
