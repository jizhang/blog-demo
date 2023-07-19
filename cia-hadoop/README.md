# Clojure in Action: Write Hadoop MapReduce Job

## Usage

### Import into Eclipse

    $ lein eclipse

### Wordcount Example

* Run locally with `lein`:

    $ lein test

* Compile:

    $ lein uberjar

* Run locally with `java`:

    $ java -cp target/cia-hadoop-0.1.0-SNAPSHOT-standalone.jar clojure_hadoop.job -job cia-hadoop.wordcount/job

* Run on a cluster:

    $ hadoop jar target/cia-hadoop-0.1.0-SNAPSHOT-standalone.jar clojure_hadoop.job -job cia-hadoop.wordcount/job

## License

Copyright © 2013 Ji ZHANG <zhangji87@gmail.com>

Distributed under the Eclipse Public License, the same as Clojure.
