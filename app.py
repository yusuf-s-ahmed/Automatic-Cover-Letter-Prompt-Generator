from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import streamlit as st

def save_to_pdf(prompt, file_name="cover_letter_prompt.pdf"):
    """Save the generated prompt to a PDF file."""
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in prompt.split("\n"):
        if line.strip():
            story.append(Paragraph(line.strip(), styles["Normal"]))
        story.append(Spacer(1, 6))

    doc.build(story)
    return file_name

def generate_cover_letter_prompt(company_name, job_role, job_description, resume_info, questions=None):
    """Generate the tailored prompt based on user inputs."""
    base_prompt = f"""
You are a skilled writer who handcrafts letters from scratch despite being in a generation where LLMs can write letters for you. Your selling point is making a letter sound very human, thoughtful and heartfelt.

I want you to write me a cover letter with the following requirements:

- I am a second year Computer Science student at City University of London with a strong interest in finance and technology.
- When you refer to 'Largence Group Ltd.', 'Vital Therapy Ltd.', and 'Sybertnetics Artificial Intelligence, Inc.', clarify their industries before introducing them, e.g. "My work at an internet technology company, Largence Group Ltd., a health technology company, Vital Therapy Ltd. and an AI startup company, Sybertnetics Artificial Intelligence, Inc."
- If it's a finance-heavy related role, highlight my experience with finance, then my technical skills and projects.
- Use British spelling.
- Do not use negating statements like “Not only do I bring curiosity to your company, but also resilience and respect.”
- Do not use em dashes ‘—’. Anywhere you would naturally write one, replace it with a comma or restructure the sentence.
- Do not fabricate details. If I do not have directly relevant experience, highlight transferable experience instead.
- Write directly and concisely, without filler or bloated phrases that add little meaning.
- When using company research, do not cite sources or list stats like a scraper. Instead, summarise naturally in plain language, as if I had read about them myself. Bring in one or two cultural or strategic points that feel relevant, and connect them to my experiences or motivations in a human way.
- Lead with most relevant experiences and skills.
- Don't use the terms 'rigour', 'underpins',  replace it with something else.
- If you can, highlight how I want to stay at the company long-term and grow with them.
- Start the cover letter off with I am a second year Computer Science student at City, University of London, and I am writing to express my interest in [role] at [company] in London. Then, in the next sentence, briefly summarise why I am interested in the role and company.

Here is the company name:

{company_name}

Here is the role and job description:

{job_role}
{job_description}

Here are my experiences, projects, and skills:

{resume_info}
"""
    if questions:
        base_prompt += f"""

Here are the application questions I would like you to help me answer in the same tone and style:

{questions}
"""
    return base_prompt

def generate_questions_prompt(company_name, job_role, job_description, resume_info, questions=True):
    """Generate the tailored prompt based on user inputs."""
    base_prompt = f"""
You are a skilled writer who handcrafts letters from scratch despite being in a generation where LLMs can write letters for you. Your selling point is making a letter sound very human, thoughtful and heartfelt.

I want you to write me responses to job application questions with the following requirements:

- I am a second year Computer Science student at City University of London with a strong interest in finance and technology.
- When you refer to Largence Group Ltd, clarify that is is a internet technology company before introducing it, Vital Therapy Ltd is a health technology company, Sybertnetics AI Solutions is an AI startup company.
- Use British spelling.
- Do not use negating statements like “Not only do I bring curiosity to your company, but also resilience and respect.”
- Do not use em dashes ‘—’. Anywhere you would naturally write one, replace it with a comma or restructure the sentence.
- Do not fabricate details. If I do not have directly relevant experience, highlight transferable experience instead.
- Write directly and concisely, without filler or bloated phrases that add little meaning.
- When using company research, do not cite sources or list stats like a scraper. Instead, summarise naturally in plain language, as if I had read about them myself. Bring in one or two cultural or strategic points that feel relevant, and connect them to my experiences or motivations in a human way.
- Lead with most relevant experiences and skills.
- Don't use the terms 'rigour', 'underpins', 'resonates', replace it with something else.
- If you can, highlight how I want to stay at the company long-term and grow with them.

Here is the company name:

{company_name}

Here is the role and job description:

{job_role}
{job_description}

Here are my experiences, projects, skills and extracurriculars:

{resume_info}
"""
    if questions:
        base_prompt += f"""

Here are the application questions I would like you to help me answer in the tone and style I described above:

{questions}
"""
    return base_prompt

def generate_latex(prompt):
    """Generate LaTeX code for the cover letter."""
    latex_template = r"""
\documentclass[letterpaper,11pt]{article}

\usepackage[english]{babel}
\usepackage[empty]{fullpage}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{tabularx}
\usepackage{graphicx}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\begin{document}

%----------HEADING----------
\begin{center}
    \textbf{\LARGE Yusuf Ahmed} \\ \vspace{1pt}
    \small London, UK $|$ 
    \small +447897705492 $|$ \href{mailto:yusufahmed101@icloud.com}{\underline{yusufahmed101@icloud.com}} $|$ 
    \href{https://linkedin.com/in/yusuf-s-ahmed}{\underline{linkedin.com/in/yusuf-s-ahmed}} 
\end{center}

%----------BODY----------
{prompt}

\bigskip

%----------CLOSING----------
Yours sincerely, \\  
Yusuf Ahmed

\end{document}
"""
    return latex_template.replace("{prompt}", prompt)

