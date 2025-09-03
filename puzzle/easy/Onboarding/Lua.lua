while true do
    enemy1 = io.read()
    dist1 = tonumber(io.read())
    enemy2 = io.read()
    dist2 = tonumber(io.read())
    
    if dist1 < dist2 then
        print(enemy1)
    else
        print(enemy2)
    end
end
