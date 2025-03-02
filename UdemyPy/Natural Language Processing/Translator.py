import asyncio
from googletrans import Translator

async def translate(text,lang):
    translator = Translator()
    translation = await translator.translate(text, dest=lang)
    return translation

async def main():
    while True:
        question = input("\nHi there, What do you want to translate?\n")
        if question.lower() == 'quit':
            break
        output = await translate(question, 'es')
        if output:
            print(output.text)
        else:
            print("I don't know!")

asyncio.run(main())
