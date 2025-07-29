# 🧼 Data Cleaning Report: Hotel Booking Demand Dataset

## Executive Summary
This report details the data cleaning process performed on the Hotel Booking Demand dataset from Kaggle. The goal was to prepare a clean, analysis-ready dataset for further exploration or modeling.

---

## 📊 Data Quality Assessment

**Original Dataset Stats:**
- Rows: 119,390
- Columns: 32

### Issues Identified:
- Missing values in `agent`, `company`, `children`, `country`
- 100+ duplicate rows
- Outliers in columns like `lead_time`, `adr`
- Inconsistent data (e.g., bookings with 0 guests)

---

## 🛠️ Cleaning Methodology

### 🔹 Missing Values:
- `children`: filled with 0
- `agent`, `company`: filled with 0
- `country`: filled with "Unknown"

### 🔹 Duplicates:
- All exact duplicates removed

### 🔹 Outliers:
- Treated using IQR method (columns like `adr`, `lead_time`, `babies`)

### 🔹 Inconsistencies:
- Removed rows where adults + children + babies = 0
- Converted date columns to datetime

---

## ✅ Results and Impact

- Final Rows: ~118,800
- All missing values handled
- Cleaned dataset saved as `hotel_bookings_cleaned.csv`

---

## 📌 Recommendations

- Improve data collection for agent and company fields
- Enforce validation on guest count (no bookings with 0 guests)

---

**Prepared by:** Jalani Sewmini
**Date:** 2025-07-29
**GitHub** https://github.com/jalanisew/ITBIN-2211-0287_datacleaning.git
