author: Caleb Madrigal
comments: true
date: 2012-03-12 14:45:40
layout: post
slug: resampling-wheel-algorithm
title: Resampling Wheel Algorithm
category: ai
tags: algorithms, ai

I've been taking the Udacity CS373 (Robotic Car) class, and this week the topic was [Particle filters](http://en.wikipedia.org/wiki/Particle_filter).  Particle filters are basically a localization algorithm that accounts for error in measurements and sensors.

Anyway, part of the Particle Filter algorithm requires the generation of a new set of these things called "particles" based on the particles' weights.  So to accomplish this task, the Resample Wheel algorithm was presented in class.  It is a particularly elegant method of generating a new set of particles by randomly drawing from an old set of particles (with replacement).  The particle weight determines the likelihood of it being picked.

Here is the algorithm (with print statements - I used these to help me understand how the algorithm works):

    
    import random
    
    def generate_new_particles(old_particles, weights):
        N = len(old_particles)
        new_particles = []
        index = int(random.random() * N)
        beta = 0.0
        mw = max(weights)
        for i in range(N):
            beta += random.random() * 2.0 * mw
            print "beta =", beta
            while beta > weights[index]:
                beta -= weights[index]
                index = (index + 1) % N
                print "\tbeta= %f, index = %d, weight = %f" % (beta, index, weights[index])
            new_particles.append(old_particles[index])
        return new_particles
    
    if __name__ == "__main__":
        old_particles = [1, 2, 3, 4]
        weights = [.3, 0, .4, .3]
        new_particles = generate_new_particles(old_particles, weights)
    
        print "old particles =", old_particles
        print "weights =", old_particles
        print "new particles =", new_particles


And here is a sample run (with my debug print statements):
    
    beta = 0.536313558942
    	beta= 0.236314, index = 0, weight = 0.300000
    beta = 0.510275914962
    	beta= 0.210276, index = 1, weight = 0.000000
    	beta= 0.210276, index = 2, weight = 0.400000
    beta = 0.954824882947
    	beta= 0.554825, index = 3, weight = 0.300000
    	beta= 0.254825, index = 0, weight = 0.300000
    beta = 0.678700538951
    	beta= 0.378701, index = 1, weight = 0.000000
    	beta= 0.378701, index = 2, weight = 0.400000
    old particles = [1, 2, 3, 4]
    weights = [1, 2, 3, 4]
    new particles = [1, 3, 1, 3]

