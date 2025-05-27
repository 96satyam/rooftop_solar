def solar_estimation(area_m2, irradiance=5.5, panel_eff=0.18, tariff=7.0):
    """
    Estimate solar energy output, system cost, and ROI for a given rooftop area.

    Parameters:
        area_m2 (float): Usable rooftop area in square meters.
        irradiance (float): Average daily solar irradiance (kWh/m²/day).
        panel_eff (float): Efficiency of the solar panels (as a decimal).
        tariff (float): Electricity tariff (₹ per kWh).

    Returns:
        dict: Contains estimated system size, annual energy output, cost, savings, and payback period.
    """

    # Estimate annual energy output (kWh/year)
    kwh_per_year = area_m2 * irradiance * 365 * panel_eff

    # Calculate system size in kW (Assuming ~6.5 m² per kW)
    system_size_kw = area_m2 / 6.5

    # Estimate system cost (₹40,000 per kW is a common average)
    system_cost = system_size_kw * 40000

    # Estimate yearly savings
    annual_savings = kwh_per_year * tariff

    # Calculate payback period (years), avoiding division by zero
    roi_years = system_cost / annual_savings if annual_savings > 0 else float('inf')

    return {
        "Rooftop Area (m²)": round(area_m2, 2),
        "System Size (kW)": round(system_size_kw, 2),
        "Energy Output (kWh/year)": round(kwh_per_year),
        "System Cost (₹)": round(system_cost),
        "Annual Savings (₹)": round(annual_savings),
        "Payback Period (yrs)": round(roi_years, 1)
    }