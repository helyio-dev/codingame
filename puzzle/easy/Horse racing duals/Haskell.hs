import System.IO
import Control.Monad
import Data.List

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering 
  
  input_line <- getLine
  let n = read input_line :: Int

  horses <- replicateM n $ do
    input_line <- getLine
    let horse = read input_line :: Int
    return horse
  
  let sorted = sort horses

  let diffs = zipWith (-) (tail sorted) (init sorted)
  
  putStrLn (show (minimum diffs))
  return ()