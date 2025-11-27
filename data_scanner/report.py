from datetime import datetime
def generate_md_report(summary,numeric,categorical,insights):
    lines = []
    lines.append(f"# Data Profile \nGenerated on {datetime.now()}\n")
    lines.append("## Basic Summary")
    for k, v in summary.items():
        lines.append(f"- **{k}** : {v}")
    lines.append("\n## Numerical Columns Summary")
    for col,stats in numeric.items():
        lines.append(f"\n### {col}")
        for s,val in stats.items():
            lines.append(f"- {s} : {val}")
    lines.append("\n## Categorical Columns Summary")
    for col,details in categorical.items():
        lines.append(f"\n### {col}")
        for s,val in details.items():
            lines.append(f"- {s} : {val}")
    lines.append("\n## Automated Insights")
    for section,insight in insights.items():
        lines.append(f"\n### {section}")
        for k,v in insight.items():
            lines.append(f"- **{k}** : {v}")
    return "\n".join(lines)