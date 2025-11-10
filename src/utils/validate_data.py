import pandas as pd
from typing import Tuple, List


def validate_telco_data(df: pd.DataFrame) -> Tuple[bool, List[str]]:
    """
    Telco Customer Churn data validation using pandas-based checks.
    Provides GX-like validation interface without complex GX setup.
    """

    print("🔍 Starting data validation...")

    failed_expectations: List[str] = []
    total_checks = 0

    # === SCHEMA VALIDATION ===
    print("📋 Checking schema and required columns...")
    required_columns: List[str] = [
        "customerID", "gender", "Partner", "Dependents",
        "PhoneService", "InternetService", "Contract",
        "tenure", "MonthlyCharges", "TotalCharges"
    ]
    
    for col in required_columns:
        total_checks += 1
        if col not in df.columns:
            failed_expectations.append(f"expect_column_to_exist({col})")
            print(f"   ❌ Column '{col}' not found")
        else:
            print(f"   ✅ Column '{col}' exists")
    
    # Check customerID not null
    total_checks += 1
    if "customerID" in df.columns:
        null_count = df["customerID"].isnull().sum()
        if null_count > 0:
            failed_expectations.append(f"expect_column_values_to_not_be_null(customerID) - {null_count} nulls")
            print(f"   ❌ customerID has {null_count} null values")
        else:
            print(f"   ✅ customerID has no null values")

    # === BUSINESS LOGIC ===
    print("💼 Validating business rules...")
    
    binary_cols = ["Partner", "Dependents", "PhoneService"]
    for c in binary_cols:
        total_checks += 1
        if c in df.columns:
            valid_values = {"Yes", "No"}
            invalid_mask = ~df[c].isin(valid_values) & df[c].notna()
            invalid_count = invalid_mask.sum()
            if invalid_count > 0:
                invalid_vals = df.loc[invalid_mask, c].unique()[:5]
                failed_expectations.append(f"expect_column_values_to_be_in_set({c}) - found: {list(invalid_vals)}")
                print(f"   ❌ {c} has {invalid_count} invalid values: {list(invalid_vals)}")
            else:
                print(f"   ✅ {c} values are valid (Yes/No)")
    
    # Contract validation
    total_checks += 1
    if "Contract" in df.columns:
        valid_contracts = {"Month-to-month", "One year", "Two year"}
        invalid_mask = ~df["Contract"].isin(valid_contracts) & df["Contract"].notna()
        invalid_count = invalid_mask.sum()
        if invalid_count > 0:
            invalid_vals = df.loc[invalid_mask, "Contract"].unique()[:5]
            failed_expectations.append(f"expect_column_values_to_be_in_set(Contract) - found: {list(invalid_vals)}")
            print(f"   ❌ Contract has {invalid_count} invalid values: {list(invalid_vals)}")
        else:
            print(f"   ✅ Contract values are valid")
    
    # InternetService validation
    total_checks += 1
    if "InternetService" in df.columns:
        valid_services = {"DSL", "Fiber optic", "No"}
        invalid_mask = ~df["InternetService"].isin(valid_services) & df["InternetService"].notna()
        invalid_count = invalid_mask.sum()
        if invalid_count > 0:
            invalid_vals = df.loc[invalid_mask, "InternetService"].unique()[:5]
            failed_expectations.append(f"expect_column_values_to_be_in_set(InternetService) - found: {list(invalid_vals)}")
            print(f"   ❌ InternetService has {invalid_count} invalid values: {list(invalid_vals)}")
        else:
            print(f"   ✅ InternetService values are valid")

    # === NUMERIC RANGE ===
    print("📊 Validating numeric ranges...")
    
    # Tenure validation
    total_checks += 1
    if "tenure" in df.columns:
        # Convert to numeric if needed
        tenure_numeric = pd.to_numeric(df["tenure"], errors='coerce')
        out_of_range = ((tenure_numeric < 0) | (tenure_numeric > 120)) & tenure_numeric.notna()
        out_of_range_count = out_of_range.sum()
        if out_of_range_count > 0:
            failed_expectations.append(f"expect_column_values_to_be_between(tenure, 0, 120) - {out_of_range_count} out of range")
            print(f"   ❌ tenure has {out_of_range_count} values outside [0, 120]")
        else:
            print(f"   ✅ tenure values are within [0, 120]")
        
        # Check for nulls
        total_checks += 1
        null_count = tenure_numeric.isnull().sum()
        if null_count > 0:
            failed_expectations.append(f"expect_column_values_to_not_be_null(tenure) - {null_count} nulls")
            print(f"   ❌ tenure has {null_count} null values")
        else:
            print(f"   ✅ tenure has no null values")
    
    # MonthlyCharges validation
    total_checks += 1
    if "MonthlyCharges" in df.columns:
        monthly_numeric = pd.to_numeric(df["MonthlyCharges"], errors='coerce')
        out_of_range = ((monthly_numeric < 0) | (monthly_numeric > 200)) & monthly_numeric.notna()
        out_of_range_count = out_of_range.sum()
        if out_of_range_count > 0:
            failed_expectations.append(f"expect_column_values_to_be_between(MonthlyCharges, 0, 200) - {out_of_range_count} out of range")
            print(f"   ❌ MonthlyCharges has {out_of_range_count} values outside [0, 200]")
        else:
            print(f"   ✅ MonthlyCharges values are within [0, 200]")
        
        # Check for nulls
        total_checks += 1
        null_count = monthly_numeric.isnull().sum()
        if null_count > 0:
            failed_expectations.append(f"expect_column_values_to_not_be_null(MonthlyCharges) - {null_count} nulls")
            print(f"   ❌ MonthlyCharges has {null_count} null values")
        else:
            print(f"   ✅ MonthlyCharges has no null values")
    
    # TotalCharges validation
    total_checks += 1
    if "TotalCharges" in df.columns:
        total_numeric = pd.to_numeric(df["TotalCharges"], errors='coerce')
        out_of_range = (total_numeric < 0) & total_numeric.notna()
        out_of_range_count = out_of_range.sum()
        if out_of_range_count > 0:
            failed_expectations.append(f"expect_column_values_to_be_between(TotalCharges, 0, inf) - {out_of_range_count} negative values")
            print(f"   ❌ TotalCharges has {out_of_range_count} negative values")
        else:
            print(f"   ✅ TotalCharges values are >= 0")

    # === CONSISTENCY ===
    print("🔗 Checking consistency...")
    total_checks += 1
    if "TotalCharges" in df.columns and "MonthlyCharges" in df.columns:
        total_numeric = pd.to_numeric(df["TotalCharges"], errors='coerce')
        monthly_numeric = pd.to_numeric(df["MonthlyCharges"], errors='coerce')
        
        # Check if TotalCharges >= MonthlyCharges (with 95% threshold)
        invalid_mask = (total_numeric < monthly_numeric) & total_numeric.notna() & monthly_numeric.notna()
        invalid_count = invalid_mask.sum()
        total_valid = (total_numeric.notna() & monthly_numeric.notna()).sum()
        
        if total_valid > 0:
            invalid_pct = (invalid_count / total_valid) * 100
            if invalid_pct > 5:  # More than 5% invalid (allowing 95% to pass)
                failed_expectations.append(f"expect_column_pair_values_A_to_be_greater_than_B(TotalCharges, MonthlyCharges) - {invalid_pct:.1f}% invalid")
                print(f"   ❌ TotalCharges < MonthlyCharges in {invalid_count}/{total_valid} cases ({invalid_pct:.1f}%)")
            else:
                print(f"   ✅ TotalCharges >= MonthlyCharges in {100-invalid_pct:.1f}% of cases")
        else:
            print(f"   ⚠️  Cannot check consistency: missing valid values")

    # === SUMMARY ===
    passed = total_checks - len(failed_expectations)
    success = len(failed_expectations) == 0

    if success:
        print(f"\n✅ Data validation PASSED: {passed}/{total_checks} checks successful.")
    else:
        print(f"\n❌ Data validation FAILED: {len(failed_expectations)}/{total_checks} checks failed.")
        print(f"   Failed expectations: {failed_expectations[:10]}")  # Show first 10

    return success, failed_expectations
