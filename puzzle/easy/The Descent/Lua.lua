while true do
    local maxH = -1
    local mountainToFire = 0
    for i=0,7 do
        local mountainH = tonumber(io.read())
        if mountainH > maxH then
            maxH = mountainH
            mountainToFire = i
        end
    end
    
    print(mountainToFire)
end
