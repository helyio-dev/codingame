import System.IO
import Control.Monad
import Text.Regex

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering 
  
  input_line <- getLine
  let lon = toRadians(input_line :: String)
  input_line <- getLine
  let lat = toRadians(input_line :: String)
  input_line <- getLine
  let n = read input_line :: Int
  
  defibrillators <- replicateM n $ do
    d <- getLine
    let defib = splitRegex (mkRegex ";") d
    let name = defib !! 1
    let defibLon = toRadians(defib !! 4)
    let defibLat = toRadians(defib !! 5)
    let x = (defibLon - lon) * cos((lat + defibLat) / 2)
    let y = defibLat - lat
    let distance = sqrt(x^2 + y^2) * 6371
    return (distance, name)
  
  let closestDefib = minimum defibrillators
  putStrLn (snd closestDefib)
  return ()

toRadians :: String -> Double
toRadians angle = (read (map replace angle) :: Double) * pi / 180

replace :: Char -> Char
replace ',' = '.'
replace c = c