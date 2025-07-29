# src/ranker.py

from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.segmenter import Section

def rank_sections(sections: List[Section], persona: Dict) -> List[Dict]:
    """
    Ranks sections based on cosine similarity between TF-IDF vectors of section text and persona's job.

    Args:
        sections (List[Section]): Sections from segmenter.py
        persona (Dict): Contains 'job_to_be_done' and optional 'focus' list

    Returns:
        List[Dict]: Ranked section dictionaries with importance_rank
    """

    # Combine job description + focus areas into one search query
    job_text = persona.get("job_to_be_done", "")
    focus_areas = " ".join(persona.get("focus", []))
    query_text = job_text + " " + focus_areas

    # Prepare corpus for TF-IDF: first item is query, rest are section texts
    corpus = [query_text] + [sec.title + " " + sec.text for sec in sections]

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(corpus)

    # Compute cosine similarity of query vs each section
    scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    ranked = []
    for idx, (section, score) in enumerate(zip(sections, scores)):
        ranked.append({
            "document": section.doc_name,
            "page": section.page,
            "section_title": section.title,
            "refined_text": section.text,
            "score": float(score)
        })

    # Sort and assign ranks
    ranked.sort(key=lambda x: x["score"], reverse=True)
    for i, r in enumerate(ranked, start=1):
        r["importance_rank"] = i

    return ranked
