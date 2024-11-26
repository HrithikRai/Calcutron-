'''
ZenML Step for Data Ingestion and Preprocessing
We'll create a ZenML step for data collection (feedbacks + source) and preprocessing (tokenization, cleaning, etc.).
'''

from zenml.steps import step
from langchain_community.document_loaders import PyPDFLoader
loader_pdf = PyPDFLoader('data/raw_data/mother-doc.pdf')
rag_data = loader_pdf.load()
