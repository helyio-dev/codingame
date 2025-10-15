use std::io;
use std::collections::VecDeque;

#[derive(Clone, Copy)]
enum Direction {
    Bottom = 0x1,
    Left = 0x2,
    Top = 0x4,
    Right = 0x8,
}

impl Direction {
    fn iter() -> impl Iterator<Item = Direction> {
        [Direction::Top, Direction::Right, Direction::Bottom, Direction::Left].into_iter()
    }
}

#[derive(Clone, Copy, PartialEq, Eq)]
struct Vec2 {
    x: usize,
    y: usize,
}

impl Vec2 {
    fn new(x: usize, y: usize) -> Vec2 {
        Vec2 { x, y }
    }

    fn new_from_stdin() -> Vec2 {
        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();
        let v = line.split_whitespace().collect::<Vec<_>>();
        Vec2 {
            x: v[0].parse().unwrap(),
            y: v[1].parse().unwrap(),
        }
    }

    fn neighbor(&self, dir: Direction) -> Option<Vec2> {
        match dir {
            Direction::Top if self.y > 0 => Some(Vec2::new(self.x, self.y - 1)),
            Direction::Right => Some(Vec2::new(self.x + 1, self.y)),
            Direction::Bottom => Some(Vec2::new(self.x, self.y + 1)),
            Direction::Left if self.x > 0 => Some(Vec2::new(self.x - 1, self.y)),
            _ => None,
        }
    }
}

struct Cell {
    walls: u8,
}

impl Cell {
    fn new(c: char) -> Cell {
        Cell {
            walls: c.to_digit(16).unwrap() as u8,
        }
    }

    fn has_wall(&self, dir: Direction) -> bool {
        self.walls & dir as u8 != 0
    }
}

struct Labyrinth {
    w: usize,
    h: usize,
    grid: Vec<Vec<Cell>>,
}

impl Labyrinth {
    fn new_from_stdin() -> Labyrinth {
        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();
        let size = line.split_whitespace().collect::<Vec<_>>();
        let w: usize = size[0].parse().unwrap();
        let h: usize = size[1].parse().unwrap();
        let mut grid = vec![];
        for _ in 0..h {
            let mut s = String::new();
            io::stdin().read_line(&mut s).unwrap();
            let row = s.trim().chars().map(Cell::new).collect::<Vec<_>>();
            grid.push(row);
        }
        Labyrinth { w, h, grid }
    }

    fn in_bounds(&self, v: &Vec2) -> bool {
        v.x < self.w && v.y < self.h
    }

    fn distance(&self, start: Vec2, end: Vec2) -> usize {
        let mut dist = vec![vec![usize::MAX; self.w]; self.h];
        let mut q = VecDeque::new();
        dist[start.y][start.x] = 0;
        q.push_back(start);
        while let Some(cur) = q.pop_front() {
            if cur == end {
                return dist[cur.y][cur.x];
            }
            for dir in Direction::iter() {
                if self.grid[cur.y][cur.x].has_wall(dir) {
                    continue;
                }
                if let Some(next) = cur.neighbor(dir) {
                    if !self.in_bounds(&next) {
                        continue;
                    }
                    if dist[next.y][next.x] == usize::MAX {
                        dist[next.y][next.x] = dist[cur.y][cur.x] + 1;
                        q.push_back(next);
                    }
                }
            }
        }
        0
    }
}

fn main() {
    let start = Vec2::new_from_stdin();
    let rabbit = Vec2::new_from_stdin();
    let lab = Labyrinth::new_from_stdin();
    print!(
        "{} {}",
        lab.distance(start, rabbit),
        lab.distance(rabbit, start)
    );
}
