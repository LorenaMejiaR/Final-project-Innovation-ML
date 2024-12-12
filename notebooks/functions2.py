import pandas as pd

def drop_columns(df):
    columns_to_drop = {
        'name_quality_certification', 'fiscal_year','fiscal_month', 'fiscal_day', 'last_fiscal_year',
        'other_status', 'electricity_obstacle', 'main_activity', 'main_product', 'sales_description',
        'sales_2years_ago', 'technology_supply_chain', 'transport_obstacle_ops', 'customs_obstacle_ops', 
        'main_solutions', 'promotions', 'time_dismissed', 'obstacle_informal_competitors', 'product_inn_description',
        'prod_inn_description2', 'process_inn_description', 'process_inn_description2', 'access_land_obstacle', 
        'obstacle_crime', 'obstacle_access_finance', 'opinion_court_system', 'tax_officials_impartial', 
        'tax_officials_transparent', 'raised_complaints', 'payments_votes', 'payments_content_decrees', 
        'payments_votes_localdecrees', 'other_public_support_descrip', 'obtacle_tax_rates', 'obtacle_tax_adm', 
        'obtacle_permits','obstacle_political_inestability', 'obstacle_corruption','obstacle_occup_safety', 
        'obstacle_healthy_reg','obstacle_environment_reg', 'obstacle_courts', 'foreing_languages', 'interpersonal_skills', 
        'managerial_skilss', 'it_skilss','engineering_skilss', 'technical_skilss', 'obstacle_labor_reg', 
        'biggest_obstacle','obstacle_educated_workers', 'year_established', 'formal_year'}
    df = df.drop(columns=columns_to_drop, errors='ignore')
    return df