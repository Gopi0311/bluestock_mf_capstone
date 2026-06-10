"""
generate_report.py - Day 7: Auto-generate Final Report PDF
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import inch
from pathlib import Path

OUTPUT = Path(__file__).parent / "Final_Report.pdf"

def build_report():
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4,
                           rightMargin=50, leftMargin=50,
                           topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    BLUE = HexColor('#1B4F9B')
    
    title_style = ParagraphStyle('Title',
        fontSize=24, textColor=BLUE,
        spaceAfter=20, alignment=1, fontName='Helvetica-Bold')
    
    h1_style = ParagraphStyle('H1',
        fontSize=16, textColor=BLUE,
        spaceAfter=10, fontName='Helvetica-Bold')
    
    h2_style = ParagraphStyle('H2',
        fontSize=13, textColor=BLUE,
        spaceAfter=8, fontName='Helvetica-Bold')
    
    body_style = ParagraphStyle('Body',
        fontSize=10, spaceAfter=8,
        fontName='Helvetica', leading=16)
    
    story = []
    
    # PAGE 1 - Title
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("BLUESTOCK FINTECH", title_style))
    story.append(Paragraph("Mutual Fund Analytics Platform", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Capstone Project — Final Report", 
                           ParagraphStyle('sub', fontSize=14, 
                           alignment=1, textColor=HexColor('#666666'))))
    story.append(Spacer(1, 0.3*inch))
    
    info_data = [
        ['Intern Name', 'Upputholla Gopi'],
        ['Institution', 'VVIT, Guntur'],
        ['Domain', 'Mutual Fund / Fintech'],
        ['Duration', '7 Working Days | June 2026'],
        ['Technologies', 'Python, SQL, Power BI'],
    ]
    info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), BLUE),
        ('TEXTCOLOR', (0,0), (0,-1), white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#CCCCCC')),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(info_table)
    story.append(PageBreak())
    
    # PAGE 2 - Executive Summary
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph("""
    This capstone project presents a full-stack Mutual Fund Analytics Platform 
    developed for Bluestock Fintech. The platform ingests publicly available 
    data from AMFI India and mfapi.in, processes it through a robust ETL 
    pipeline, stores it in a normalized SQLite database, and delivers insights 
    through an interactive Power BI dashboard.
    """, body_style))
    
    story.append(Paragraph("Key Achievements:", h2_style))
    achievements = [
        "Built automated ETL pipeline processing 87,000+ rows of financial data",
        "Designed 5-table star schema SQLite database with 8 fact/dimension tables",
        "Created 10+ EDA charts revealing key market trends and investor behaviour",
        "Computed Sharpe, Sortino, Alpha, Beta, VaR metrics for 40 fund schemes",
        "Built 4-page interactive Power BI dashboard with Bluestock branding",
        "Developed fund recommendation system based on risk appetite",
    ]
    for a in achievements:
        story.append(Paragraph(f"• {a}", body_style))
    story.append(PageBreak())
    
    # PAGE 3 - Data Sources
    story.append(Paragraph("2. Data Sources & Datasets", h1_style))
    story.append(Paragraph("""
    All data is sourced from publicly available APIs and reports published 
    by AMFI India, NSE, and BSE. No proprietary data was used.
    """, body_style))
    
    data_table = [
        ['Dataset', 'Rows', 'Description'],
        ['01_fund_master.csv', '40', 'Master list of 40 fund schemes'],
        ['02_nav_history.csv', '46,000+', 'Daily NAV 2022-2026'],
        ['03_aum_by_fund_house.csv', '90', 'Quarterly AUM by AMC'],
        ['04_monthly_sip_inflows.csv', '48', 'Monthly SIP inflow data'],
        ['05_category_inflows.csv', '144', 'Net inflows by category'],
        ['06_industry_folio_count.csv', '21', 'Total MF folios growth'],
        ['07_scheme_performance.csv', '40', 'Risk-return metrics'],
        ['08_investor_transactions.csv', '32,000+', 'SIP/Lumpsum transactions'],
        ['09_portfolio_holdings.csv', '322', 'Equity fund holdings'],
        ['10_benchmark_indices.csv', '8,050', 'Nifty/BSE index data'],
    ]
    dt = Table(data_table, colWidths=[2.5*inch, 1*inch, 3*inch])
    dt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#CCCCCC')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), 
         [HexColor('#F5F5F5'), white]),
    ]))
    story.append(dt)
    story.append(PageBreak())
    
    # PAGE 4 - EDA Findings
    story.append(Paragraph("3. EDA Key Findings", h1_style))
    findings = [
        ("NAV Trend", "All 40 funds showed consistent growth 2022-2026 with strong 2023 bull run."),
        ("SBI Dominance", "SBI Mutual Fund leads AUM at Rs.12.5 Lakh Crore — nearly 2x ICICI Pru."),
        ("SIP All-time High", "Monthly SIP inflows hit Rs.31,002 Crore in Dec 2025."),
        ("Age Demographics", "26-35 age group forms the largest investor segment."),
        ("Geographic", "Maharashtra and Karnataka lead in total investment amounts."),
        ("T30 vs B30", "T30 cities contribute ~70% of total investments."),
        ("Folio Growth", "Total folios doubled from 13.26 Cr to 26.12 Cr — 97% growth."),
        ("Correlation", "Large cap funds show 0.85+ correlation with each other."),
        ("Sector", "Consumer Goods and IT together account for ~25% of portfolios."),
        ("Gender Gap", "Male investors outnumber female 65:35."),
    ]
    for title, desc in findings:
        story.append(Paragraph(
            f"<b>{title}:</b> {desc}", body_style))
    story.append(PageBreak())
    
    # PAGE 5 - Performance Metrics
    story.append(Paragraph("4. Performance Analytics", h1_style))
    story.append(Paragraph("""
    Key risk-return metrics were computed for all 40 fund schemes using 
    daily NAV history from January 2022 to May 2026.
    """, body_style))
    
    metrics_data = [
        ['Metric', 'Formula', 'Purpose'],
        ['CAGR', '(NAV_end/NAV_start)^(1/n) - 1', 'Annualised return'],
        ['Sharpe Ratio', '(Rp - Rf) / Std(Rp) x √252', 'Risk-adjusted return'],
        ['Sortino Ratio', '(Rp - Rf) / Downside_Std', 'Downside risk measure'],
        ['Alpha', 'OLS intercept x 252', 'Return above benchmark'],
        ['Beta', 'OLS slope', 'Market sensitivity'],
        ['Max Drawdown', 'min(NAV/max_NAV - 1)', 'Worst peak-to-trough'],
        ['VaR (95%)', '5th percentile of returns', 'Daily loss threshold'],
        ['CVaR', 'Mean of returns < VaR', 'Expected tail loss'],
    ]
    mt = Table(metrics_data, colWidths=[1.5*inch, 2.5*inch, 2.5*inch])
    mt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#CCCCCC')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1),
         [HexColor('#F5F5F5'), white]),
    ]))
    story.append(mt)
    story.append(PageBreak())
    
    # PAGE 6 - Recommendations
    story.append(Paragraph("5. Recommendations", h1_style))
    recs = [
        "Investors with Low risk appetite should consider Liquid and Short-term Debt funds with Sharpe > 1.",
        "Moderate risk investors can explore Large Cap funds with consistent 3yr CAGR > 12%.",
        "High risk investors may consider Mid/Small Cap funds but should monitor Max Drawdown.",
        "AMCs should target B30 cities for SIP campaigns as growth potential is higher.",
        "Funds with high HHI concentration should diversify sector exposure.",
        "At-risk SIP investors (gap > 35 days) need re-engagement through notifications.",
    ]
    for r in recs:
        story.append(Paragraph(f"• {r}", body_style))
    
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("6. Limitations", h1_style))
    limits = [
        "Investor transaction data is synthetically generated for educational purposes.",
        "NAV data anchored to real values but simulated forward with realistic parameters.",
        "Analysis limited to 40 schemes out of 1,908 total industry schemes.",
        "Dashboard requires Power BI Desktop to view interactively.",
    ]
    for l in limits:
        story.append(Paragraph(f"• {l}", body_style))
    
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Prepared by: Upputholla Gopi | Bluestock Fintech Internship | June 2026",
                           ParagraphStyle('footer', fontSize=9,
                           textColor=HexColor('#666666'), alignment=1)))
    
    doc.build(story)
    print(f"✅ Final Report saved: {OUTPUT}")

if __name__ == "__main__":
    build_report()