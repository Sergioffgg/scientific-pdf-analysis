from trabajo1.analysis import count_figures

def test_count_figures():
    sample_xml = """
    <TEI>
        <figure></figure>
        <figure></figure>
        <figure></figure>
    </TEI>
    """

    count = count_figures(sample_xml)

    assert count == 3