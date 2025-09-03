(ns Player
  (:require [clojure.string :as str])
  (:gen-class))

(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (while true
    (loop [i 0
           max-h -1
           mountain-to-fire 0]
      (if (< i 8)
        (let [mountainH (Integer/parseInt (read-line))]
          (if (> mountainH max-h)
            (recur (inc i) mountainH i)
            (recur (inc i) max-h mountain-to-fire)))
        (output mountain-to-fire)))))
