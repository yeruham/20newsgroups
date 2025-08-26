from sklearn.datasets import fetch_20newsgroups


def get_newsgroups_interesting():
     interesting_categories = ['alt.atheism',
                               'comp.graphics',
                               'comp.os.ms-windows.misc',
                               'comp.sys.ibm.pc.hardware',
                               'comp.sys.mac.hardware',
                               'comp.windows.x',
                               'misc.forsale',
                               'rec.autos',
                               'rec.motorcycles',
                               'rec.sport.baseball']

     newsgroups_interesting = fetch_20newsgroups(subset='all', categories=interesting_categories)
     return newsgroups_interesting.data


def get_newsgroups_not_interesting():

     not_interesting_categories = ['rec.sport.hockey',
                                   'sci.crypt',
                                   'sci.electronics',
                                   'sci.med',
                                   'sci.space',
                                   'soc.religion.christian',
                                   'talk.politics.guns',
                                   'talk.politics.mideast',
                                   'talk.politics.misc',
                                   'talk.religion.misc']

     newsgroups_not_interesting = fetch_20newsgroups(subset='all', categories=not_interesting_categories)
     return newsgroups_not_interesting.data



def iter_data(data: list, num: int):
    for i in range(0, len(data), num):
        yield data[i: i+num]