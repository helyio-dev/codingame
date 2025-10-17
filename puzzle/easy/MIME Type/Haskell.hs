import System.IO
import Control.Monad
import System.FilePath
import Data.Char
import qualified Data.Map as Map

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering 

  input_line <- getLine
  let nbElements = read input_line :: Int
  input_line <- getLine
  let nbNames = read input_line :: Int

  associationList <- replicateM nbElements $ do
    input_line <- getLine
    let input = words input_line
    let extension = input!!0
    let mimeType = input!!1
    return (map toLower extension, mimeType)

  let table = Map.fromList associationList

  replicateM nbNames $ do
    name <- getLine
    let extension = map toLower (takeExtension name)
    if extension == "" || extension == "." then
      putStrLn "UNKNOWN"
    else do
      let extWithoutDot = drop 1 extension
      case Map.lookup extWithoutDot table of
        Just mimeType -> putStrLn mimeType
        Nothing -> putStrLn "UNKNOWN"
    return ()
  return ()