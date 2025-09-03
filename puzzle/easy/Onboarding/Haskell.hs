import System.IO
import Control.Monad

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering
    
    forever $ do
        enemy1 <- getLine
        dist1_str <- getLine
        let dist1 = read dist1_str :: Int
        enemy2 <- getLine
        dist2_str <- getLine
        let dist2 = read dist2_str :: Int
        
        if dist1 < dist2 then
            putStrLn enemy1
        else
            putStrLn enemy2
