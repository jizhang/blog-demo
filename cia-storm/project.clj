(defproject cia-storm "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.4.0"]
                 [org.clojure/tools.logging "0.2.6"]]
  :profiles {:dev {:dependencies [[storm "0.8.2"]]}}
  :plugins [[lein2-eclipse "2.0.0"]]
  :aot [cia-storm.wordcount])
