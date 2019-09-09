from bs4 import BeautifulSoup
import urllib.request
import pickle

def scrape_to_file(url, file_to_save):
    quote_page = url

    page = urllib.request.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    text = soup.get_text()

    edges = []

    for line in text.splitlines():
        if (line[0] == 'e'):
            i = 3
            while (line[i] != ' '):
                i += 1

            v_out = int(line[2:i])
            v_in = int(line[i+1:len(line)])
            edges.append([v_out, v_in])

    with open(file_to_save + '.pickle', 'wb') as fp:
        pickle.dump(edges, fp)

    print('Success')
    return 

scrape_to_file('https://turing.cs.hbg.psu.edu/txn131/file_instances/coloring/graph_color/queen10_10.col', '10x10')
