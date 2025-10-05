#include <bits/stdc++.h>

std::map<char, std::vector<std::pair<int, int>>> dir = {
    {'K', {{ -1, -1}, { -1, 0}, { -1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}},
    {'Q', {{ -1, -1}, { -1, 0}, { -1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}},
    {'R', {{ -1, 0}, {0, -1}, {0, 1}, {1, 0}}},
    {'B', {{ -1, -1}, { -1, 1}, {1, -1}, {1, 1}}},
    {'N', {{ -2, -1}, { -2, 1}, { -1, -2}, { -1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}}}
};

struct Piece {
    char pl, type;
    int  y, x;

    Piece(int _y = 0, int _x = 0, char p = ' ', char t = ' ') : y(_y), x(_x), pl(p), type(t) {}

    void get_move_coord(int d, int& y_in, int& x_in) const {
        y_in += (dir.at(toupper(type))[d].first);
        x_in += (dir.at(toupper(type))[d].second);
    }
    
    static bool is_valid(int y, int x) {
        return (y >= 0 && x >= 0 && y < 8 && x < 8);
    }
};

std::vector<Piece> pieces;

bool IsSquareAttacked(int y, int x, char target_player, const std::vector<std::string>& grid) {
    
    for (const auto& piece : pieces) {
        if (piece.pl == target_player) continue;

        if (piece.type == 'P' || piece.type == 'p') {
            int dy_pawn = (piece.type == 'P' ? -1 : 1);
            int dx_pawn[] = { -1, 1 };
            for (int i = 0; i < 2; ++i) {
                int ny = piece.y + dy_pawn;
                int nx = piece.x + dx_pawn[i];
                if (Piece::is_valid(ny, nx) && ny == y && nx == x) return true;
            }
            continue; 
        }

        for (int d = 0; d < std::size(dir.at(toupper(piece.type))); ++d) {
            int ny = piece.y;
            int nx = piece.x;
            
            bool is_long_range = ( std::string::npos == std::string("NK").find(toupper(piece.type)) );

            while (true) {
                piece.get_move_coord(d, ny, nx);

                if (!Piece::is_valid(ny, nx)) break;

                if (ny == y && nx == x) return true;
                
                if (grid[ny][nx] != '.') break; 

                if (!is_long_range) break; 
            }
        }
    }
    return false;
}

bool InCheck(int y, int x, char king_type, const std::vector<std::string>& grid) {
    char player = isupper(king_type) ? 'W' : 'B';
    return IsSquareAttacked(y, x, player, grid);
}

bool Solve(Piece king, std::vector<std::string>& grid) {
    if (!InCheck(king.y, king.x, king.type, grid)) {
        return false; 
    }

    int original_y = king.y;
    int original_x = king.x;
    char player = king.pl;

    Piece* king_ptr = nullptr;
    for (auto& p : pieces) {
        if (p.type == king.type) {
            king_ptr = &p;
            break;
        }
    }
    if (!king_ptr) return true;

    for (int d = 0; d < std::size(dir.at('K')); ++d) {
        int ny = original_y; 
        int nx = original_x;
        
        king.get_move_coord(d, ny, nx); 

        if (!Piece::is_valid(ny, nx)) continue;

        if (grid[ny][nx] != '.' && (isupper(grid[ny][nx]) == isupper(king.type))) continue;

        char original_content = grid[ny][nx];

        bool is_safe_capture = true;
        if (original_content != '.') {
            grid[ny][nx] = '.'; 
            
            if (IsSquareAttacked(ny, nx, player, grid)) {
                 is_safe_capture = false;
            }
            
            grid[ny][nx] = original_content; 
        }

        if (!is_safe_capture) continue;

        grid[original_y][original_x] = '.';
        grid[ny][nx] = king.type;
        king_ptr->y = ny;
        king_ptr->x = nx;
        
        if (!InCheck(ny, nx, king.type, grid)) {
            grid[original_y][original_x] = king.type; 
            grid[ny][nx] = original_content;
            king_ptr->y = original_y;
            king_ptr->x = original_x;

            return false;
        }

        grid[original_y][original_x] = king.type; 
        grid[ny][nx] = original_content; 
        king_ptr->y = original_y;
        king_ptr->x = original_x;
    }

    return true;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    Piece white_king_data, black_king_data;
    
    auto grid = std::vector<std::string>(8);
    for(int i = 0; i < 8; ++i) {
        if (!(std::cin >> grid[i])) break;
    }

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (isalpha( grid[i][j])) {
                char player_char = (isupper(grid[i][j]) ? 'W' : 'B');
                Piece piece(i, j, player_char, grid[i][j]);

                pieces.push_back(piece);

                if (piece.type == 'K') white_king_data = piece;
                else if (piece.type == 'k') black_king_data = piece;
            }
        }
    }

    if (Solve(black_king_data, grid)) {
        std::cout << 'W';
    } 
    else if (Solve(white_king_data, grid)) {
        std::cout << 'B';
    } 
    else {
        std::cout << 'N';
    }

    return 0;
}