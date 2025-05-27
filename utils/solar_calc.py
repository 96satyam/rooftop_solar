def solar_estimation(area_m2, irradiance=5.5, panel_eff=0.18, tariff=7.0):
    """
    Calculate solar output and ROI from rooftop area.

    Args:
        area_m2 (float): Usable rooftop area in square meters.
        irradiance (float): kWh/m²/day (default = 5.5 for India)
        panel_eff (float): Efficiency of solar panels (18% = 0.18)
        tariff (float): ₹/kWh for local electricity cost

    Returns:
        dict with kWh/year, cost, savings/year, ROI
    """
    # Energy output
    kwh_per_year = area_m2 * irradiance * 365 * panel_eff

    # System size in kW (1kW ≈ 6.5 m² of panels)
    system_size_kw = area_m2 / 6.5

    # Approx cost (₹40,000 per kW)
    system_cost = system_size_kw * 40000

    # Yearly savings
    annual_savings = kwh_per_year * tariff

    # Payback period
    roi_years = system_cost / annual_savings if annual_savings > 0 else float('inf')

    return {
        "Rooftop Area (m²)": round(area_m2, 2),
        "System Size (kW)": round(system_size_kw, 2),
        "Energy Output (kWh/year)": round(kwh_per_year),
        "System Cost (₹)": round(system_cost),
        "Annual Savings (₹)": round(annual_savings),
        "Payback Period (yrs)": round(roi_years, 1)
    }
