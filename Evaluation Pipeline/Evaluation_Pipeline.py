from openai import OpenAI
from collections import Counter
import matplotlib.pyplot as plt
import textstat

client = OpenAI(api_key="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")

stories = []
for i in range(20):
    prompt = f"Write a 200-word creative story about a cat traveling the world, version {i+1}"
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[{"role": "user", "content": prompt}]
    )
    stories.append(response.choices[0].message.content)

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

plt.bar(range(1, 21), scoresForLexicalDiversity)
plt.xlabel("Story number")
plt.ylabel("Lexical diversity")
plt.show()

#readability
scoresForReadablity = [textstat.flesch_reading_ease(s) for s in stories]
plt.bar(range(1, 21), scoresForReadablity)
plt.xlabel("Story number")
plt.ylabel("Readablity")
plt.show()