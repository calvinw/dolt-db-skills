-- SHW FY2024 (DB year 2024) — Operating Profit correction
-- Generated: 2026-06-11
-- Issue: DB had Operating Profit = 3,451,800K which is actually Pretax Income
--        (us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest)
-- Correct Operating Profit = Gross Profit - SGA - Other operating expense - Impairment
--   = 11,195,100 - 7,422,100 - 38,800 - 0 = 3,734,200K
-- Source: SEC 10-K CIK 89800, fiscal year ending 2024-12-31
-- All other fields unchanged.

UPDATE financials
SET `Operating Profit` = 3734200
WHERE company_name = 'Sherwin-Williams'
  AND year = 2024;
