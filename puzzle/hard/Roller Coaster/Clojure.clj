(ns Solution
  (:require [clojure.string :as str])
  (:gen-class))

(defn output [msg] (println msg) (flush))
(defn debug [msg] (binding [*out* *err*] (println msg) (flush)))

(defn -main [& args]
  (let [[L C N] (map #(Integer/parseInt %) (filter #(not-empty %) (str/split (read-line) #" ")))
        groupes (vec (repeatedly N #(Integer/parseInt (read-line))))
        gains (int-array N)
        groupeSuivant (int-array N)]
    
    (dotimes [i N]
      (loop [current i total 0]
        (let [nextGp (groupes current)]
          (if (> (+ total nextGp) L)
            (do
              (aset gains i total)
              (aset groupeSuivant i current))
            (let [new-total (+ total nextGp)
                  next-idx (mod (inc current) N)]
              (if (= next-idx i)
                (do
                  (aset gains i new-total)
                  (aset groupeSuivant i i))
                (recur next-idx new-total)))))))

    (loop [i 0 c C total 0]
      (if (zero? c)
        (output total)
        (recur (aget groupeSuivant i)
               (dec c)
               (+ total (aget gains i)))))))
