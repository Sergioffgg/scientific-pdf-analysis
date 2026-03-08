from lxml import etree

def extract_abstract(xml):
    tree = etree.fromstring(xml.encode())
    parts = tree.xpath("//*[local-name()='abstract']//*[local-name()='p']//text()")
    return " ".join(parts).strip()

def count_figures(xml):
    tree = etree.fromstring(xml.encode())
    return len(tree.xpath("//*[local-name()='figure']") + tree.xpath("//*[local-name()='graphic']"))

def extract_links(xml):
    tree = etree.fromstring(xml.encode())
    return tree.xpath("//*[local-name()='ref'][@type='url']/@target")