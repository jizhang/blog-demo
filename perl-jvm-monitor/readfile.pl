#!/usr/bin/perl

use strict;

open my $fd, '<', '/proc/diskstats';
while (my $line = <$fd>) {
    print $line;
}

