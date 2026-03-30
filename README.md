## ARABIZI FOR COLLOQUIAL ARABIC : THE TUNISIAN CASE

In the early 2000s, most keyboards were based on the Latin script and were not adapted to North African Arabic dialects. Users adapted the Latin Alphabet to represent Arabic sounds, developing a phonetic writing system based on both letters and numbers to encode non-latin sounds such as uvular, emphatic and laryngeal consonants.

## About this project

This project aims to provide solutions for complex cases in the Arabizi writing system, such as emphatic consonants, the hamza and the tāʾ marbūṭa.

## COMPLEX CASES 

## The case of emphatics الحروف المفخمة :

Tunisian arabic is characterized by the weakening or reduction of emphatic consonants, including /ṭ/, /ẓ/, /ḍ/, and /ṣ/. 

In the first part of the project, we opted to handle ambiguous cases by assigning a default value corresponding to the non-emphatic consonant. Rather than distinguishing emphatic from non-emphatic sounds, this approach manages ambiguity by providing a consistent default output. When the converter processes an ambiguous input (e.g. 's', 'dh', 't'), it defaults to their non-emphatic counterparts (/ẓ/ vs. /ḍ/, /ṭ/ vs. /t/, and /ṣ/ vs. /s/). As a result, the underlying form may correspond to either an emphatic or a non-emphatic realization. This default setting was introduced to manage ambiguity.

## The case of the hamza 'ء' : 

In Tunisia, the Standard Arabic hamza weakens and is typically realized as /a/, similar to the alif. In certain areas of the Sahel, some words exhibit a realization of /i/ instead, particularly in final position. These variants correspond to geographical (diatopic) differences across the dialects.

## The case of the ta marbouta 'ة' :

The tāʾ marbūṭa is a word-final form of the letter (ت). It is typically pronounced /a/ but it surfaces as /t/ in annexation structures, as in "my friend's car" --> "karahbet sa7bi". In this example, the tāʾ marbūṭa is realized as /t/ in karahba due to its phonological connection to the following word. Its primary function is to mark the feminine gender, it is not exclusively associated with feminine nouns, as some masculine words also carry this ending. It also shifts to the open tāʾ form (tāʾ maftūḥa) when followed by a suffix, as in the previous example. 

## The case of short and long vowels الحركات :

## The case of weak verbs الفعل المعتل :
