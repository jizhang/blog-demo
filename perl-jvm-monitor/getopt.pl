#!/usr/bin/perl

use strict;
use Getopt::Long;
use Pod::Usage;

my $help = 0;
my $port = 10060;

GetOptions(
    'help|?' => \$help,
    'port=i' => \$port
) || pod2usage(2);
pod2usage(1) if $help;

print "PORT $port\n";

__END__

=head1 NAME

getopt

=head1 SYNOPSIS

getopt.pl [options]

 Options:
   -help brief help message
   -port bind to tcp port

=cut

