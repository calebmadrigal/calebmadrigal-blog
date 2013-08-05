author: Caleb Madrigal
comments: true
date: 2012-11-26 06:19:53
layout: post
slug: pyknon-intro-chords-intervals
title: Pyknon Intro, Chords, and Intervals
category: math
tags: math, music, python

I've continued on my (hopefully) short-term fascination with music+math (it's fun, but really bad for productivity).  So I found this great library for generating music in Python called [Pyknon](http://kroger.github.com/pyknon/).  And it can be installed using pip: `pip install pyknon`.

I wrote a little python script just to help me understand some concepts in music theory like intervals and chords.  It is meant to be read top to bottom (which is why I intersperse functions and variables throughout).  It is NOT written in good modular form (in general, I don't recommend writing python like this).  This code can also be used as an intro to the pyknon library.

Behold:

    
    from pyknon.genmidi import Midi
    from pyknon.music import NoteSeq, Note, Rest
    
    ####### First we'll generate all piano notes
    
    # Pyknon dubs C5 as the value 0, so Note(0) give you C5
    # (C in the 5th octave).  So we have to move 51 keys to the
    # left to get the far left key on a piano.
    first_note = Note("A,,,,,") # The far-left key on the piano
    
    def key_number(n):
        return n.octave * 12 + n.value - first_note.value
    
    def note_from_key_number(k):
        return Note(k - 51)
    
    def intervals(notes):
        interval = []
        for n in range(len(notes)-1):
            interval.append(notes[n+1] - notes[n])
        return interval
    
    piano_notes = map(note_from_key_number, range(88))
    midi = Midi(1, tempo=80)
    midi.seq_notes(piano_notes, track=0)
    midi.write("piano_keys.mid")
    
    ####### Next we'll examine a major and minor scale, and look at the intervals between
    ####### each of their notes
    
    middle_c = Note("C,")     # key_number=39
    note_nums = map(key_number, piano_notes)
    print "All piano notes:", note_nums
    print "Middle C key number:", key_number(middle_c)
    
    # A, means drop the octave, C' means raise the octave.
    # Also, in a NoteSeq, Pyknon stays in the same octave unless explicitly
    # changed by using either , or '.
    C_major = NoteSeq("C D E F G A B C'' ")
    A_minor = NoteSeq("A, B C' D E F G A")
    
    # Note, when defining a NoteSeq, all notes are by default in the same 
    # octave as the starting note.
    print "C major (staring with middle C):", map(key_number, NoteSeq("C, D E F G A B"))
    print "C major:", map(key_number, C_major)
    print "Intervals for C major:", intervals(map(key_number, C_major))
    print "A minor:", map(key_number, A_minor)
    print "Intervals A minor:", intervals(map(key_number, A_minor))
    
    ####### Last we'll generate some chords in a major and minor keys.
    
    def major_chord(root):
        root_key_num = key_number(root)
        return map(note_from_key_number, [root_key_num, root_key_num+4, root_key_num+7])
    
    def minor_chord(root):
        root_key_num = key_number(root)
        return map(note_from_key_number, [root_key_num, root_key_num+3, root_key_num+7])
    
    def dim_chord(root):
        root_key_num = key_number(root)
        return map(note_from_key_number, [root_key_num, root_key_num+3, root_key_num+6])
    
    # Chord qualities: M m m M M m d (M)
    major_chord_progression = [major_chord, minor_chord, minor_chord, major_chord, \
                               major_chord, minor_chord, dim_chord]
    
    # Chord qualities: m d M m m M M (m)
    minor_chord_progression = [minor_chord, dim_chord, major_chord, minor_chord, \
                               minor_chord, major_chord, major_chord]
    
    ####### Generate C major chords ###
    C_maj_chords = []
    for i in range(len(major_chord_progression)):
        C_maj_chords.append(major_chord_progression[i](C_major[i]))
    
    # Throw a "mistake" in there to hear the difference
    C_maj_chords.append([Note("C"), Note("F#"), Note("Bb")])
    
    print "C major chords:", C_maj_chords
    
    midi = Midi(1, tempo=80)
    midi.seq_chords(map(NoteSeq, C_maj_chords))
    midi.write("c_major_chords.mid")
        
    ####### Generate G minor chords ###
    G_minor = NoteSeq("G, A Bb C' D Eb F")
    G_min_chords = []
    for i in range(len(minor_chord_progression)):
        G_min_chords.append(minor_chord_progression[i](G_minor[i]))
    print "G minor chords:", G_min_chords
    
    midi = Midi(1, tempo=80)
    midi.seq_chords(map(NoteSeq, G_min_chords))
    midi.write("g_minor_chords.mid")


And here is the output (excluding the MIDI files it writes):

    
    localhost:music caleb$ python piano_notes.py 
    All piano notes: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
     44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
     67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]
    Middle C key number: 39
    C major (staring with middle C): [39, 41, 43, 44, 46, 48, 50]
    C major: [51, 53, 55, 56, 58, 60, 62, 63]
    Intervals for C major: [2, 2, 1, 2, 2, 2, 1]
    A minor: [48, 50, 51, 53, 55, 56, 58, 60]
    Intervals A minor: [2, 1, 2, 2, 1, 2, 2]
    C major chords: [[<c>, <e>, <g>], [<d>, <f>, <a>], [<e>, <g>, <b>], [<f>, <a>, <c>],
     [<g>, <b>, <d>], [<a>, <c>, <e>], [<b>, <d>, <f>], [<c>, <F#>, <A#>]]

    G minor chords: [[<g>, <A#>, <d>], [<a>, <c>, <D#>], [<A#>, <d>, <f>], [<c>, <D#>, <g>],
     [<d>, <f>, <a>], [<D#>, <g>, <A#>], [<f>, <a>, <c>]]


