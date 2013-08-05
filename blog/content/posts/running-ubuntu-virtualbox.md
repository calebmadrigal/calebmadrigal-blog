author: Caleb Madrigal
comments: true
date: 2012-11-28 18:48:27
layout: post
slug: running-ubuntu-virtualbox
title: Running Ubuntu on VirtualBox in Windows
category: linux
tags: linux

I'm mostly a Mac user and I also really like Linux (especially Ubuntu), but I hate Windows.  However, I'm occasionally required to use Windows at work, so I've found a way to make using Windows more enjoyable: to use Ubuntu (installed on VirtualBox inside of Windows) instead of Windows for everything except for the few tasks which require Windows.


So I have made this little **How to Install Ubuntu on VirtualBox in Windows** setup guide:

## Contents

* Install VirtualBox
* Download Ubuntu 12.04 ISO file
* Create and configure a Virtual Machine
* Tweak Virtual Machine hardware settings
* Install Ubuntu in the Virtual Machine
* Make Ubuntu nicer to use in VirtualBox
* Using your new Virtual Ubuntu system


## Install VirtualBox
	
* Download installer from: https://www.virtualbox.org/wiki/Downloads
* The version I am using is 4.2.4: [http://download.virtualbox.org/virtualbox/4.2.4/VirtualBox-4.2.4-81684-Win.exe](http://download.virtualbox.org/virtualbox/4.2.4/VirtualBox-4.2.4-81684-Win.exe)

## Download Ubuntu 12.04 ISO file
	
* Download 12.04 LTS (12.10 is VERY SLOW in VirtualBox): [http://www.ubuntu.com/download/desktop/questions?distro=desktop&bits;=32&release;=lts](http://www.ubuntu.com/download/desktop/questions?distro=desktop&bits=32&release=lts)

## Create a virtual machine

#### Hit New:

![Virtualbox New](/static/images/virtualbox_new.png)

#### Type: Linux, Version: Ubuntu

![Virtualbox Create VM](/static/images/virtualbox_create_vm.png)

#### 2 Gb memory (At least that's what I used on an 8Gb machine)

![Virtualbox Ram](/static/images/virtualbox_ram.png)


#### Create a virtual hard drive

![Virtualbox HD](/static/images/virtualbox_hd.png)


#### Use VID Format

![Virtualbox HD Format](/static/images/virtualbox_hd_format.png)


#### Create a Fixed size hard drive - they are faster

![Virtualbox HD Fixed Size](/static/images/virtualbox_hd_fixed_size.png)


#### I allocated 10 Gb for my virtual hard drive

![Virtualbox HD Size](/static/images/virtualbox_hd_size.png)


#### Select the Ubuntu ISO as a CD; Go to Settings -> Storage


![Virtualbox CD](/static/images/virtualbox_cd.png)


#### Click "Choose Disk"


![Virtualbox choose disk](/static/images/virtualbox_choose_disk.png)


#### Choose the Ubuntu ISO file


![Virtualbox choose disk2](/static/images/virtualbox_choose_disk2.png)

Then finish out the wizard


## Tweak Virtual Machine hardware settings


#### Open the Settings

![Virtualbox Settings](/static/images/virtualbox_settings.png)


#### Add more Video memory and enable 3d acceleration


![Virtualbox video memory](/static/images/virtualbox_video_mem.png)


#### Default network settings worked for me

![Virtualbox networking](/static/images/virtualbox_network.png)


#### Add shared host drive.  Later, this will allow you to mount your entire windows hard drive from Ubuntu


![Virtualbox shared folders](/static/images/virtualbox_shared_folders.png)


#### Enable copy/paste between Linux and Windows


Go to Settings - General - Advanced and set Shared Clipboard to be "Bidirectional".

![Virtualbox shared clipboard](/static/images/virtualbox_shared_clipboard.png)


Now exit out of the settings.  Time to install Ubuntu.

## Install Ubuntu in the Virtual Machine


#### Click "Start" to start the Virtual Machine

![Virtualbox start](/static/images/virtualbox_start.png)


#### The Virtual Machine should see the "bootable" Ubuntu ISO image and run it automatically.  If this works, you will soon see the Ubuntu installation screen


![Ubuntu install screen](/static/images/ubuntu_install_screen.png)


#### Ubuntu Installation Steps

The wizard will walk you through these, but here are the basic steps:
	
* Click "Install Ubuntu"
* Check "Download updates while installing" and Check "Install this third-party software" (and then click "Continue")
* Select "Erase disk and install Ubuntu" (and then click Continue)
    - Note that this erases your virtual hard drive created just for Ubuntu (not your entire real computer hard drive)
* Click "Install Now"
* While installing, it will prompt you for some basic info like timezone, keyboard layout, etc.  Just do what is best for you.
* Also, while installing, it will prompt you for "Who you are?"  Make sure to pick a username and password which you will remember.
* Also, click "Require password on startup", because you will need this later when you switch to Xubuntu (assuming you want to switch - I recommend it for speed).
* When complete, click restart
* Right click on the CD looking thing near the bottom right of the VirtualBox window to remove the installation disk (the Ubuntu ISO) from the Virtual drive.
* Login when it restarts.

## Make Ubuntu nicer to use in VirtualBox

#### Install "Guest Additions"

The Guest Additions allow Ubuntu to behave better inside of Virtualbox; for example, you can resize the VirtualBox window and Ubuntu will appropriately resize.  Here are the steps:

* Click on Devices - Install Guest Additions (in the VitualBox window).
* Click "Run" on the window that pops up.
* Enter your password on the box that pops up and click "Authenticate"

#### Install Updates

You should get a popup asking if you want to install updates.  If you do, install them.

#### Install Xubuntu

Xubuntu is a customized XFCE packages.  It is much more lightweight than the default Unity window manager.  I also prefer it to Unity

* Open the Terminal
* sudo apt-get install xubuntu-desktop
* Once that finishes installing, log out
* Click the Ubuntu button to switch to the Xubuntu window manage:

![Ubuntu change wm](/static/images/ubuntu_change_wm.png)

* Select "Xubuntu Session"

![Ubuntu change wm2](/static/images/ubuntu_change_wm2.png)

* Then log back in, and you should have a Xubuntu desktop

#### Add access to your entire Windows hard drive within Ubuntu

Run this command at the Terminal (the Terminal can be found under Accessories):

    
    sudo mount -t vboxsf C_DRIVE /media/windows


This command must be run each time you start the Virtual Machine.   I decided to write a script called mountw to run this script:
    
    sudo cat "sudo mount -t vboxsf C_DRIVE /media/windows" > /usr/bin/mountw
    sudo chmod a+x /usr/bin/mountw


Now I can just run "mountw" from the terminal when I want full access to my Windows hard drive.

**The installation/configuration is complete!**


## Using your new Virtual Ubuntu system

You can, of course, just keep Ubuntu running in the VirtualBox window (which is what I do most of the time):

![Ubuntu in windows](/static/images/ubuntu_in_window.png)


Or, you can also use "Seemless mode" by clicking "Host-L" ("Host" is typically the Right Control key, so Right Control+L), which lets you have mesh Linux and Windows windows right beside each other (without having the containing VirtualBox window).  You can click Right Control+L again to get out of Seamless mode:


![Ubuntu in seamless](/static/images/ubuntu_in_seamless.png)


Lastly, if you want to stop using your Virtual Machine for a little while but don't want to turn it off, you can just hit "Right Control+P" to pause it.

Special thanks to [Grant Rettke](http://www.wisdomandwonder.com/) for helping me compile this guide.

