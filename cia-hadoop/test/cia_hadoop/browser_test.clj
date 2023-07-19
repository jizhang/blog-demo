(ns cia-hadoop.browser-test
  (:use clojure.test
        clojure-hadoop.job
        cia-hadoop.browser))

(deftest test-my-map
  (is (= [["ie" 1]] (my-map 0 "{\"agent\":\"MSIE 6.0\"}")))
  (is (= [["chrome" 1]] (my-map 0 "{\"agent\":\"Chrome/20.0 Safari/6533.2\"}")))
  (is (= [["other" 1]] (my-map 0 "{\"agent\":\"abc\"}")))
  (is (nil? (my-map 0 "{"))))

(deftest test-browser
  (is (run job)))
