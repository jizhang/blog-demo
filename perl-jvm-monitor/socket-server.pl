#!/usr/bin/perl

use strict;
use IO::Socket::INET;

my $server = IO::Socket::INET->new(
    LocalPort => 10060,
    Type => SOCK_STREAM,
    Reuse => 1,
    Listen => SOMAXCONN
) || die "服务创建失败\n";

while (my $client = $server->accept()) {

    my $line = <$client>;
    chomp($line);

    if ($line =~ /^JVMPORT ([0-9]+)$/) {
        print "RECV $1\n";
        print $client "OK\n";
    } else {
        print "ERROR $line\n";
        print $client "ERROR\n";
    }

    close($client);
}

close($server);

