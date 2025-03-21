from lxml import etree # type: ignore
from docx import Document # type: ignore

with open('Src/arquivo.xml', 'rb') as file:
    xml_data = file.read()

root = etree.fromstring(xml_data)

namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
# Definir namespaces e buscar dados do XML
namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
item_element = root.xpath('//nfe:ide/nfe:cNF', namespaces=namespaces)
nNF_element = root.xpath('//nfe:ide/nfe:nNF', namespaces=namespaces)
cProd_element = root.xpath('//nfe:prod/nfe:cProd', namespaces=namespaces)
xProd_element = root.xpath('//nfe:prod/nfe:xProd', namespaces=namespaces)

# Extrair valores do XML
item_value = item_element[0].text if item_element else "Valor não encontrado"
nNF_value = nNF_element[0].text if nNF_element else "Valor não encontrado"
cProd_value = cProd_element[0].text if cProd_element else "Valor não encontrado"
xProd_value = xProd_element[0].text if xProd_element else "Valor não encontrado"
doc = Document(r'C:\Users\EricCosta\Documents\Projeto_Mercato\NFC-maneger\NFC-maneger\Src\CertificadoConf.docx')

# Substituir ou adicionar o texto acima da tabela
for paragraph in doc.paragraphs:
    if "NF: N°" in paragraph.text:  # Localiza o parágrafo com "NF: N°"
        paragraph.text = f"NF: N° {nNF_value}"  # Substitui pelo valor de <nNF>

doc.save('arquivo_atualizado.docx')