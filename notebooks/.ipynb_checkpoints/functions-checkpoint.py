import pandas as pd
# Function to rename the columns
def rename_columns(df):
    column_mapping = {
        'a4a': 'sampling_sector', 'a6a': 'sampling_size', 'a2': 'sampling_location',
        'a4b': 'sector', 'a0': 'module', 'a3a': 'region', 'a6b': 'size',
        'a14d': 'day', 'a14m': 'month', 'a14y': 'year', 'a14h': 'hour', 'a14min': 'minutes', 'a12': 'interviewer', 
        'a1a': 'language', 'a7': 'multiestablishment_firm', 'a20y': 'fiscal_year', 'a20m': 'fiscal_month',
        'a20d': 'fiscal_day', 'COVa20m_1': 'last_fiscal_year', 'b1': 'legal_status', 'b1x': 'other_status', 
        'b3': 'percentage_ownership', 'b3a': 'owner_manager', 'EUb1': 'number_companies_owned', 
        'b29': 'private_domestic_companies', 'b2b': 'private_foreing_companies', 'b2c': 'government_company',
        'b2d': 'other_company', 'b4': 'female_owner', 'b4a': 'percentage_female_ownership', 
        'EUb2':'family_ownership',
        'EUb3': 'family_members_management', 'EUb4': 'ceo_politician', 'EUb5': 'support_group',
        'EUb6a':'international_markets','EUb6b': 'standard_quality', 'EUb6c': 'government_regulations',
        'EUb6d':'lobbying', 'b5': 'year_established', 'b6': 'fte_started', 'b6b': 'formal_year', 'b7': 
        'manager_experience', 'b7a': 'top_manager_female', 
        'Eub7': 'age_top_manager', 'Eub8': 'education_manager', 'Eub9': 'top_manager_dutch', 
        'Eub10': 'manager_experience_multinational', 'b8': 'quality_certification',
        'b8x':'name_quality_certification', 
        'c3': 'electrical_connection', 'c4': 'wait_for_elect_connec', 'c5': 'informal_payment_elect_connec', 
        'c6': 'power_outages', 'c7': 'number_power_outages', 'c8a': 'duration_power_outages', 
        'c8b': 'minutes_power_outages','c9a': 'percentage_losses_outages', 'c9b': 'amount_losses_outages', 'c10': 
        'own_generator', 'c11': 'electricity_generator','c12': 'application_water_connection', 
        'c13':'days_water_connection', 'c14':'informal_payment_water_connect', 
        'c15': 'insufficient_water_supply',  'c16': 'incidents_insufficient_water', 'c17': 
        'duration_incidents_water',
        'c22b': 'website', 'COVc4a': 'online_activity_covid', 'c30a': 'electricity_obstacle', 'd1a1a': 
        'main_activity', 'd1a1x': 'main_product', 'd1a3': 'percentage_sales_main_product', 'd2': 'sales', 'd2x': 
        'sales_description', 'COVb2a': 'sales_difference_covid', 'COVb2b': 'sales_increase_covid', 'COVb2c': 
        'sales_decrease_covid','n3': 'sales_2years_ago', 'EUd1a': 'direct_sales', 'EUd1b': 'direct_sales_phone', 
        'EUd1c': 'direct_sales_online','EUd1d': 'direct_sales_other', 'd3a': 'national_sales', 'd3b': 
        'indirect_exports', 'd3c': 'direct_exports', 'd4': 'avg_days_exp', 'd5a': 'informal_payment_exp', 'd8': 
        'first_year_exp', 'd10': 'losses_theft_products','d11': 'losses_spoilage_products', 'd12a': 
        'domestic_supplies', 'd12b': 'foreign_supplies', 'd13': 'imported_supplies', 'd14': 'avg_days_imp', 'd15a': 
        'informal_payment_imp', 'EUd2': 'technology_supply_chain', 'EUd3': 'formal_planning',
        'EUd4': 'method_planning', 'EUd5': 'main_technology', 'EUd6a': 'taxes_prevent_growth', 'EUd6b': 
        'labor_reg_prevent_growth','EUd6c': 'market_demand_prevent_growth', 'COVc2b':'more_demand_covid', 
        'COVc2c':'more_inputs_covid', 'd30a':'transport_obstacle_ops', 'd30b':'customs_obstacle_ops', 
        'r1':'main_solutions', 'r2':'kpis', 'r3':'number_kpis', 'r4':'production_targets',
        'r5':'time_frame_targets', 'r6':'difficulty_achieve_targets', 'r7':'people_aware_targets', 
        'r8':'performance_bonus', 'r9':'bonus_based_on', 'r10':'promotions', 'r11':'time_dismissed', 
        'e1':'main_market', 'e2b':'competitors', 'e6':'foreign_technology','e11':'informal_competitors', 
        'e30':'obstacle_informal_competitors', 'h1':'product_innovation', 'h2':'product_inn_market',
        'h3x':'product_inn_description', 'h4x':'prod_inn_description2', 'h5':'process_innovation', 
        'h6x':'process_inn_description','h7x':'process_inn_description2', 'h8':'r&d', 'h9':'r&d_intensity', 
        'f1':'capacity_utilization', 'f2':'operation_hours', 'COVb1a':'closing_covid', 
        'COVb1b':'closing_period_covid', 'g6a':'own_building', 'g1a':'own_land', 'g2':'construction_permit',
        'g3':'construction_permit_time', 'g4':'informal_payment_construction', 'g30a':'access_land_obstacle', 
        'i1':'security', 'i2a':'cost_security','i2b':'cost_security_amount', 'i3':'losses_fraudulent_transactions', 
        'i4a':'anual_losses_frauds', 'i4b':'amount_losses_frauds','i30':'obstacle_crime', 
        'k3a':'internal_funds_workingcapital', 'k3bc':'bank_loans_workingcapital', 
        'k3e':'other_loans_workingcapital',
        'k3f':'suppliers_customers_workingcapital', 'k3f':'suppliers_customers_workingcapital', 
        'k3hd':'other_source_workingcapital','k4':'fixed_assets', 'n5a':'machinery_equipment', 'n5b':'land_buildings', 
        'k5a':'internal_funds_fassets', 'k5a1':'amount_int_funds_fassets','k5i':'owner_contribution_fassets', 
        'k5i1':'amount_owner_contrib_fassets', 'k5bc':'bank_loan_fassets', 'k5bc1':'amount_bank_loan_fassets',
        'k5e':'other_loan_fassets', 'k5e1':'amount_other_loan_fassets', 'k5f':'suppliers_customers_fassets', 
        'k5f1':'amount_supp_cust_fassets','k5hdj':'other_source_fassets', 
        'k5hdj1':'amount_other_source_fassets','k4b':'fassets_last_year', 'n5c':'mach_equip_last_year',
        'n5d':'land_building_last_year', 'COVe1a':'liquidity_change_covid', 'COVe2':'source_cashflow_covid', 
        'k6':'savings_account','k7':'overdraft_facility', 'k8':'credit_line', 'k9':'insitution_credit_line', 
        'k10':'year_approval_credit_line', 'k11':'value_credit_line','k13':'collateral_credit_line', 
        'k14a':'collateral_land','k14b':'collateral_machinery','k14c':'collateral_acc_receivable','k14d':'collateral_owner_assets',
        'k14e':'collateral_other', 'k15a':'collateral_value', 'k15b':'outstanding_loans', 
        'k15c':'total_outstanding_balance', 'k15d':'outstanding_personal_loans', 
        'k16':'application_loans', 'k17':'reason_nottoappy_loans', 'k17':'reason_nottoappy_loans', 
        'k20a1':'outcome_application', 'k21':'certified_fin_statements',
        'k30':'obstacle_access_finance', 'h7a':'opinion_court_system', 'j2':'manager_timespent_regulations', 
        'j3':'tax_inspection', 'j4':'times_tax_inspection', 
        'j5':'informal_payment_taxinspection', 'EUj1':'online_tax_payment', 'EUj2a':'tax_officials_impartial', 
        'EUj2b':'tax_officials_transparent',
        'EUj2c':'raised_complaints', 'j6a':'government_contract', 'j6':'informal_payment_govcontract', 
        'j7a':'percentage_informal_payments',
        'j7b':'amount_informal_payments', 'j10':'import_lic', 'j11':'time_get_import_lic', 
        'j12':'informal_payment_import_lic', 'j13':'operating_licence', 
        'j14':'time_operating_license', 'EUj3':'operating_lic_online', 'j15':'informal_payment_operating_lic', 
        'EUj4a':'professional_officials_operating_lic',
        'EUj4b':'transparent_officials_operating_lic', 'EUj4c':'raised_complaints_operating_lic', 
        'EUj5a':'payments_votes', 'EUj5b':'payments_content_decrees',
        'EUj5c':'payments_votes_localdecrees', 'COVf1':'public_support', 'COVf2a':'cash_public_support', 
        'COVf2b':'deferralpaym_public_support',
        'COVf2c':'newcredit_public_support', 'COVf2d':'fiscalexemp_public_support', 
        'COVf2e':'wagesubsidies_public_support', 'COVf2f':'other_public_support',
        'COVf2fx':'other_public_support_descrip', 'j30a':'obtacle_tax_rates', 'j30b':'obtacle_tax_adm', 
        'j30c':'obtacle_permits', 'j30e':'obstacle_political_inestability',
        'j30f':'obstacle_corruption', 'EUj6a':'obstacle_occup_safety', 'EUj6b':'obstacle_healthy_reg', 
        'EUj6c':'obstacle_environment_reg', 'h30':'obstacle_courts',
        'l1':'permanent_fte', 'l2':'permanent_fte_lastyear', 
        'l3a':'production_workers','l3b':'administrative_workers','l4a1':'skilled_prod_workers', 
        'l4a2':'semi_skilled_prod_workers',
        'l4b':'low_skilled_prod_workers', 'l5a':'female_prod_workers', 'l5b':'female_adm_workers', 
        'EUl1a':'foreing_workers', 'EUl1b':'number_foreing_workers', 'EUl2a':'foreing_languages',
        'EUl2b':'interpersonal_skills', 'EUl2c':'problem_solving_skills', 'EUl2d':'managerial_skilss', 
        'EUl2e':'it_skilss',  'EUl2f':'engineering_skilss', 'EUl2g':'technical_skilss',
        'l6':'temporal_workers', 'l6a':'female_temporal_workers', 'l8':'avg_lenght_temporal_workers', 
        'COVd3a':'perm_workers_growth_covid', 'COVd3b':'temp_workers_growth_covid',
        'COVd6':'laidoff_workers_covid', 'COVd8':'furloughed_workers_covid', 'l9b':'workers_secondary_scchool', 
        'l9b1':'number_workers_secondary_scchool',
        'EUl3a':'workers_university_degree', 'EUl3b':'number_workers_university_degree', 'l10':'training', 
        'EUl4':'reasons_no_training', 'l11a':'prod_workers_training', 
        'l11a1':'number_prod_workers_training', 'l11b':'adm_workers_training', 'l11b1':'numberadm_workers_training', 
        'EUl5':'focus_training',  'EUl6':'vacancies',
        'EUl7a':'few_applicants_vac', 'EUl7b':'lacked_skills_vac', 'EUl7c':'applicants_rejected_vac', 
        'EUl8a':'difficulty_foreing_languages', 'EUl8b':'difficulty_communic_skills',
        'EUl8c':'problem_solving_skills', 'EUl8d':'management_skills', 'EUl8e':'it_skills',  
        'EUl8f':'engineering_skills',  'EUl8g':'technical_skills', 'l30a':'obstacle_labor_reg',
        'l30b':'obstacle_educated_workers', 'm1a':'biggest_obstacle', 'n2a':'labor', 'n2e':'raw_material', 
        'n2b':'cost_elctricity','n2p':'cost_goods_sold', 'n2e1':'cost_raw_material',
        'COVg2':'weeks_remain_open', 'n7a':'machinery_value', 'n7a':'machinery_value', 'EUb7':'age_top_manager', 
        'EUb8':'education_top_manager', 'EUb9':'citizenship_top_manager', 'EUb10':'multinational_exp_top_manager'
    }
    
    df = df.rename(columns=column_mapping)
    return df





