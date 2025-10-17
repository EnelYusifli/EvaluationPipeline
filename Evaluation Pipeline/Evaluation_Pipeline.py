#!/usr/bin/env python3

from openai import OpenAI
from collections import Counter
import matplotlib.pyplot as plt
import textstat
import time

client = OpenAI(api_key="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")



import time

stories = []
for i in range(3):
    print(f"Generating story {i+1}...")
    prompt = f"Write a 200-word creative story about a cat traveling the world, version {i+1}"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": prompt}]
        )
        stories.append(response.choices[0].message.content)
    except Exception as e:
        print(f"Error generating story {i+1}: {e}")
    time.sleep(20)  # Wait 20 seconds to avoid rate limits

print("All stories generated!")


with open("stories.txt", "w") as f:
    f.write("\n\n---\n\n".join(stories))

# Criterion	Example evaluation idea
# Lexical diversity	Count how many unique words appear per story
# Sentiment	Use a sentiment analysis tool (like TextBlob, Hugging Face model)
# Readability	Use a readability score (Flesch-Kincaid)
# Repetition / redundancy	Count how often phrases repeat
# Coherence	Check average sentence similarity (using embeddings)
# Emotion richness	Count emotion-related words (joy, sadness, fear...)
# Length consistency	Compare average word counts


def lexical_diversity(text):
    words = text.lower().split()
    return len(set(words)) / len(words)

scoresForLexicalDiversity = [lexical_diversity(story) for story in stories]

num_stories = len(stories)

plt.bar(range(1, num_stories+1), scoresForLexicalDiversity)
plt.xlabel("Story number")
plt.ylabel("Lexical diversity")

plt.savefig("lex_diver.png")

plt.show()

#readability
scoresForReadability = [textstat.flesch_reading_ease(s) for s in stories]
plt.bar(range(1, num_stories+1), scoresForReadability)
plt.xlabel("Story number")
plt.ylabel("Readablity")

plt.savefig("readability.png")

plt.show()


