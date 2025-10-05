#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <tuple>

using namespace std;

void simulate_infection(int n, vector<string>& grid) {
    while (true) {
        vector<pair<int, int>> newly_infected;
        vector<pair<int, int>> current_contagious;

        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 'C') {
                    current_contagious.push_back({r, c});
                }
            }
        }

        int dr[] = {-1, -1, 1, 1};
        int dc[] = {-1, 1, -1, 1};
        
        for (const auto& pos : current_contagious) {
            int r0 = pos.first;
            int c0 = pos.second;

            for (int i = 0; i < 4; ++i) {
                int r = r0 + dr[i];
                int c = c0 + dc[i];

                while (r >= 0 && r < n && c >= 0 && c < n) {
                    if (grid[r][c] == 'H') {
                        break;
                    }
                    if (grid[r][c] == '.') {
                        newly_infected.push_back({r, c});
                        break;
                    }
                    if (grid[r][c] == 'C') {
                        break; 
                    }
                    
                    r += dr[i];
                    c += dc[i];
                }
            }
        }

        if (newly_infected.empty()) {
            break;
        }

        for (const auto& pos : newly_infected) {
            if (grid[pos.first][pos.second] == '.') { 
                grid[pos.first][pos.second] = 'C';
            }
        }
    }
}

int count_infected(int n, const vector<string>& grid) {
    int count = 0;
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            if (grid[r][c] == 'C') {
                count++;
            }
        }
    }
    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, g;
    cin >> n >> g;

    vector<vector<string>> all_grids(g, vector<string>(n));
    for (int i = 0; i < g; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> all_grids[i][j];
        }
    }

    int max_infected_count = -1;
    int best_grid_index = -1;
    vector<string> best_grid_aftermath;

    for (int i = 0; i < g; ++i) {
        vector<string> current_grid = all_grids[i];
        simulate_infection(n, current_grid);

        int current_infected_count = count_infected(n, current_grid);

        if (current_infected_count > max_infected_count) {
            max_infected_count = current_infected_count;
            best_grid_index = i;
            best_grid_aftermath = current_grid;
        }
    }

    cout << best_grid_index << "\n";
    for (const string& row : best_grid_aftermath) {
        cout << row << "\n";
    }

    return 0;
}