(ns Player
  (:require [clojure.string :as str])
  (:gen-class))

(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (while true
    (let [enemy1 (read-line)
          dist1 (Integer/parseInt (read-line))
          enemy2 (read-line)
          dist2 (Integer/parseInt (read-line))]
      (if (< dist1 dist2)
        (output enemy1)
        (output enemy2)))))
