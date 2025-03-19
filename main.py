from lxml import etree # type: ignore
from docx import Document # type: ignore

with open('arquivo.xml', 'r', encoding='utf-8') as file:
    xml_data = file.read()