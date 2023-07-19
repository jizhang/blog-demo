#!/usr/bin/perl

use strict;

sub hello {
    for my $i (@_) {
        print $i;
    }
}

my @arr1 = (1, 2);
my @arr2 = (3, 4);

hello @arr1, @arr2;
