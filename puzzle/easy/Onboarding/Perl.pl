use strict;
use warnings;
use 5.32.1;

select(STDOUT); $| = 1;

while (1) {
    chomp(my $enemy_1 = <STDIN>);
    chomp(my $dist_1 = <STDIN>);
    chomp(my $enemy_2 = <STDIN>);
    chomp(my $dist_2 = <STDIN>);

    if ($dist_1 < $dist_2) {
        print "$enemy_1\n";
    } else {
        print "$enemy_2\n";
    }
}
