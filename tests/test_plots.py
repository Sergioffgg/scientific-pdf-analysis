import os
from trabajo1.plots import plot_wordcloud

def test_wordcloud_generation():

    text = "science data research science analysis"

    plot_wordcloud(text)

    assert os.path.exists("output/wordcloud.png")