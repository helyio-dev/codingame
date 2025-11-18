sub sum_digits {
    my $n = shift;
    my $sum = 0;
    $sum += $_ for split //, $n;
    return $sum;
}

my $R = <STDIN>;
my $C = <STDIN>;
my $T = <STDIN>;

my @visited;
for my $i (0..$R-1) {
    for my $j (0..$C-1) {
        $visited[$i][$j] = 0;
    }
}

my @queue;
my $count = 0;

if (sum_digits(0) + sum_digits(0) <= $T) {
    push @queue, [0, 0];
    $visited[0][0] = 1;
    $count = 1;
}

my @directions = ([0,1], [1,0], [0,-1], [-1,0]);

while (@queue) {
    my $cell = shift @queue;
    my ($x, $y) = @$cell;
    
    for my $dir (@directions) {
        my ($dx, $dy) = @$dir;
        my $nx = $x + $dx;
        my $ny = $y + $dy;
        
        if ($nx >= 0 && $nx < $R && $ny >= 0 && $ny < $C && !$visited[$nx][$ny]) {
            if (sum_digits($nx) + sum_digits($ny) <= $T) {
                $visited[$nx][$ny] = 1;
                push @queue, [$nx, $ny];
                $count++;
            }
        }
    }
}

print "$count\n";