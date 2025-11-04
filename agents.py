from groq_call import call_llm
import json


def parse_json(text): #for proper loading
    
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        
        try:
            json_str = text[text.find("{"):text.rfind("}")+1]
            return json.loads(json_str)
        except Exception:
            return {"status": "failed", "details": "Invalid JSON output", "raw": text}


class Validator:
    @staticmethod
    def validate_output(data: dict, persona: str, check_type: str) -> dict:
        """Validate and refine LLM output according to persona and content rules."""
        # null check
        if not data or not isinstance(data, dict):
            return {"status": "failed", "details": "No data to validate"}

        
        prompt = f"""
        You are a helpful text reviewer.
        Persona Type: {persona}
        Validation Task: Review this {check_type} for tone, continuity, and persona match.
        If something feels off or away from context, rewrite lightly while keeping structure same.
        
        Rules:
        - Explorer: Curious, pattern-finder, logical clarity
        - Builder: Learns by trying, practical, structured
        - Dreamer: Emotional, imaginative, poetic tone
        - Challenger: Confident, calm, resilient
        
        Here is the data to check:
        {json.dumps(data, indent=2)}
        
        Respond ONLY with corrected JSON in same format.
        """

        response = call_llm(prompt)
        checked = parse_json(response)
        return checked if "status" not in checked else data  # fallback to original if invalid


class Generator:
    @staticmethod
    def generate_persona_scenario(persona: str) -> dict:
        """Generate 7-day storyline + overall story for the persona."""
        prompt = f"""
        You are a JSON-only storyteller. Respond ONLY with valid JSON.

        Persona: {persona}

        Task:
        Create a one-week storyline (7 days) for this persona.
        Output the following structure ONLY:
        {{
            "Overall_story": "<2-3 sentence overview of the journey>",
            "persona_scenario": [
                "DAY 1 — <storyline>",
                "DAY 2 — <storyline>",
                ...
                "DAY 7 — <storyline>"
            ]
        }}
        """

        response = call_llm(prompt)
        data = parse_json(response)

        if "Overall_story" not in data or "persona_scenario" not in data:
            return {"status": "failed", "details": "Invalid persona_scenario output", "raw": response}
        validated = Validator.validate_output(data, persona, "persona_scenario")
        return validated
        return data

    @staticmethod
    def generate_persona_subscenario(persona_scenario: list, persona: str) -> dict:
        """Generate 7-day substory twists for each day in the persona_scenario."""
        scenario_text = "\n".join(persona_scenario)

        prompt = f"""
        You are a JSON-only storyteller. Respond ONLY with valid JSON.

        Persona: {persona}
        Storyline:
        {scenario_text}

        Task:
        For each day above, generate a short 1-line substory twist that adds intrigue or reflection.

        Output this structure ONLY:
        {{
            "persona_subscenario": [
                "DAY 1 — <substory>",
                "DAY 2 — <substory>",
                ...
                "DAY 7 — <substory>"
            ]
        }}
        """

        response = call_llm(prompt)
        data = parse_json(response)

        if "persona_subscenario" not in data:
            return {"status": "failed", "details": "Invalid subscenario output", "raw": response}

        validated = Validator.validate_output(data, persona, "persona_subscenario")
        return validated

