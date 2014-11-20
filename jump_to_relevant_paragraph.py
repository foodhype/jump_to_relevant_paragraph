import bs4
import re
import tfidf


def jump_to_relevant_paragraph(question, html):
    paragraphs = []
    table = tfidf.tfidf()
    input_soup = bs4.BeautifulSoup(html)
    
    for index, paragraph in enumerate(input_soup.find_all("p")):
        paragraphs.append(paragraph.text)
        words = extract_words(paragraph.text)
        table.addDocument(index, words)
    
    question_words = extract_words(question)
    most_relevant_paragraph_index = max(table.similarities(question_words),
            key=lambda (paragraph_index, score):score)[0]

    output = []
    for paragraph in paragraphs[most_relevant_paragraph_index:]:
        output.append("".join(["<p>", paragraph, "</p>"]))

    return "".join(output)


def extract_words(text):
    return [word.lower() for word in re.split("\W", text) if word]
