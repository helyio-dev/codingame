import Data.List
import Control.Monad

data Player = Player { posX :: Int, posY :: Int, isActive :: Bool }
data GameState = GameState { teamA :: [Player], teamB :: [Player], ballX :: Int, ballY :: Int, attacker :: Char }

main :: IO ()
main = do
    rows <- replicateM 15 getLine
    let gs = parseGrid rows
    let (count, isOffside) = checkOffside gs
    
    if count == 0 
        then putStrLn "No player in an offside position."
        else putStrLn $ show count ++ " player(s) in an offside position."
    
    putStrLn $ if isOffside then "VAR: OFFSIDE!" else "VAR: ONSIDE!"

parseGrid :: [String] -> GameState
parseGrid rows = foldl' findEntities (GameState [] [] 0 0 ' ') coords
  where
    coords = [(x, y, (rows !! y) !! x) | y <- [0..14], x <- [0..50]]
    findEntities gs (x, y, char)
        | char `elem` "aA" = gs { teamA = Player x y (char == 'A') : teamA gs }
        | char `elem` "bB" = gs { teamB = Player x y (char == 'B') : teamB gs }
        | char == 'o'      = gs { ballX = x, ballY = y, attacker = 'A' }
        | char == 'O'      = gs { ballX = x, ballY = y, attacker = 'B' }
        | otherwise        = gs

checkOffside :: GameState -> (Int, Bool)
checkOffside gs
    | ballY gs == 0 || ballY gs == 14 = (0, False)
    | attacker gs == 'A' = 
        let sortedOpp = sort $ map posX (teamB gs)
            limit = sortedOpp !! 1
            offsides = filter (\p -> posX p < 25 && posX p < ballX gs && posX p < limit) (teamA gs)
        in (length offsides, any isActive offsides)
    | otherwise = 
        let sortedOpp = sortBy (flip compare) $ map posX (teamA gs)
            limit = sortedOpp !! 1
            offsides = filter (\p -> posX p > 25 && posX p > ballX gs && posX p > limit) (teamB gs)
        in (length offsides, any isActive offsides)