def main():
    st.title("Auto-Tailored Cover Letter Prompt Generator")

    st.text("""This application helps you generate a tailored prompt for writing cover letters based on your inputs. Fill in the details below and click "Generate Prompt" to create your personalised prompt, save it as a PDF, and get the LaTeX code for your cover letter.""")

    st.link_button("Trackr", "https://www.the-trackr.com/")
    st.link_button("Overleaf", "https://www.overleaf.com/project")

    # Input fields for user data
    st.header("Enter the required details:")
    company_name = st.text_input("Company Name")
    job_role = st.text_area("Job Role")
    job_description = st.text_area("Job Description")
    resume_info = st.text_area("CV + Extracurricular Information")
    questions = st.text_area("Application Questions (Optional)")

    if st.button("Generate Prompt"):
        if not (company_name and job_role and job_description and resume_info):
            st.error("Please fill in all required fields before generating the prompt.")
        else:
            if questions.strip():
                prompt = generate_questions_prompt(company_name, job_role, job_description, resume_info, questions)
            else:
                prompt = generate_cover_letter_prompt(company_name, job_role, job_description, resume_info)

            # Save the prompt to a PDF
            file_name = save_to_pdf(prompt)
            st.success(f"Prompt generated and saved as {file_name}.")

            # Display the prompt in the app
            st.header("Generated Prompt:")
            st.text_area("Prompt", prompt, height=400)

            # Provide a download link for the PDF
            with open(file_name, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name=file_name,
                    mime="application/pdf"
                )

            # Generate LaTeX code
            latex_code = generate_latex(prompt)

            # Provide a download link for the LaTeX file
            st.header("Generated LaTeX Code:")
            st.text_area("LaTeX Code", latex_code, height=400)
            st.download_button(
                label="Download LaTeX File",
                data=latex_code,
                file_name="cover_letter.tex",
                mime="text/plain"
            )

            # -------------------------
            # Static instruction block for ChatGPT
            # -------------------------
            st.header("Copy for ChatGPT:")
            chatgpt_instruction = r"""Apply that cover letter to this LaTex code:

\documentclass[letterpaper,11pt]{article}

\usepackage[english]{babel}
\usepackage[empty]{fullpage}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{tabularx}
\usepackage{graphicx}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

%-------------------------------------------
% COVER LETTER STARTS HERE

\begin{document}

%----------HEADING----------
\begin{center}
    \textbf{\LARGE Yusuf Ahmed} \\ \vspace{1pt}
    \small London, UK $|$ 
    \small +447897705492 $|$ \href{mailto:yusufahmed101@icloud.com}{\underline{yusufahmed101@icloud.com}} $|$ 
    \href{https://linkedin.com/in/yusuf-s-ahmed}{\underline{linkedin.com/in/yusuf-s-ahmed}} $|$ 
    \href{https://github.com/yusuf-s-ahmed}{\underline{github.com/yusuf-s-ahmed}} 
\end{center}

%----------COMPANY ADDRESS----------
\begin{tabular}{@{} l}
  \vspace{1em}
  August 26, 2025 \\  
  Rothschild \& Co.
\end{tabular}

\vspace{1em}

%----------BODY----------
RE: 2026 UK Global Advisory Spring Insight Programme

\vspace{1em}

Dear Hiring Manager,

\vspace{1em}

I am writing to express my interest in the 2026 UK Global Advisory Spring Insight Programme at Rothschild \& Co. in London. As a second-year Computer Science student at City, University of London, I have developed strong analytical and problem-solving skills that I am eager to apply in a financial advisory environment.  

\vspace{1em}

While my background is in technology and data analysis, I have completed projects that intersect with finance and investment. For example, I performed a portfolio risk and investment analysis of UK equities, using Python, SQL, Excel, and Power BI to evaluate performance, volatility, and scenario-based risks. This project reflects Rothschild \& Co.’s focus on delivering insightful and data-informed advisory solutions to clients.  

\vspace{1em}

Beyond this, I gained valuable exposure to cross-functional collaboration through my work as a data analyst at Largence Ltd., where I used ETL processes, SQL queries, and Power BI visualisations to support business decisions across engineering and finance teams. These experiences shaped my ability to analyse complex data, communicate findings effectively, and work collaboratively, which are directly relevant to Rothschild \& Co.’s advisory work.  

\vspace{1em}

I am particularly drawn to Rothschild \& Co. because of its culture of thoughtful, client-focused advisory and its emphasis on long-term relationships and integrity. The opportunity to learn from experienced bankers and observe the breadth of advisory services would provide invaluable insight into the financial industry. I am confident that my analytical mindset, technical skills, and collaborative approach would allow me to contribute meaningfully to the programme.  

\vspace{1em}

Thank you for considering my application. I would welcome the opportunity to bring my skills and enthusiasm to Rothschild \& Co. and to contribute to a team whose work I greatly admire.  

\bigskip

%----------CLOSING----------
Yours sincerely, \\  
Yusuf Ahmed


\\end{document}"""
            st.text_area("ChatGPT Instruction", chatgpt_instruction, height=600)

if __name__ == "__main__":
    main()
