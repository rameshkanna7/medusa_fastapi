import re


def preprocess_text(text):
    # Split text into words, lowercase them, and remove punctuation
    words = re.findall(r"\w+", text.lower())
    return words


def common_word_percentage(a, b):
    a_words = set(preprocess_text(a))
    b_words = set(preprocess_text(b))

    common_words = a_words.intersection(b_words)
    total_words = a_words.union(b_words)

    percentage = len(common_words) / len(total_words) * 100
    return common_words, percentage


# Input texts
text1 = """SEP : 
DIM : 17 cm
COT : 8-135
TIT :  CATALOGUE DES OUVRAGES D’ART ET D’INDUSTRIE, exposés dans les Salons de la Mairie de Valenciennes, Depuis le 9 septembre until’au 15 octobre 1838
EDI : VALENCIENNES, IMPRIMERIE de A. Prignet
DAT : 1838
ILL : nb.
NUL : 
NUL : 
PGN : 55
TC : 100%"""

text2 = """Rec: UNIMARC MARC: 
0 cam0   
1 023394900
3 http://www.sudoc.fr/023394900
5 20231022100443.000
35   $a(OCoLC)25827212
35   $aocm25827212
100   $a19920515d1838    u  y0frey50      ba
101 0 $afre $2639-2
102   $aFR
105   $ay   b   000|y
181   $6z01 $ctxt $2rdacontent
181  1$6z01 $ai# $bxxxe##
182   $6z01 $cn $2rdamedia
182  1$6z01 $an
200 0 $aCatalogue des ouvrages d'art and d'industrie exposés dans les Salons de Mairie de Valenciennes $e9 sept. until’au 15 oct. 1838 ...
210   $aValenciennes $cimpr. de A. Prignet $d1838
215   $a55 p. $d14 x 8 cm
801  3$aFR $bAbes $c20231022 $gAFNOR
801  1$aUS $bOCLC $gAACR2
801  2$aFR $bAUROC
915   $5751025206:057871345 $aA/3 H 10
917   $5751025206:057871345 $auubu
930   $5751025206:057871345 $b751025206 $eFIAA $a8 H 14 (6) $jg
999   $5751025206:057871345 $zA/3 H 10
"""

# Calculate common words and percentage
common_words, percentage = common_word_percentage(text1, text2)

print("Common words in both texts:")
for word in common_words:
    print(word)

print(f"Percentage of common words: {percentage:.2f}%")
