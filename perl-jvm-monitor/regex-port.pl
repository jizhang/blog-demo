#!/usr/bin/perl

use strict;

my $line = 'JVMPORT 2181';
if ($line =~ /^JVMPORT ([0-9]+)$/) {
    print $1, "\n"; # 输出 2181
} else {
    print '匹配失败', "\n";
}
