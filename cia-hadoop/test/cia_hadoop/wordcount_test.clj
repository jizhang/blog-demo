(ns cia-hadoop.wordcount-test
  (:use clojure.test
        clojure-hadoop.job
        cia-hadoop.wordcount))

(deftest test-wordcount
  (is (run job)))
