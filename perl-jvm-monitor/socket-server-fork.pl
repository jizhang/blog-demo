#!/usr/bin/perl

use strict;
use IO::Socket::INET;

sub REAPER {
    my $pid;
    while (($pid = waitpid(-1, 'WNOHANG')) > 0) {
        print "SIGCHLD $pid\n";
    }
}

my $interrupted = 0;
sub INTERRUPTER {
    $interrupted = 1;
}

$SIG{CHLD} = \&REAPER;
$SIG{TERM} = \&INTERRUPTER;
$SIG{INT} = \&INTERRUPTER;

my $server = IO::Socket::INET->new(
    LocalPort => 10060,
    Type => SOCK_STREAM,
    Reuse => 1,
    Listen => SOMAXCONN
) || die "服务创建失败\n";

while (!$interrupted) {

    if (my $client = $server->accept()) {

        my $pid = fork();

        if ($pid > 0) {
            close($client);
            print "PID $pid\n";
        } elsif ($pid == 0) {
            close($server);

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
            exit;

        } else {
            print "fork()调用失败\n";
        }
    }
}

close($server);

