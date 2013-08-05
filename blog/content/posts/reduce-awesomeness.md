author: Caleb Madrigal
comments: true
date: 2012-09-06 04:30:29
layout: post
slug: reduce-awesomeness
title: Reduce with Python and Clojure
wordpress_id: 345
category: clojure
tags: clojure, functional programming, python

I was just playing around writing an annuity calculator function.  Here is my first version:


    
    
    def calculate_annuity(years, interest=0, addition_per_year=0, starting_amount=0):
        result = []
        running_total = starting_amount
        for year in range(years+1):
            result.append(running_total)
            running_total = (running_total + addition_per_year) * (1 + interest)
        return result
    



Here is a 2nd version, written using reduce instead of a loop:

    
    
    def calculate_annuity2(years, interest=0, addition_per_year=0, starting_amount=0):
        return reduce(lambda result,addition: result + [(result[-1] + addition) * (1 + interest)],
                      [addition_per_year] * years, [starting_amount])
    



And here is a version in Clojure (basically a direct translation of the Python one:


    
    
    (defn annuity [years interest addition_per_year init]
        (reduce
            #(conj %1 (* (+ (last %1) %2) (+ 1 interest)))
            [starting_amount]
            (for [i (range years)] addition_per_year)))
    



Here are some example use cases:


    
    
    ; Find investment returns by year for a $1000 investment at 7% interest
    ; for 10 years.
    (println (annuity 10 0.07 0 1000))
    
    ; Find annuity value if contributing $1000 each month and starting with $7777
    ; with 10% interest for 10 years.
    (println (annuity 10 0.10 1000 7777))
    
    ; Find annuity value if contributing $1000 each month and starting with $777
    ; with 10% interest for 10 years.
    (println (annuity 10 0.07 0 1000))
    
    ; Test perpetuity annuity that pays out $6000 per year, given a $100000
    ; at 6.4% interest.
    (println (annuity 30 0.064 -6000 100000))
    
