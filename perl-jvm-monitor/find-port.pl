#!/usr/bin/perl

use strict;

my $pid;
my $jvmport = '2181';
my @netstat = `netstat -lntp 2>/dev/null`;
foreach my $line (@netstat) {
    if ($line =~ /.*?:$jvmport\s.*?([0-9]+)\/java\s*$/) {
        $pid = $1;
        last;
    }
}
if ($pid) {
    print $pid, "\n";
} else {
    print '端口不存在', "\n";
}

