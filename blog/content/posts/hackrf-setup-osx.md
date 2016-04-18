author: Caleb Madrigal
comments: true
date: 2016-04-17 22:00:00
layout: post
slug: hackrf-setup-osx-2016
title: HackRF Setup OSX 2016
category: hacking
tags: hacking, security, sdr

These are some pretty raw notes I took while installing the software for using a HackRF on OSX. This is the software I installed:

* Gnu Radio (which comes with Gnu Radio Companion)
* Osmocom Gnu Radio Blocks
* gqrx

## Gnu Radio Installation

### Installed gnuradio via Homebrew

    brew update

    brew tap robotastic/homebrew-hackrf
    brew install gnuradio --with-qt

    brew install hackrf
    brew install --HEAD rtlsdr
    brew link --overwrite rtlsdr

This got GNU Radio and GNU Radio Companion installed, but then I needed to install the Osmocom Gnu Radio Blocks so that Gnu Radio could communicate with the HackRF.

## Installing Osmocom Gnu Radio Blocks

This didn't work:

    brew install --HEAD gr-osmosdr

Build with directions here: <http://sdr.osmocom.org/trac/wiki/GrOsmoSDR>

Had to add this to /Users/caleb/Documents/gnu_radio/repos/gr-osmosdr/lib/redpitaya/redpitaya_sink_c.cc

    #ifndef MSG_NOSIGNAL
        #define MSG_NOSIGNAL 0x0 //Don't request NOSIGNAL on systems where this is not implemented.
    #endif

Find python library path:

    sudo find /usr -iname libpython*.dylib
    # Found python dylib at: /usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib

Use this library path to build `gr-osmosdr`:

    mkdir build
    cd build/
    cmake -DPYTHON_LIBRARY=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib ../

Got warning:   MACOSX_RPATH is not specified for the following targets:  gnuradio-osmosdr

Install it:

    make
    sudo make install
    sudo ldconfig

At some point, I tried this command to install a collection of Gnu Radio Companion Blocks. I don't remember the result:

    brew install gr-baz --HEAD

##### Add config for osmocom blocks:

Create the ~/.gnuradio/config.conf config file for custom block support and add this into it

    [grc]
    local_blocks_path=/usr/local/share/gnuradio/grc/blocks

## Install gqrx

Installed gqrx with installer from here: <http://gqrx.dk/download>


## Other Resources

I found this guide helpful: <https://github.com/robotastic/homebrew-hackrf>

