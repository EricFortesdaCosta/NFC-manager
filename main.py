from lxml import etree # type: ignore
from docx import Document # type: ignore

with open('Src/arquivo.xml', 'rb') as file:
    xml_data = file.read()

root = etree.fromstring(xml_data)

items = root.xpath('//item')
dados_estraidos = [item.text for item in items]

doc = Document(r'C:\Users\EricCosta\Documents\Projeto_Mercato\NFC-maneger\NFC-maneger\Src\CertGarantia.docx')


doc.add_heading('Dados Atualizados do XML', level=2)
for dado in dados_estraidos:
    doc.add_paragraph(dado)

primeiro_paragrafo = doc.paragraphs[0]
primeiro_paragrafo.add_run('\n\nDados do XML adicionados Abaixo: ')
for dado in dados_estraidos:
    primeiro_paragrafo.add_run(f'\n{dado}')

doc.save('arquivo_atualizado.docx')