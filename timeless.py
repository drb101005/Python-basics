def calculate_gross_salary():
    basic_salary = float(input("Enter the basic salary: "))
    
    da = 0.7 * basic_salary  # Dearness Allowance
    ta = 0.3 * basic_salary  # Travel Allowance
    hra = 0.1 * basic_salary  # House Rent Allowance
    
    gross_salary = basic_salary + da + ta + hra
    
    print("\nSalary Breakdown:")
    print(f"Basic Salary: {basic_salary:.2f}")
    print(f"Dearness Allowance (70%): {da:.2f}")
    print(f"Travel Allowance (30%): {ta:.2f}")
    print(f"House Rent Allowance (10%): {hra:.2f}")
    print(f"\nGross Salary: {gross_salary:.2f}")

calculate_gross_salary()