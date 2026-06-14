-- Ace Hardware Corporation
-- Source: PDF annual reports (private company)
-- Units: thousands (converted from millions × 1,000)
-- Generated: 2026-06-14

REPLACE INTO company_info
  (company, display_name, segment, subsegment, currency, units)
VALUES
  ('Ace Hardware', 'Ace Hardware Corporation', 'Home Improvement', NULL, 'USD', 'thousands');

-- FY2021 (ended Jan 1, 2022)
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware', 2021, '2022-01-01', 8594200, 7299800, 1294400,
   955600, 338800, 330000, 1224300, 1917400, 3141400,
   1618200, 2333300, 808100, 3141400,
   '2023_Financials_2023-2021.pdf');

-- FY2022 (ended Dec 31, 2022) — verified against 2026 Financials2024-2022.pdf, all values match
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware', 2022, '2022-12-31', 9169800, 7808400, 1361400,
   1019500, 341900, 340600, 1303700, 2096000, 3491000,
   1730500, 2599200, 891800, 3491000,
   '2023_Financials_2023-2021.pdf, 2026 Financials2024-2022.pdf (verified)');

-- FY2023 (ended Dec 30, 2023) — verified against 2025financialreportfinal.pdf, all values match
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware', 2023, '2023-12-30', 9131100, 7653200, 1477900,
   1116800, 361100, 323400, 1235100, 2060700, 3957600,
   1702900, 3036200, 921400, 3957600,
   '2026 Financials2024-2022.pdf, 2025financialreportfinal.pdf (verified)');

-- FY2024 (ended Dec 28, 2024) — verified against 2025financialreportfinal.pdf, all values match
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware', 2024, '2024-12-28', 9491400, 7946300, 1545100,
   1227800, 317300, 314100, 1197900, 2092000, 4292800,
   1893400, 3370900, 921900, 4292800,
   '2026 Financials2024-2022.pdf, 2025financialreportfinal.pdf (verified)');

-- FY2025 (ended Jan 3, 2026)
REPLACE INTO financials
  (company_name, year, reportDate, `Net Revenue`, `Cost of Goods`, `Gross Margin`,
   SGA, `Operating Profit`, `Net Profit`, Inventory, `Current Assets`, `Total Assets`,
   `Current Liabilities`, Liabilities, `Total Shareholder Equity`,
   `Total Liabilities and Shareholder Equity`, source_pdf)
VALUES
  ('Ace Hardware', 2025, '2026-01-03', 10043600, 8370600, 1673000,
   1353200, 319800, 293400, 1200800, 2117900, 4445300,
   1898800, 3545200, 900100, 4445300,
   '2025financialreportfinal.pdf');
