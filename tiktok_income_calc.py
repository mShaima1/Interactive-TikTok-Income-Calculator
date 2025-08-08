# TikTok Income Calculator (Interactive)

def tiktok_income_calculator(avg_viewers, hours_per_day, gift_revenue_per_viewer_per_hour):
    """
    Calculate daily and monthly income from TikTok live streams.
    
    Parameters:
    avg_viewers (int): Average viewers per stream
    hours_per_day (float): Hours live per day
    gift_revenue_per_viewer_per_hour (float): Estimated USD gift per viewer per hour (before cuts)
    
    Returns:
    dict: Contains raw daily income, final daily income after cuts, and monthly income
    """
    # Raw gift income
    daily_income = avg_viewers * hours_per_day * gift_revenue_per_viewer_per_hour
    
    # After TikTok cut (50%)
    daily_after_tiktok = daily_income * 0.5
    
    # After Payoneer/bank fees (~3%)
    final_daily = daily_after_tiktok * 0.97
    
    # Monthly (30 days)
    final_monthly = final_daily * 30
    
    return {
        "daily_before_cut": round(daily_income, 2),
        "daily_after_cut": round(final_daily, 2),
        "monthly_after_cut": round(final_monthly, 2)
    }

# Example interactive usage
if __name__ == "__main__":
    print("=== TikTok Live Income Calculator ===")
    viewers = int(input("Average viewers: "))
    hours = float(input("Hours live per day: "))
    rate = float(input("Gift revenue per viewer per hour (USD): "))
    
    result = tiktok_income_calculator(viewers, hours, rate)
    print("\n--- Estimated Income ---")
    print(f"Daily (before cut): ${result['daily_before_cut']}")
    print(f"Daily (after cut): ${result['daily_after_cut']}")
    print(f"Monthly (after cut): ${result['monthly_after_cut']}")
