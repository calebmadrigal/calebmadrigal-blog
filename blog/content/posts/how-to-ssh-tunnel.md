author: Caleb Madrigal
comments: true
date: 2014-06-27 19:07:00
layout: post
slug: how-to-ssh-tunnel
title: How to SSH Tunnel
category: networking
tags: networking, linux, security

## When to use an SSH Tunnel?

An SSH Tunnel is perfect for the following scenarios:

* You want to get to a website that a corporate network is blocking.
* You want to encrypt the network traffic for a non-encrypted protocol.

## What is an SSH Tunnel?

An SSH Tunnel is where you tell your local SSH Client to forward your local computer's traffic to a specified SSH Server (over the encrypted SSH protocol). The SSH Server will then act as a proxy for all requests you make on your local computer.

![SSH Tunnel](/images/ssh_tunnel.png)

## How to set up an SSH Tunnel

There are 2 steps to set up an SSH Tunnel, and they both happen on your local computer (**no configuration is needed on the SSH server which will be acting as the proxy**).

### Set 1: Open the tunnel

Run this command on your local computer:

	ssh -D 5000 -N user@yourserver.com

* `user@yourserver.com` is the user/server you would use for normal SSH (e.g. `ssh user@yourserver.com`).
* `5000` is the port you will hit on `localhost` to enter the tunnel (see Step 2).


### Set 2: Direct your network to use the tunnel

Open the network settings, find the Network Proxy configuration section, and set `localhost:5000` as a SOCKS proxy:

![SOCKS proxy network settings](images/ssh_tunnel_proxy_ubuntu.png)


## Ride the tube!

If you did it right, all traffic between your computer and `yourserver.com` should now be encrypted, and `yourserver.com` should be acting as a proxy on your local computer's behalf.

A **simple test to make sure it is working properly** is to Google for "what's my ip" before and after setting up the Tunnel. The IP should change when the Tunnel is on (and should be your server's IP).
