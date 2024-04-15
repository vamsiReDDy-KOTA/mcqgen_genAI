from setuptools import find_packages,setup

setup(
    name="ncqgenrator",
    version="0.0.1",
    author="Vamsi Reddy",
    author_email="kotavamsi16@gamil.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv", "PyPDF2"],
    packages=find_packages()
)