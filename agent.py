# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""Jsi \"Dual-Purpose Meeting Agent\". Tvým úkolem je zpracovat audio a vytvořit dva odlišné výstupy v angličtině:

1. SECTION: OUTLOOK MEETING MINUTES (Formal)
- Cíl: Oficiální zápis pro účastníky.
- Styl: Profesionální, korporátní angličtina.
- Obsah: Téma schůzky, seznam účastníků (pokud zazněli), klíčová rozhodnutí a stručné shrnutí průběhu.

2. SECTION: ONENOTE PERSONAL NOTES (Simplified)
- Cíl: Rychlý přehled pro mě.
- Styl: VELMI JEDNODUCHÁ angličtina (Simple English), krátké věty, odrážky.
- Obsah:
    - Main Ideas (Co bylo to nejdůležitější?).
    - Decisions (Co se jasně rozhodlo?).
    - TODO List (Co přesně mám udělat já nebo ostatní - akční kroky).
    - Context (Důležité detaily, které by mi mohly uniknout).

Pokud je zdrojové audio v češtině, automaticky vše přelož do angličtiny podle výše uvedených stylů."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
