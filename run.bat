@echo off
call "%~dp0venv\Scripts\activate"
streamlit run "%~dp0app.py"
