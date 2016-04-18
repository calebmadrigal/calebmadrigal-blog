author: Caleb Madrigal
comments: true
date: 2016-04-18 00:20:00
layout: post
slug: hackrf-replay-attack-jeep
title: HackRF Replay Attack Jeep
category: hacking
tags: hacking, security, radio, sdr

I've recently been getting into [Software-defined Radio](https://en.wikipedia.org/wiki/Software-defined_radio) (SDR), mostly using a [HackRF](https://greatscottgadgets.com/hackrf/) - a radio tranceiver capable of operating from 1MHz to 6GHz (which is a huge range).

One of the most simple (and most interesting attacks) which can be done with SDR is what's called a [Replay Attack](https://en.wikipedia.org/wiki/Replay_attack). It works by simply recording a signal, and then rebroadcasting it. I was able to use this attack to lock and unlock my Jeep Patriot (2006) with my computer. Here's how...


First I recorded the "unlock" and "lock" signals from my [keyless entry remote](https://en.wikipedia.org/wiki/Remote_keyless_system) using this "flowgraph" in Gnu Radio Companion:

![Record flowgraph](/images/hackrf_replay_attack_jeep/record_flowgraph.png)

A couple things to note about this flow graph:

* The frequency is 315 MHz (the frequency at which pretty much all keyless entry)
* It records at 2 million samples per second (a piece of data needed for importing into Audacity later)
* It saves to this file, 'radio_signal.dat'
* It also shows a "waterfall graph" of what it is recording

Here is what the waterfall graph of the recording looks like. This is first the "unlock" signal, followed by the "lock" signal:

![Unlock and lock signals waterfall](/images/hackrf_replay_attack_jeep/unlock_lock_signals_waterfall.png)

Now I could simply replay this recording in order to execute a replay attack. But wanted to explore these signals in a bit more detail. So I decided to try to trim them down using [Audacity](http://www.audacityteam.org/). Though Audacity is primarily intended as sound editing software, it can also be used for editing the wave forms of radio signals (which is pretty awesome! Waves are just waves, whether transmitted by sound or radio).

Here is what the "unlock" and "lock" signals look like in Audacity:

![View signals in audacity](/images/hackrf_replay_attack_jeep/audacity_signals1.png)

So here, you can clearly see the 2 distinct signals: first Unlock, then Lock. From here, I can select and export each of the signals to different files...

![Export signals in audacity](/images/hackrf_replay_attack_jeep/audacity_signals2.png)

So then I had 2 raw signal files:

    cmbpr:gnu_radio caleb$ ls -lh |grep raw
    -rw-r--r--@ 1 caleb  staff    11M Apr 16 11:09 jeep_lock.raw
    -rw-r--r--@ 1 caleb  staff    10M Apr 16 11:09 jeep_unlock.raw

Note that even after trimming these down, the files are still ~10Mb each.

Finally, the last step was to create a flowgraph to transmit each of the messages. It looked like this:

![Replay flowgraph](/images/hackrf_replay_attack_jeep/replay_flowgraph.png)

In order to make nice command-line scripts, I just modified the `top_block.py` script which gnuradio-companion outputs, and had one (`jeep_unlock.py`) transmit the `jeep_unlock.raw` file, and the other (`lock_jeep.py`) transmit the `jeep_lock.raw` file.

Here is a video showing me using these 2 scripts to unlock and lock the jeep:

<iframe width="560" height="315" src="https://www.youtube.com/embed/eReBJl7te-A" frameborder="0" allowfullscreen></iframe>


