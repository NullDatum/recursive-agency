"""Demonstrate basic AgencyEngine usage."""

from recursive_agency import AgencyEngine


def run_demo() -> None:
    engine = AgencyEngine()
    prompt = "What is intelligence?"
    response = engine.generate_response(prompt)
    artifact = engine.forge("raw idea")
    reflection = engine.reflect()
    print(response)
    print(artifact)
    print(reflection)


if __name__ == "__main__":
    run_demo()
