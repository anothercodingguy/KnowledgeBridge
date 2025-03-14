from datetime import datetime

def save_expert_insight(problem: str, solution: str):
    # Save to a TXT file in 'data' folder
    with open("data/expert_insights.txt", "a") as f:
        f.write(
            f"Problem: {problem}\n"
            f"Solution: {solution}\n"
            f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
        )
    print("Insight saved!")