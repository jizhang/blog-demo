(ns cia-storm.wordcount
  (:import [backtype.storm StormSubmitter LocalCluster])
  (:use [backtype.storm clojure config])
  (:require [clojure.tools.logging :as logging])
  (:gen-class))

(defspout sentence-spout ["sentence"]
  [conf context collector]
  (let [sentences ["a little brown dog"
                   "the man petted the dog"
                   "four score and seven years ago"
                   "an apple a day keeps the doctor away"]]
    (spout
      (nextTuple []
        (Thread/sleep 100)
        (emit-spout! collector [(rand-nth sentences)])))))

;(defspout sentence-spout ["sentence"] {:prepare false}
;  [collector]
;  (Thread/sleep 1000)
;  (emit-spout! collector [(rand-nth ["a little brown dog"
;                                     "the man petted the dog"
;                                     "four score and seven years ago"
;                                     "an apple a day keeps the doctor away"])]))

;(defbolt split-bolt ["word"] {:prepare true}
;  [conf context collector]
;  (bolt
;    (execute [tuple]
;      (let [words (.split (.getString tuple 0) " ")]
;        (doseq [w words]
;          (emit-bolt! collector [w])))
;      (ack! collector tuple))))

(defbolt split-bolt ["word"]
  [tuple collector]
  (let [words (.split (.getString tuple 0) " ")]
    (doseq [w words]
      (emit-bolt! collector [w]))
    (ack! collector tuple)))

(defbolt count-bolt [] {:prepare true}
  [conf context collector]
  (let [counts (atom {})]
    (bolt
      (prepare [conf context collector]
        (.start (Thread. (fn []
                           (while (not (Thread/interrupted))
                             (logging/info
                               (clojure.string/join ", "
                                 (for [[word count] @counts]
                                   (str word ": " count))))
                             (reset! counts {})
                             (Thread/sleep 5000))))))
      (execute [tuple]
        (let [word (.getString tuple 0)]
          (swap! counts (partial merge-with +) {word 1}))
        (ack! collector tuple)))))

(defn mk-topology []
  (topology
    {"sentence" (spout-spec sentence-spout)}
    {"split" (bolt-spec {"sentence" :shuffle}
                        split-bolt
                        :p 3)
     "count" (bolt-spec {"split" ["word"]}
                        count-bolt
                        :p 2)}))

(defn run-local! []
  (let [cluster (LocalCluster.)]
    (.submitTopology cluster
      "wordcount" {} (mk-topology))
    (Thread/sleep 30000)
    (.shutdown cluster)))

(defn submit-topology! [name]
  (StormSubmitter/submitTopology
    name {TOPOLOGY-WORKERS 3} (mk-topology)))

(defn -main
  ([]
    (run-local!))
  ([name]
    (submit-topology! name)))
