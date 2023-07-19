#!/usr/bin/perl

use strict;

sub kv_parse {

    my @kv_data = @_;

    map { s/^\s+|\s+$// } @kv_data;
    
    my @kv_keys = split(/\s+/, $kv_data[0]);
    my @kv_vals = split(/\s+/, $kv_data[1]);
    
    my $result = '';
    for my $i (0 .. $#kv_keys) {
        $result .= "$kv_keys[$i] $kv_vals[$i]\n";
    }

    return $result;

}

my $pid = 2017;
my @jstat = `jstat -gc $pid`;
my @ps = `ps -o pcpu,rss -p $pid`;

print kv_parse(@jstat);
print kv_parse(@ps);

