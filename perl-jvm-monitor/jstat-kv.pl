#!/usr/bin/perl

use strict;

my $pid = 2017;
my @jstat = `jstat -gc $pid`;

$jstat[0] =~ s/^\s+|\s+$//;
$jstat[1] =~ s/^\s+|\s+$//;

#map { s/^\s+|\s+$// } @jstat;

my @kv_keys = split(/\s+/, $jstat[0]);
my @kv_vals = split(/\s+/, $jstat[1]);

my $result = '';
for my $i (0 .. $#kv_keys) {
    $result .= "$kv_keys[$i] $kv_vals[$i]\n";
}

print $result;
