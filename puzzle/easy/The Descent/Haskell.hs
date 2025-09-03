import System.IO
import Control.Monad

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering
    forever $ do
        mountains <- replicateM 8 getLine
        let heights = map read mountains :: [Int]
        let (maxH, maxIndex) = foldl (\(h, i) (currentH, currentIndex) -> 
                if currentH > h then (currentH, currentIndex) else (h, i)) 
                (-1, 0) (zip heights [0..])
        putStrLn (show maxIndex)
