(ns cia-hadoop.browser
  (:require [clojure-hadoop.wrap :as wrap]
            [clojure-hadoop.defjob :as defjob]
            [clojure.data.json :as json])
  (:use clojure-hadoop.job))

(defn json-decode [s]
  (try
    (json/read-str s)
    (catch Exception e)))

(def rule-set {"ie" (partial re-find #"(?i)MSIE [0-9]+")
               "chrome" (partial re-find #"(?i)Chrome/[0-9]+")
               "firefox" (partial re-find #"(?i)Firefox/[0-9]+")
               "opera" (partial re-find #"(?i)Opera/[0-9]+")
               "safari" #(and (re-find #"(?i)Safari/[0-9]+" %)
                              (not (re-find #"(?i)Chrom(e|ium)/[0-9]+" %)))
               })

(defn get-type [ua]
  (if-let [rule (first (filter #((second %) ua) rule-set))]
    (first rule)
    "other"))

(defn my-map [key value]
  (when-let [ua (get (json-decode value) "agent")]
    [[(get-type ua) 1]]))

(defn my-reduce [key values-fn]
  [[key (reduce + (values-fn))]])

(defjob/defjob job
  :map my-map
  :map-reader wrap/int-string-map-reader
  :reduce my-reduce
  :input-format :text
  :output-format :text
  :compress-output false
  :replace true
  :input "user_agent.log"
  :output "out-browser")
