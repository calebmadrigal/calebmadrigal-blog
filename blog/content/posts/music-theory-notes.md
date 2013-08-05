author: Caleb Madrigal
comments: true
date: 2012-11-23 23:11:39
layout: post
slug: music-theory-notes
title: Music Theory and Math Notes
category: math
tags: math, music, python

For the last day, I've done some reading on music theory (trying to understand why things are the way they are in terms of math).  Here are my raw unedited notes:
	
## Important musical ratios:
* Unison: 1:1 frequency
* Octave: 2:1 frequency
    - 12 semitone increase
* Fifth: 3:2 frequency (i.e. multiply by 1.5)
    - 7 semitone increase
* Semitone: 2^(1./12) (12th root of 2) - about 1.059 - this is the "half-step" distance, so you can multiply the frequency of F by 1.059 to get the frequency for F#

## Scales and keys
* Chromatic scale: 12 notes (list of all semitones in an octave)
* Diatomic scale: 7 notes
* To be in a "key" (like C-major) means to select 7 notes from the 12 notes in the chromatic scale
    - In theory, these notes sound good together
* C-major is the white keys on the piano staring on C
    - There is no E# or B# notes on the piano (because the notes in the diatonic scale are determined by going up fifths). So the interval between the white keys (which don't have a black key in between them) are half-tones (i.e. "semitones"). Each key increase is a "half tone" increase (including black keys).
        * See python program below to generate chromatic scale
* Major key intervals can be derived by starting on C and hitting 7 white key
    - Intervals: whole whole half whole whole whole half
* Minor key intervals can be derived by starting on A and hitting 7 white keys
    - Intervals: whole half whole whole half whole whole
	
## Chords
	
* Major chord ratios: 4:5:6
    - The original note
    - A major 3rd
    - A perfect fifth (notice that 4 * 1.5 = 6)
* Minor chord ratios: 10:12:15
    - The original note
    - A minor 3rd
    - A perfect fifth (notice that 10 * 1.5 = 15)
* In a "key", there are 7 chords (numbered I, II, III, IV, V, VI, VII).
    - To determine if which chords (major or minor) are in a key, start at each of the 7 notes in the key and see which chords "fit" into that key (all notes in the chords must be in the key as well).


## Note generation example with python
Python to generate the 12 basic notes (starting with the note F1 = 43.65Hz):

    >>> notes = []
    >>> acc = f1
    >>> for i in range(12):
    ...     notes.append(acc)
    ...     acc = acc * 1.5
    ...
    >>> notes
    [43.65, 65.475, 98.21249999999999, 147.31875, 220.97812499999998, 331.46718749999997, 497.20078125, 745.8011718749999, 1118.7017578124999, 1678.05263671875, 2517.0789550781246, 3775.618432617187]
    >>> note_names = ['f', 'c', 'g', 'd', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']
    >>> 3729 * 1.5
    5593.5
    >>> 5593.5 / f1
    128.1443298969072
    >>> # f8 should equal 5587 Hz. So from A#, if we go up a fifth, we are at F8,
    >>> # which is a 7 octaves higher than F1 (2^7 = 128).  128* F1 = F8.


## Sources
	
* [http://en.wikipedia.org/wiki/Piano_key_frequencies](http://en.wikipedia.org/wiki/Piano_key_frequencies)
* [http://www.pianoworld.com/forum/ubbthreads.php/topics/988787/E%20Sharp,%20B%20Sharp.html](http://www.pianoworld.com/forum/ubbthreads.php/topics/988787/E%20Sharp,%20B%20Sharp.html)
* [http://www.phy.mtu.edu/~suits/chords.html](http://www.phy.mtu.edu/~suits/chords.html)
* Michael New's video tutorials:
    - [http://www.youtube.com/watch?v=5Y01jIorpeA](http://www.youtube.com/watch?v=5Y01jIorpeA)
    - [http://www.youtube.com/watch?v=rHlWP-nc4tM](http://www.youtube.com/watch?v=rHlWP-nc4tM)
    - [http://www.youtube.com/watch?v=xLaw0CLTNfA&feature=relmfu](http://www.youtube.com/watch?v=xLaw0CLTNfA&feature=relmfu)







