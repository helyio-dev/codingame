function sumDigits(n)
    local s = tostring(n)
    local sum = 0
    for i = 1, #s do
        sum = sum + tonumber(s:sub(i, i))
    end
    return sum
end

local R = tonumber(io.read())
local C = tonumber(io.read())
local T = tonumber(io.read())

local visited = {}
for i = 1, R do
    visited[i] = {}
    for j = 1, C do
        visited[i][j] = false
    end
end

local queue = {}
local count = 0

if sumDigits(0) + sumDigits(0) <= T then
    table.insert(queue, {1, 1})
    visited[1][1] = true
    count = 1
end

local directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

while #queue > 0 do
    local cell = table.remove(queue, 1)
    local x, y = cell[1], cell[2]
    
    for _, dir in ipairs(directions) do
        local nx = x + dir[1]
        local ny = y + dir[2]
        
        if nx >= 1 and nx <= R and ny >= 1 and ny <= C and not visited[nx][ny] then
            if sumDigits(nx-1) + sumDigits(ny-1) <= T then
                visited[nx][ny] = true
                table.insert(queue, {nx, ny})
                count = count + 1
            end
        end
    end
end

print(count)