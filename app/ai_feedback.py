def generate_feedback(scores, complexity, code):
    return f"""
Overall Score: {scores['total']}/100

Correctness: {scores['correctness']}
Efficiency: {scores['efficiency']}
Readability: {scores['readability']}
Modularity: {scores['modularity']}
Edge Handling: {scores['edge']}
Similarity: {scores['similarity']}%

Detected Complexity: {complexity}

Suggestions:
• Improve variable naming clarity
• Add comments explaining logic
• Optimize nested loops if present
• Handle empty inputs and edge cases
• Break logic into reusable functions
"""
