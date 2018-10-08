# -*- coding: utf-8 -*-

import unittest
from extractor import phrases_extractor


class TestPhraseExtractor(unittest.TestCase):

    def test_get_terms(self):
        text = '''Shanghai lies on China's east coast roughly equidistant from Beijing and Guangzhou. 
        The Old City and modern downtown Shanghai are now located in the center of an expanding peninsula 
        between the Yangtze River Delta to the north and Hangzhou Bay to the south.
        '''
        grammar = r"""
            NP:   {<NNP>?<NNP>?}
        """
        label = 'NP'
        terms = phrases_extractor.get_phrases(text, grammar, label)
        self.assertEqual(terms, ['Old City','Yangtze River','Hangzhou Bay'])


suite = unittest.TestLoader().loadTestsFromTestCase(TestPhraseExtractor)
unittest.TextTestRunner(verbosity=2).run(suite)