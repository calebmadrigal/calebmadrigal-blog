author: Caleb Madrigal
comments: true
date: 2016-04-18 00:10:00
layout: post
slug: editing-radio-signals-with-audacity
title: Editing radio signals with Audacity
category: hacking
tags: hacking, security, radio, sdr

You can capture radio signals with [Software-defined Radios](https://en.wikipedia.org/wiki/Software-defined_radio) (SDR), such as the [HackRF](https://greatscottgadgets.com/hackrf/). [Gnu Radio](https://en.wikipedia.org/wiki/GNU_Radio) is the main software I use for receiving and transmitting radio signals, but I've found [Audacity](http://www.audacityteam.org/), a program meant primarily for editing sound files, to be a great program for viewing and editing radio signals.

So I had these remote-controlled outlets (which I bought at Home Depot):

![Remote-controlled outlets](/images/editing_radio_signals_with_audacity/remote_controlled_outlets.jpg)

And I wanted to see what their wireless communication looked like...

So first I recorded the signals of the different outlets with this Gnu Radio Companion flowgraph:

![Record flowgraph](/images/editing_radio_signals_with_audacity/record_flowgraph.png)

A few things to note about this flowgraph:

* It records at around 315 MHz, the frequency at which the remote transmits (which I found by looking up it's FCC ID code online)
* It records 2 million samples per second (something needed for importing into Audacity)
* It saves the radio signals to a file - `/tmp/radio_signal.dat`

I recorded the signal sent by the remote control for both ON and OFF for each of the 3 outlets (so a total of 6 signals).

The next step was to import the signals into Audacity like this:

Go to `File` -> `Import` -> `Raw Data...`:

![Audacity import 1](/images/editing_radio_signals_with_audacity/audacity_import1.png)

Make sure the sample rate is set to `2000000` (2 million samples per second), to match the rate at which it was recorded. I also found it's best to set the channels to 1 - Mono. It's also important to set the Encoding (32-bit float in my case) and Byte order (Little endian on Intel) correctly.

![Audacity import 2](/images/editing_radio_signals_with_audacity/audacity_import2.png)

I was then able to see the waves of the signals in Audacity:

![Audacity signal 1](/images/editing_radio_signals_with_audacity/audacity_signal1.png)

Or zooming in:

![Audacity signal 2](/images/editing_radio_signals_with_audacity/audacity_signal2.png)

Further zooming in, I could finally see the individual bits being transmitted:

![Remote channel 1 on signal blob 1](/images/editing_radio_signals_with_audacity/remote_chan1_on_blob1.png)

So this signal is transmitted with what is called [On-Off Keying](https://en.wikipedia.org/wiki/On-off_keying), which is what almost all wireless devices use to communicate. It just transmits signals by sending long or short pulses - just like [morse code](https://en.wikipedia.org/wiki/Morse_code).

I found that the signals sent always start with a long "on", followed by the signal repeated again and again. Here is the "off" signal for outlet 2:

![Remote channel 1 off signal blob 1 and 2](/images/editing_radio_signals_with_audacity/remote_chan1_off_blob12.png)

So here, you can see that the first group has the long "on" followed by a pattern, and that pattern is repeated a 2nd time in the other group.

Eventually, analyzed all 6 signals (3 on signals and 3 off signals), and found that the data transmitted by the remote looks like this:

    Channel 1 ON:  0     110 10 0 0 10 0 0 0 0 0 0
    Channel 1 OFF: 0     110 10 0 0 0 10 0 0 0 0 0
    Channel 2 ON:  0     110 10 0 0 0 0 10 0 0 0 0
    Channel 2 OFF: 0     110 10 0 0 0 0 0 10 0 0 0
    Channel 3 ON:  0     110 10 0 10 0 0 0 0 0 0 0
    Channel 3 OFF: 0     110 10 10 0 0 0 0 0 0 0 0

Pretty intersting. It looks very possible to brute force :)


