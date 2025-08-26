from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f" Warning: {filename} not found.")
        return ""

def main():
    # Read inputs from text files
    company_name = read_file("company_name.txt")
    job_role = read_file("job_role.txt")
    job_description = read_file("job_description.txt")
    resume_info = read_file("resume_info.txt")
    questions = read_file("questions.txt")

    # Big prompt template
    big_prompt = f"""
You are a skilled writer who handcrafts letters from scratch despite being in a generation where LLMs can write letters for you. Your selling point is making a letter sound very human, thoughtful and heartfelt.

I want you to write me responses to the following questions that I provide with the following requirements:

- Use British spelling.
- Do not use negating statements like “Not only do I bring curiosity to your company, but also resilience and respect.”
- Do not use em dashes ‘—’. Anywhere you would naturally write one, replace it with a comma or restructure the sentence.
- Do not fabricate details. If I do not have directly relevant experience, highlight transferable experience instead.
- Write directly and concisely, without filler or bloated phrases that add little meaning.
- When using company research, do not cite sources or list stats like a scraper. Instead, summarise naturally in plain language, as if I had read about them myself. Bring in one or two cultural or strategic points that feel relevant, and connect them to my experiences or motivations in a human way.

Here is the company name:

{company_name}

Here is the role and job description:

{job_role}
{job_description}

Here are my experiences, projects, and skills:

{resume_info}

Here are the application questions I would like you to help me answer in the same tone and style:

{questions}

Here is a template you can follow for the style of writing:

---

Dear Hiring Manager,

I am writing to express my interest in the < job title > Internship at < company name > in London. As a second-year Computer Science student at City, University of London, I have developed strong < analytical / research / technical > skills that I am eager to apply in <company name>’s <collaborative / entrepreneurial / dynamic> environment.

While <insert relevant project, experience, or academic work> I <what did I do?> to <why?>, <result?>. This project reflects <company name>’s focus on <relevant theme or value>.

Beyond this, I gained valuable exposure to <industry / business / teamwork> through <internship / freelance / research>. These experiences shaped my ability to <skill>, and to collaborate effectively, which are directly relevant to <company name>’s work in <projects / client engagements>.

I am particularly drawn to <company name> because of its <unique quality, culture, or strategic approach>, which, for me, <personal reflection>. I am confident that my ability to <relevant skill or quality> would allow me to contribute meaningfully to <specific division or client-facing work>.

Thank you for considering my application. I would welcome the opportunity to bring my <skills / perspective / passion> to <company name> and to contribute to a team whose work I <admire>.

Yours sincerely,

Yusuf Ahmed
"""

    # Save to PDF
    file_name = "cover_letter_prompt.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in big_prompt.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), styles["Normal"]))
        story.append(Spacer(1, 6))

    doc.build(story)
    print(f"\n Prompt saved as {file_name}. You can now copy-paste it into ChatGPT.")

if __name__ == "__main__":
    main()
