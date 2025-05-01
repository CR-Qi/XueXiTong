from agno.agent import Agent
from agno.models.ollama import Ollama

Paragraph_classifier = Agent(
    model=Ollama(
        id="qwen3:latest",
        host="http://localhost:11434"
        ),
    description="You are a paragraph classifier for scientific papers in covalent organic framework materials chemistry.",
    instructions="Classify paragraph into Synthesis, Testing, Application, or Other. Return only the category name.",
    goal="Return the category name.",
    retries=3,
)

para = "BTA-COF1. Compound 2 (0.44 g, 1 mmol) and HHTP (0.32 g, 1 mmol) were placed into a 100 mL Schlenk flask. Mesitylene (25 mL) and 1,4-dioxane (25 mL) were added, and the mixture was degassed under reduced pressure. Then the mixture was heated at 85 °C with stirring for 72 h. The obtained suspension was left to stand, and the supernatant solvent was carefully decanted with a syringe. THF (50 mL) was added, and the mixture was stirred overnight. The washing with THF was repeated twice in the same manner. The obtained slurry was dried in vacuo at 85 °C for 24 h to afford the product as a gray powder. Final removal of remaining guest molecules was accomplished by heating in vacuo at 200 °C for 12 h. Yield = 0.56 g (86%)."
Paragraph_classifier.print_response(para)
