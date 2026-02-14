from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='harsha bheemanathi',
    author_email='bheemanathiharsha@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)