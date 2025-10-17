(ns Solution
  (:gen-class))

(defn -main [& args]
  (let [horses (java.util.ArrayList.)]
    (let [N (read)]
      (loop [i N]
        (when (> i 0)
          (.add horses (read))
          (recur (dec i))))
    (java.util.Collections/sort horses)

    (let [diffs (java.util.ArrayList.)]
      (loop [i N]
        (when (> i 1)
          (.add diffs
            (- (.get horses (- i 1)) (.get horses (- i 2)))
          )
          (recur (dec i))))

    (println (java.util.Collections/min diffs))))))